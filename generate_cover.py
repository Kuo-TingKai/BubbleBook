#!/usr/bin/env python3
"""
自動生成封面插圖腳本
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from image_generation_pipeline import BubbleBookGenerator

def main():
    """生成封面"""
    print("🎨 生成《泡泡知道自己在哪裡》封面插圖")
    print("=" * 50)
    
    # 創建生成器
    generator = BubbleBookGenerator()
    
    # 載入模型
    print("📥 載入模型...")
    if not generator.load_model():
        print("❌ 模型載入失敗")
        return False
    
    # 生成封面
    print("🚀 開始生成封面...")
    results = generator.generate_single_page("cover", num_variations=3)
    
    if results:
        print(f"\n🎉 封面生成完成！")
        print(f"📊 生成了 {len(results)} 張封面圖片:")
        for i, result in enumerate(results, 1):
            print(f"  {i}. {result}")
        
        print(f"\n📁 圖片保存在: illustrations/generated/")
        print("💡 你可以選擇最喜歡的一張作為最終封面")
        
        return True
    else:
        print("❌ 封面生成失敗")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️ 生成已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        import traceback
        traceback.print_exc()
