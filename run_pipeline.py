#!/usr/bin/env python3
"""
簡化的Pipeline運行腳本
自動檢查環境並運行生圖pipeline
"""

import sys
import subprocess
import os
from pathlib import Path

def check_and_install_requirements():
    """檢查並安裝必要的套件"""
    print("🔍 檢查Python套件...")
    
    required_packages = [
        "torch", "diffusers", "transformers", 
        "PIL", "tqdm", "accelerate"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == "PIL":
                import PIL
            else:
                __import__(package)
            print(f"✅ {package} 已安裝")
        except ImportError:
            print(f"❌ {package} 未安裝")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 需要安裝套件: {', '.join(missing_packages)}")
        
        install_choice = input("是否自動安裝？(y/n): ").strip().lower()
        if install_choice in ['y', 'yes', '是']:
            print("🔄 開始安裝套件...")
            
            # 安裝PyTorch
            try:
                subprocess.run([
                    sys.executable, "-m", "pip", "install", 
                    "torch", "torchvision", "torchaudio"
                ], check=True)
                print("✅ PyTorch 安裝完成")
            except subprocess.CalledProcessError:
                print("❌ PyTorch 安裝失敗")
                return False
            
            # 安裝其他套件
            try:
                subprocess.run([
                    sys.executable, "-m", "pip", "install",
                    "diffusers", "transformers", "accelerate",
                    "Pillow", "tqdm", "safetensors", "huggingface-hub"
                ], check=True)
                print("✅ 其他套件安裝完成")
            except subprocess.CalledProcessError:
                print("❌ 其他套件安裝失敗")
                return False
            
            print("🎉 所有套件安裝完成！")
            return True
        else:
            print("❌ 請手動安裝所需套件")
            return False
    
    return True

def run_pipeline():
    """運行生圖pipeline"""
    print("\n🚀 啟動生圖Pipeline...")
    
    try:
        # 導入並運行主程式
        from image_generation_pipeline import main
        return main()
    except ImportError as e:
        print(f"❌ 無法導入pipeline: {e}")
        print("請確保 image_generation_pipeline.py 存在")
        return False
    except Exception as e:
        print(f"❌ 運行失敗: {e}")
        return False

def main():
    """主函數"""
    print("🎨 《泡泡知道自己在哪裡》生圖Pipeline啟動器")
    print("=" * 60)
    
    # 檢查並安裝套件
    if not check_and_install_requirements():
        print("❌ 環境準備失敗")
        return False
    
    # 創建必要目錄
    Path("illustrations/generated").mkdir(parents=True, exist_ok=True)
    Path("models").mkdir(exist_ok=True)
    
    # 運行pipeline
    if run_pipeline():
        print("\n🎉 Pipeline運行完成！")
        print("📁 生成的圖片在: illustrations/generated/")
        return True
    else:
        print("\n❌ Pipeline運行失敗")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️ 已取消")
        sys.exit(1)
