#!/usr/bin/env python3
"""
《泡泡知道自己在哪裡》插圖生成Pipeline
使用Stable Diffusion自動生成所有插圖
"""

import torch
import json
import os
from pathlib import Path
from PIL import Image
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import logging
from tqdm import tqdm
import time

# 設置日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BubbleBookGenerator:
    """泡泡書籍插圖生成器"""
    
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5"):
        """初始化生成器"""
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipeline = None
        self.output_dir = Path("illustrations/generated")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 載入提示詞配置
        self.load_prompts()
        
        logger.info(f"使用設備: {self.device}")
        logger.info(f"模型: {self.model_name}")
    
    def load_prompts(self):
        """載入提示詞配置"""
        config_path = Path("illustrations/generation_config.json")
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            self.prompts = config['illustrations']
            logger.info(f"載入 {len(self.prompts)} 個提示詞")
        else:
            # 使用內建提示詞
            self.prompts = self.get_default_prompts()
            logger.info("使用內建提示詞")
    
    def get_default_prompts(self):
        """內建提示詞"""
        return {
            "cover": {
                "prompt": "A large transparent soap bubble floating in soft sky blue gradient background, rainbow prismatic edges, gentle watercolor illustration style, children's book cover, cute bubble with friendly expression, dreamy atmosphere, soft lighting, pastel colors, 20cm x 20cm square format",
                "negative": "dark, scary, sharp edges, complex details, adult themes"
            },
            "page_01_birth": {
                "prompt": "Cute cartoon bubble blower machine with smiley face, transparent soap bubble flying out with dotted trail lines, pure white background, gentle watercolor style, children's illustration, soft pastel colors, playful atmosphere, bubble trajectory arrows, friendly cartoon style",
                "negative": "dark background, sharp edges, realistic photography, complex machinery"
            },
            "page_02_mirror": {
                "prompt": "Transparent soap bubble looking at oval mirror with classical frame, reflection of bubble in mirror with faded colors and dotted border, surprised and happy bubble expressions, round speech bubbles, soft watercolor illustration, gentle lighting, children's book style",
                "negative": "realistic mirror, dark reflections, sharp edges, adult themes"
            },
            "page_03_world": {
                "prompt": "Large transparent soap bubble in center of page, rainbow spectrum flowing inside bubble, flowing wind lines surrounding outside, clear boundary line slightly thickened, soft watercolor style, gentle gradient colors, children's illustration, dreamy atmosphere",
                "negative": "dark colors, sharp boundaries, realistic physics, complex details"
            },
            "page_04_expanding": {
                "prompt": "Expanding soap bubble with multiple bubble contours showing growth process, outward spreading dynamic lines, boundary gradually thinning, tension building effect, deeper colors and dense lines, soft watercolor illustration, children's book style, gentle expansion",
                "negative": "explosive, violent, sharp edges, dark tension, scary expansion"
            },
            "page_05_burst": {
                "prompt": "Explosive burst effect with colorful rainbow fragments scattering in all directions, spiral wind vortex lines, dynamic tilted composition, soap bubble breaking moment, soft watercolor style, gentle explosion, children's illustration, colorful chaos",
                "negative": "violent explosion, sharp fragments, dark colors, scary elements"
            },
            "page_06_new_bubble": {
                "prompt": "New transparent soap bubble with happy smiley face, bright colors showing new beginning, same design as page 1 but with added smile, gentle watercolor style, children's illustration, hopeful atmosphere, soft lighting, rebirth theme",
                "negative": "dark rebirth, sad expression, sharp edges, complex details"
            },
            "page_07_friends": {
                "prompt": "Group of 3-5 soap bubbles in different sizes, each with unique rainbow colors inside, naturally scattered arrangement maintaining visual balance, each bubble with individual characteristics, soft watercolor style, children's illustration, friendly group scene",
                "negative": "crowded, chaotic arrangement, dark colors, sharp edges, too many bubbles"
            },
            "page_08_hug": {
                "prompt": "Two soap bubbles gently touching with overlapping boundaries, blurred boundary effect using dotted lines and faded colors, heart symbol at contact point, confused questioning expressions on bubbles, soft watercolor style, children's illustration, gentle contact",
                "negative": "violent collision, sharp contact, dark emotions, complex physics"
            },
            "page_09_merge": {
                "prompt": "Two soap bubbles merging into one large bubble with arrow showing transformation, mixed rainbow colors inside large bubble, newly drawn clear boundary, soft watercolor style, children's illustration, gentle fusion process, unity theme",
                "negative": "violent merger, sharp transformation, dark fusion, complex physics"
            },
            "page_10_thinking": {
                "prompt": "Single soap bubble floating quietly with thinking expression, small thought bubbles surrounding large bubble, calm colors and peaceful composition, contemplative atmosphere, soft watercolor style, children's illustration, philosophical mood",
                "negative": "dark contemplation, sharp thoughts, scary philosophy, complex thinking"
            },
            "page_11_understanding": {
                "prompt": "Happy soap bubble with bright smile, artistic brush strokes surrounding bubble showing creativity, bright colors and open composition, enlightenment feeling, soft watercolor style, children's illustration, joyful realization, creative atmosphere",
                "negative": "dark enlightenment, sharp realization, scary creativity, complex art"
            },
            "page_12_continuing": {
                "prompt": "Soap bubble flying toward edge of page, infinite gradient sky background extending to infinity, warm colors and complete composition, continuous flying motion, soft watercolor style, children's illustration, eternal journey theme",
                "negative": "dark journey, sharp flying, scary infinity, complex travel"
            }
        }
    
    def load_model(self):
        """載入Stable Diffusion模型"""
        logger.info("載入Stable Diffusion模型...")
        
        try:
            # 載入pipeline
            self.pipeline = StableDiffusionPipeline.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                safety_checker=None,
                requires_safety_checker=False
            )
            
            # 設置調度器
            self.pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
                self.pipeline.scheduler.config
            )
            
            # 移到設備
            self.pipeline = self.pipeline.to(self.device)
            
            # 啟用記憶體優化
            if self.device == "cuda":
                self.pipeline.enable_attention_slicing()
                self.pipeline.enable_vae_slicing()
            
            logger.info("模型載入完成")
            return True
            
        except Exception as e:
            logger.error(f"模型載入失敗: {e}")
            return False
    
    def generate_image(self, prompt, negative_prompt, page_id, num_inference_steps=20, guidance_scale=7.5):
        """生成單張圖片"""
        logger.info(f"生成 {page_id}...")
        
        try:
            # 添加風格關鍵詞
            style_tags = "children's book illustration, soft watercolor, gentle colors, pastel colors, dreamy atmosphere"
            full_prompt = f"{prompt}, {style_tags}"
            
            # 生成圖片
            with torch.autocast(self.device):
                result = self.pipeline(
                    prompt=full_prompt,
                    negative_prompt=negative_prompt,
                    num_inference_steps=num_inference_steps,
                    guidance_scale=guidance_scale,
                    width=1024,
                    height=1024,
                    num_images_per_prompt=1
                )
            
            # 保存圖片
            image = result.images[0]
            output_path = self.output_dir / f"{page_id}_v1.png"
            image.save(output_path, "PNG", quality=95)
            
            logger.info(f"✅ {page_id} 生成完成: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"❌ {page_id} 生成失敗: {e}")
            return None
    
    def generate_all_images(self, num_variations=3):
        """生成所有插圖"""
        if not self.pipeline:
            logger.error("模型未載入，請先運行 load_model()")
            return False
        
        logger.info(f"開始生成 {len(self.prompts)} 個插圖，每個 {num_variations} 個變體...")
        
        results = {}
        
        for page_id, prompt_data in tqdm(self.prompts.items(), desc="生成插圖"):
            page_results = []
            
            for i in range(num_variations):
                output_path = self.generate_image(
                    prompt_data["prompt"],
                    prompt_data["negative"],
                    f"{page_id}_v{i+1}",
                    num_inference_steps=25,
                    guidance_scale=7.5
                )
                
                if output_path:
                    page_results.append(output_path)
                
                # 短暫休息避免過熱
                time.sleep(1)
            
            results[page_id] = page_results
            
            if page_results:
                logger.info(f"✅ {page_id}: 生成 {len(page_results)} 張圖片")
            else:
                logger.error(f"❌ {page_id}: 生成失敗")
        
        return results
    
    def generate_single_page(self, page_id, num_variations=3):
        """生成單頁插圖"""
        if page_id not in self.prompts:
            logger.error(f"找不到頁面: {page_id}")
            return None
        
        if not self.pipeline:
            logger.error("模型未載入，請先運行 load_model()")
            return None
        
        prompt_data = self.prompts[page_id]
        results = []
        
        for i in range(num_variations):
            output_path = self.generate_image(
                prompt_data["prompt"],
                prompt_data["negative"],
                f"{page_id}_v{i+1}",
                num_inference_steps=25,
                guidance_scale=7.5
            )
            
            if output_path:
                results.append(output_path)
        
        return results

def main():
    """主函數"""
    print("🎨 《泡泡知道自己在哪裡》插圖生成Pipeline")
    print("=" * 60)
    
    # 創建生成器
    generator = BubbleBookGenerator()
    
    # 載入模型
    if not generator.load_model():
        print("❌ 模型載入失敗，請檢查環境設置")
        return False
    
    # 詢問生成模式
    print("\n選擇生成模式:")
    print("1. 生成所有插圖 (13頁)")
    print("2. 生成單頁插圖")
    print("3. 生成封面")
    
    choice = input("請選擇 (1-3): ").strip()
    
    if choice == "1":
        # 生成所有插圖
        print("\n🚀 開始生成所有插圖...")
        results = generator.generate_all_images(num_variations=3)
        
        if results:
            print("\n🎉 生成完成！")
            print("📁 圖片保存在: illustrations/generated/")
            
            # 顯示結果統計
            total_generated = sum(len(pages) for pages in results.values())
            successful_pages = len([pages for pages in results.values() if pages])
            
            print(f"📊 統計:")
            print(f"  - 成功頁面: {successful_pages}/{len(results)}")
            print(f"  - 總生成圖片: {total_generated}")
            
        else:
            print("❌ 生成失敗")
    
    elif choice == "2":
        # 生成單頁
        print("\n可用頁面:")
        for i, page_id in enumerate(generator.prompts.keys(), 1):
            print(f"{i}. {page_id}")
        
        try:
            page_choice = int(input("選擇頁面編號: ")) - 1
            page_ids = list(generator.prompts.keys())
            
            if 0 <= page_choice < len(page_ids):
                page_id = page_ids[page_choice]
                print(f"\n🚀 生成 {page_id}...")
                results = generator.generate_single_page(page_id)
                
                if results:
                    print(f"✅ 生成完成: {len(results)} 張圖片")
                    for result in results:
                        print(f"  - {result}")
                else:
                    print("❌ 生成失敗")
            else:
                print("❌ 無效選擇")
        
        except ValueError:
            print("❌ 請輸入有效數字")
    
    elif choice == "3":
        # 生成封面
        print("\n🚀 生成封面...")
        results = generator.generate_single_page("cover")
        
        if results:
            print(f"✅ 封面生成完成: {len(results)} 張圖片")
            for result in results:
                print(f"  - {result}")
        else:
            print("❌ 封面生成失敗")
    
    else:
        print("❌ 無效選擇")
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️ 生成已取消")
    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        import traceback
        traceback.print_exc()
