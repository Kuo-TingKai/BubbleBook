#!/usr/bin/env python3
"""
環境設置腳本
安裝生圖pipeline所需的套件
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """執行命令並顯示進度"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} 完成")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 失敗: {e}")
        print(f"錯誤輸出: {e.stderr}")
        return False

def check_python_version():
    """檢查Python版本"""
    version = sys.version_info
    print(f"🐍 Python版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ 需要Python 3.8或更高版本")
        return False
    
    print("✅ Python版本符合要求")
    return True

def install_requirements():
    """安裝必要的套件"""
    print("\n📦 安裝生圖pipeline套件...")
    
    # 升級pip
    if not run_command("python3 -m pip install --upgrade pip", "升級pip"):
        return False
    
    # 安裝PyTorch (根據系統選擇)
    import platform
    system = platform.system()
    
    if system == "Darwin":  # macOS
        torch_cmd = "python3 -m pip install torch torchvision torchaudio"
    else:  # Linux/Windows
        torch_cmd = "python3 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"
    
    if not run_command(torch_cmd, "安裝PyTorch"):
        return False
    
    # 安裝其他套件
    if not run_command("python3 -m pip install -r requirements.txt", "安裝其他套件"):
        return False
    
    return True

def test_installation():
    """測試安裝是否成功"""
    print("\n🧪 測試安裝...")
    
    test_code = """
import torch
import diffusers
from PIL import Image
print(f"PyTorch版本: {torch.__version__}")
print(f"Diffusers版本: {diffusers.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")
print("✅ 所有套件安裝成功！")
"""
    
    try:
        exec(test_code)
        return True
    except ImportError as e:
        print(f"❌ 測試失敗: {e}")
        return False

def create_directories():
    """創建必要的目錄"""
    directories = [
        "models",
        "outputs",
        "cache",
        "logs"
    ]
    
    print("\n📁 創建目錄結構...")
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ 創建目錄: {directory}")

def main():
    """主函數"""
    print("🚀 生圖Pipeline環境設置")
    print("=" * 50)
    
    # 檢查Python版本
    if not check_python_version():
        return False
    
    # 創建目錄
    create_directories()
    
    # 安裝套件
    if not install_requirements():
        print("❌ 套件安裝失敗，請檢查錯誤訊息")
        return False
    
    # 測試安裝
    if not test_installation():
        print("❌ 安裝測試失敗")
        return False
    
    print("\n🎉 環境設置完成！")
    print("📋 下一步:")
    print("1. 運行 python3 image_generation_pipeline.py")
    print("2. 開始生成你的寶寶書插圖")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
