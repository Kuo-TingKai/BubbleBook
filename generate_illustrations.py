#!/usr/bin/env python3
"""
《泡泡知道自己在哪裡》插圖生成腳本
使用 Stable Diffusion 生成兒童書籍插圖
"""

import os
import json
from pathlib import Path

# 插圖提示詞配置
ILLUSTRATIONS = {
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

# 通用生成參數
GENERATION_CONFIG = {
    "width": 1024,
    "height": 1024,
    "steps": 50,
    "cfg_scale": 7.5,
    "sampler": "euler_a",
    "batch_size": 1,
    "seed": -1  # 隨機種子
}

def create_directories():
    """創建插圖文件夾結構"""
    base_dir = Path("/Users/kevin.k/baby_book/illustrations")
    directories = [
        base_dir / "cover",
        base_dir / "pages", 
        base_dir / "raw",
        base_dir / "processed"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ 創建目錄: {directory}")
    
    return base_dir

def save_generation_config(base_dir):
    """保存生成配置到JSON文件"""
    config = {
        "generation_config": GENERATION_CONFIG,
        "illustrations": ILLUSTRATIONS,
        "model_recommendations": [
            "dreamshaper_8.safetensors",
            "deliberate_v2.safetensors", 
            "anything-v5.0.safetensors",
            "realisticVisionV60B1_v60B1VAE.safetensors"
        ],
        "style_tags": [
            "children's book illustration",
            "soft watercolor", 
            "gentle colors",
            "pastel colors",
            "dreamy atmosphere"
        ]
    }
    
    config_path = base_dir / "generation_config.json"
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 保存配置: {config_path}")

def create_batch_script(base_dir):
    """創建批量生成腳本"""
    
    # AUTOMATIC1111 WebUI 批量腳本
    auto1111_script = f"""#!/bin/bash
# AUTOMATIC1111 WebUI 批量生成腳本

MODEL="dreamshaper_8.safetensors"
OUTPUT_DIR="{base_dir}/raw"
STYLE_TAGS="children's book illustration, soft watercolor, gentle colors, pastel colors"

echo "開始生成《泡泡知道自己在哪裡》插圖..."

"""
    
    for page_id, config in ILLUSTRATIONS.items():
        output_file = f"{page_id}.png"
        auto1111_script += f"""
# 生成 {page_id}
echo "正在生成 {page_id}..."
python scripts/txt2img.py \\
    --prompt "{config['prompt']}, $STYLE_TAGS" \\
    --negative_prompt "{config['negative']}" \\
    --width {GENERATION_CONFIG['width']} \\
    --height {GENERATION_CONFIG['height']} \\
    --steps {GENERATION_CONFIG['steps']} \\
    --cfg_scale {GENERATION_CONFIG['cfg_scale']} \\
    --sampler_name {GENERATION_CONFIG['sampler']} \\
    --batch_size {GENERATION_CONFIG['batch_size']} \\
    --output_dir "$OUTPUT_DIR" \\
    --filename "{output_file}"

"""
    
    auto1111_script += """
echo "所有插圖生成完成！"
echo "請檢查 $OUTPUT_DIR 目錄中的結果"
"""
    
    script_path = base_dir / "generate_auto1111.sh"
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(auto1111_script)
    
    os.chmod(script_path, 0o755)
    print(f"✅ 創建 AUTOMATIC1111 腳本: {script_path}")
    
    # ComfyUI 工作流程
    comfyui_workflow = {
        "1": {
            "inputs": {
                "ckpt_name": "dreamshaper_8.safetensors"
            },
            "class_type": "CheckpointLoaderSimple",
            "_meta": {
                "title": "Load Checkpoint"
            }
        },
        "2": {
            "inputs": {
                "text": "{prompt}",
                "clip": ["1", 1]
            },
            "class_type": "CLIPTextEncode",
            "_meta": {
                "title": "CLIP Text Encode (Prompt)"
            }
        },
        "3": {
            "inputs": {
                "text": "{negative}",
                "clip": ["1", 1]
            },
            "class_type": "CLIPTextEncode", 
            "_meta": {
                "title": "CLIP Text Encode (Negative)"
            }
        },
        "4": {
            "inputs": {
                "seed": -1,
                "steps": 50,
                "cfg": 7.5,
                "sampler_name": "euler_a",
                "scheduler": "normal",
                "denoise": 1.0,
                "model": ["1", 0],
                "positive": ["2", 0],
                "negative": ["3", 0],
                "latent_image": ["5", 0]
            },
            "class_type": "KSampler",
            "_meta": {
                "title": "KSampler"
            }
        },
        "5": {
            "inputs": {
                "width": 1024,
                "height": 1024,
                "batch_size": 1
            },
            "class_type": "EmptyLatentImage",
            "_meta": {
                "title": "Empty Latent Image"
            }
        },
        "6": {
            "inputs": {
                "samples": ["4", 0],
                "vae": ["1", 2]
            },
            "class_type": "VAEDecode",
            "_meta": {
                "title": "VAE Decode"
            }
        },
        "7": {
            "inputs": {
                "filename_prefix": "{page_id}",
                "images": ["6", 0]
            },
            "class_type": "SaveImage",
            "_meta": {
                "title": "Save Image"
            }
        }
    }
    
    comfyui_path = base_dir / "comfyui_workflow.json"
    with open(comfyui_path, 'w', encoding='utf-8') as f:
        json.dump(comfyui_workflow, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 創建 ComfyUI 工作流程: {comfyui_path}")

def create_manual_instructions(base_dir):
    """創建手動生成說明"""
    instructions = """# 手動生成說明

## 使用 AUTOMATIC1111 WebUI

1. 啟動 WebUI:
   ```bash
   cd /path/to/stable-diffusion-webui
   ./webui.sh
   ```

2. 在瀏覽器中打開 http://localhost:7860

3. 選擇模型: dreamshaper_8.safetensors (推薦)

4. 設定參數:
   - Width: 1024
   - Height: 1024  
   - Steps: 50
   - CFG Scale: 7.5
   - Sampler: Euler a
   - Batch size: 1

5. 逐頁輸入提示詞 (見 generation_config.json)

## 使用 ComfyUI

1. 啟動 ComfyUI:
   ```bash
   cd /path/to/ComfyUI
   python main.py
   ```

2. 導入工作流程: comfyui_workflow.json

3. 修改提示詞節點

## 後製建議

1. 使用 GIMP 或 Photoshop 調整色彩
2. 確保一致的色彩方案
3. 加強彩虹透明度效果
4. 為文字預留空間

## 品質檢查清單

- [ ] 泡泡透明效果正確
- [ ] 色彩符合兒童友好標準  
- [ ] 構圖平衡且有趣
- [ ] 與其他頁面視覺一致
- [ ] 適合印刷品質 (300 DPI)
"""
    
    instructions_path = base_dir / "MANUAL_INSTRUCTIONS.md"
    with open(instructions_path, 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print(f"✅ 創建手動說明: {instructions_path}")

def main():
    """主函數"""
    print("🎨 《泡泡知道自己在哪裡》插圖生成準備")
    print("=" * 50)
    
    # 創建目錄結構
    base_dir = create_directories()
    
    # 保存配置
    save_generation_config(base_dir)
    
    # 創建腳本
    create_batch_script(base_dir)
    
    # 創建手動說明
    create_manual_instructions(base_dir)
    
    print("\n🎉 插圖生成準備完成！")
    print(f"📁 所有文件已保存到: {base_dir}")
    print("\n📋 下一步:")
    print("1. 選擇你的 Stable Diffusion 環境")
    print("2. 運行對應的生成腳本")
    print("3. 檢查生成的插圖品質")
    print("4. 進行必要的後製調整")
    
    print(f"\n📖 詳細說明請查看: {base_dir}/MANUAL_INSTRUCTIONS.md")

if __name__ == "__main__":
    main()
