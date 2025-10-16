#!/usr/bin/env python3
"""
提示詞測試工具
用於快速測試和優化插圖生成提示詞
"""

import json
from pathlib import Path

def load_illustrations():
    """載入插圖配置"""
    config_path = Path("/Users/kevin.k/baby_book/illustrations/generation_config.json")
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config['illustrations']
    return {}

def format_prompt(page_id, prompt_data, style_tags=None):
    """格式化提示詞"""
    if style_tags is None:
        style_tags = [
            "children's book illustration",
            "soft watercolor", 
            "gentle colors",
            "pastel colors",
            "dreamy atmosphere"
        ]
    
    main_prompt = prompt_data['prompt']
    negative_prompt = prompt_data['negative']
    style_text = ", ".join(style_tags)
    
    return {
        "positive": f"{main_prompt}, {style_text}",
        "negative": negative_prompt,
        "page_id": page_id
    }

def generate_test_prompts():
    """生成測試用的提示詞"""
    illustrations = load_illustrations()
    
    if not illustrations:
        print("❌ 無法載入插圖配置")
        return
    
    print("🎨 《泡泡知道自己在哪裡》提示詞測試工具")
    print("=" * 60)
    
    # 生成所有頁面的提示詞
    for page_id, prompt_data in illustrations.items():
        formatted = format_prompt(page_id, prompt_data)
        
        print(f"\n📖 {page_id.upper()}")
        print("-" * 40)
        print(f"✅ 正面提示詞:")
        print(f"   {formatted['positive']}")
        print(f"\n❌ 負面提示詞:")
        print(f"   {formatted['negative']}")
        print(f"\n📋 複製用格式:")
        print(f"   {formatted['positive']} | {formatted['negative']}")

def interactive_prompt_builder():
    """互動式提示詞建構器"""
    print("\n🔧 互動式提示詞建構器")
    print("=" * 40)
    
    # 基本元素
    elements = {
        "主角": ["transparent soap bubble", "cute bubble with expression"],
        "動作": ["floating", "flying", "expanding", "bursting", "merging"],
        "背景": ["soft sky blue background", "pure white background", "gradient background"],
        "風格": ["watercolor illustration", "children's book style", "gentle colors"],
        "氛圍": ["dreamy atmosphere", "peaceful", "playful", "hopeful"]
    }
    
    print("選擇元素組合:")
    for category, options in elements.items():
        print(f"\n{category}:")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
    
    print("\n💡 提示：可以組合多個元素來創建新的提示詞")

def save_custom_prompts():
    """保存自定義提示詞"""
    custom_prompts = {}
    
    print("\n✍️ 自定義提示詞編輯器")
    print("=" * 40)
    
    pages = [
        "cover", "page_01_birth", "page_02_mirror", "page_03_world",
        "page_04_expanding", "page_05_burst", "page_06_new_bubble",
        "page_07_friends", "page_08_hug", "page_09_merge",
        "page_10_thinking", "page_11_understanding", "page_12_continuing"
    ]
    
    for page in pages:
        print(f"\n📝 編輯 {page}:")
        positive = input("正面提示詞: ")
        negative = input("負面提示詞: ")
        
        if positive and negative:
            custom_prompts[page] = {
                "prompt": positive,
                "negative": negative
            }
    
    # 保存自定義提示詞
    output_path = Path("/Users/kevin.k/baby_book/自定義提示詞.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(custom_prompts, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 自定義提示詞已保存到: {output_path}")

def main():
    """主函數"""
    while True:
        print("\n🎨 提示詞測試工具選單")
        print("=" * 30)
        print("1. 顯示所有提示詞")
        print("2. 互動式提示詞建構器")
        print("3. 編輯自定義提示詞")
        print("4. 生成快速複製格式")
        print("5. 退出")
        
        choice = input("\n請選擇 (1-5): ").strip()
        
        if choice == "1":
            generate_test_prompts()
        elif choice == "2":
            interactive_prompt_builder()
        elif choice == "3":
            save_custom_prompts()
        elif choice == "4":
            generate_copy_format()
        elif choice == "5":
            print("👋 再見！")
            break
        else:
            print("❌ 無效選擇，請重試")

def generate_copy_format():
    """生成快速複製格式"""
    illustrations = load_illustrations()
    
    if not illustrations:
        print("❌ 無法載入插圖配置")
        return
    
    print("\n📋 快速複製格式")
    print("=" * 40)
    
    for page_id, prompt_data in illustrations.items():
        formatted = format_prompt(page_id, prompt_data)
        print(f"\n{page_id}:")
        print(f"Positive: {formatted['positive']}")
        print(f"Negative: {formatted['negative']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
