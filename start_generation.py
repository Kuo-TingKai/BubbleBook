#!/usr/bin/env python3
"""
立即開始生成插圖腳本
"""

import webbrowser
import subprocess
import os
from pathlib import Path

def open_generation_services():
    """打開生圖服務網站"""
    services = [
        ("Playground AI", "https://playgroundai.com"),
        ("Leonardo.ai", "https://leonardo.ai"),
        ("Hugging Face Spaces", "https://huggingface.co/spaces")
    ]
    
    print("🌐 打開生圖服務網站...")
    for name, url in services:
        print(f"📱 正在打開 {name}...")
        webbrowser.open(url)

def show_first_prompt():
    """顯示第一個提示詞"""
    print("\n🎨 第一個提示詞（封面）：")
    print("=" * 60)
    print("A large transparent soap bubble floating in soft sky blue gradient background, rainbow prismatic edges, gentle watercolor illustration style, children's book cover, cute bubble with friendly expression, dreamy atmosphere, soft lighting, pastel colors, 20cm x 20cm square format")
    print("\n❌ 負面提示詞：")
    print("dark, scary, sharp edges, complex details, adult themes")

def create_generation_folders():
    """創建生成文件夾"""
    folders = [
        "illustrations/generated",
        "illustrations/selected", 
        "illustrations/backup"
    ]
    
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"✅ 創建文件夾: {folder}")

def show_instructions():
    """顯示操作說明"""
    print("\n📋 操作步驟：")
    print("1. 選擇一個生圖服務（推薦 Playground AI）")
    print("2. 註冊帳號（使用 Google 或 email）")
    print("3. 複製上面的提示詞")
    print("4. 設定參數：")
    print("   - Model: Playground v2.5")
    print("   - Dimensions: 1024x1024")
    print("   - Quality: Standard")
    print("5. 點擊 Generate")
    print("6. 下載結果到 illustrations/generated/ 文件夾")

def main():
    """主函數"""
    print("🚀 《泡泡知道自己在哪裡》插圖生成 - 立即開始！")
    print("=" * 60)
    
    # 創建文件夾
    create_generation_folders()
    
    # 顯示第一個提示詞
    show_first_prompt()
    
    # 顯示操作說明
    show_instructions()
    
    # 詢問是否打開網站
    choice = input("\n🌐 是否打開生圖服務網站？(y/n): ").strip().lower()
    if choice in ['y', 'yes', '是']:
        open_generation_services()
    
    print("\n🎉 準備完成！現在你可以開始生成插圖了！")
    print("📁 生成的圖片請保存到: illustrations/generated/ 文件夾")
    print("📖 詳細說明請查看: 立即開始指南.md")

if __name__ == "__main__":
    main()
