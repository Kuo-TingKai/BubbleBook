#!/usr/bin/env python3
"""
生成PDF版本的童書
使用ReportLab創建專業的童書排版
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
import os
from pathlib import Path

class ChildrenBookGenerator:
    """兒童書籍PDF生成器"""
    
    def __init__(self, output_path="泡泡知道自己在哪裡.pdf"):
        """初始化生成器"""
        self.output_path = output_path
        self.page_size = (20*cm, 20*cm)  # 20cm x 20cm 正方形
        self.margin = 1.5*cm
        
        # 設置顏色
        self.bubble_blue = colors.HexColor('#1976D2')
        self.bubble_bg = colors.HexColor('#E3F2FD')
        self.orange = colors.HexColor('#FF9800')
        
        # 創建樣式
        self.setup_styles()
        
        # 頁面內容
        self.pages = [
            {
                "type": "cover",
                "image": "Cover.png",
                "title": "泡泡知道自己在哪裡",
                "subtitle": "寶寶的範疇思維書",
                "author": "作者：郭庭愷",
                "year": "2025年"
            },
            {
                "type": "content",
                "image": "Page1.png",
                "texts": [
                    {"type": "sound", "content": "噗噗噗..."},
                    {"type": "normal", "content": "泡泡從泡泡機裡飛出來"},
                    {"type": "normal", "content": "圓圓的、透明的"},
                    {"type": "speech", "content": "泡泡知道自己是泡泡"}
                ]
            },
            {
                "type": "content",
                "image": "Page2.png",
                "texts": [
                    {"type": "normal", "content": "泡泡在鏡子前"},
                    {"type": "normal", "content": "看到另一個泡泡"},
                    {"type": "speech", "content": "那是誰？"},
                    {"type": "speech", "content": "是我！"}
                ]
            },
            {
                "type": "content",
                "image": "Page3.png",
                "texts": [
                    {"type": "normal", "content": "泡泡裡有彩虹"},
                    {"type": "normal", "content": "泡泡外有風"},
                    {"type": "normal", "content": "泡泡知道："},
                    {"type": "speech", "content": "我在裡面，世界在外面"}
                ]
            },
            {
                "type": "content",
                "image": "Page4.png",
                "texts": [
                    {"type": "sound", "content": "呼呼呼..."},
                    {"type": "normal", "content": "泡泡越來越大"},
                    {"type": "normal", "content": "邊界越來越薄"},
                    {"type": "normal", "content": "快要...快要..."}
                ]
            },
            {
                "type": "content",
                "image": "Page5.png",
                "texts": [
                    {"type": "sound", "content": "啪！"},
                    {"type": "normal", "content": "泡泡不見了"},
                    {"type": "normal", "content": "彩虹飛散了"},
                    {"type": "normal", "content": "風吹進來了"}
                ]
            },
            {
                "type": "content",
                "image": "Page6.png",
                "texts": [
                    {"type": "sound", "content": "噗噗噗..."},
                    {"type": "normal", "content": "又一個泡泡飛出來"},
                    {"type": "normal", "content": "圓圓的、透明的"},
                    {"type": "speech", "content": "我又是泡泡了！"}
                ]
            },
            {
                "type": "content",
                "image": "Page7.png",
                "texts": [
                    {"type": "normal", "content": "好多泡泡！"},
                    {"type": "normal", "content": "每個泡泡都有自己的彩虹"},
                    {"type": "normal", "content": "每個泡泡都有自己的邊界"},
                    {"type": "normal", "content": "每個泡泡都知道自己在哪裡"}
                ]
            },
            {
                "type": "content",
                "image": "Page8.png",
                "texts": [
                    {"type": "normal", "content": "兩個泡泡輕輕碰在一起"},
                    {"type": "normal", "content": "邊界變模糊了"},
                    {"type": "speech", "content": "我們是一起的嗎？"},
                    {"type": "speech", "content": "我們還是分開的嗎？"}
                ]
            },
            {
                "type": "content",
                "image": "Page9.png",
                "texts": [
                    {"type": "normal", "content": "變成一個大泡泡！"},
                    {"type": "normal", "content": "彩虹混合了"},
                    {"type": "normal", "content": "邊界重新畫了"},
                    {"type": "speech", "content": "我們現在是一體的"}
                ]
            }
        ]
    
    def setup_styles(self):
        """設置文字樣式"""
        self.styles = getSampleStyleSheet()
        
        # 標題樣式
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=48,
            textColor=self.bubble_blue,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            spaceAfter=20
        )
        
        # 副標題樣式
        self.subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=24,
            textColor=self.bubble_blue,
            alignment=TA_CENTER,
            fontName='Helvetica',
            spaceAfter=30
        )
        
        # 普通文字樣式
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=24,
            textColor=self.bubble_blue,
            alignment=TA_CENTER,
            fontName='Helvetica',
            spaceAfter=15
        )
        
        # 音效文字樣式
        self.sound_style = ParagraphStyle(
            'CustomSound',
            parent=self.styles['Normal'],
            fontSize=32,
            textColor=self.orange,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            spaceAfter=20
        )
        
        # 對話泡泡樣式
        self.speech_style = ParagraphStyle(
            'CustomSpeech',
            parent=self.styles['Normal'],
            fontSize=22,
            textColor=self.bubble_blue,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            spaceAfter=15,
            backColor=self.bubble_bg,
            borderColor=self.bubble_blue,
            borderWidth=2,
            borderPadding=10
        )
        
        # 作者信息樣式
        self.author_style = ParagraphStyle(
            'CustomAuthor',
            parent=self.styles['Normal'],
            fontSize=18,
            textColor=self.bubble_blue,
            alignment=TA_CENTER,
            fontName='Helvetica',
            spaceAfter=10
        )
    
    def resize_image(self, image_path, max_width, max_height):
        """調整圖片大小"""
        if not os.path.exists(image_path):
            print(f"警告：圖片文件不存在 {image_path}")
            return None
        
        try:
            # 使用PIL調整圖片大小
            with PILImage.open(image_path) as img:
                # 計算縮放比例
                width_ratio = max_width / img.width
                height_ratio = max_height / img.height
                ratio = min(width_ratio, height_ratio)
                
                new_width = int(img.width * ratio)
                new_height = int(img.height * ratio)
                
                # 調整大小
                resized_img = img.resize((new_width, new_height), PILImage.Resampling.LANCZOS)
                
                # 保存臨時文件
                temp_path = f"temp_{os.path.basename(image_path)}"
                resized_img.save(temp_path)
                
                return temp_path
        except Exception as e:
            print(f"錯誤：無法處理圖片 {image_path}: {e}")
            return None
    
    def create_cover_page(self, story, canvas, doc):
        """創建封面頁"""
        # 添加背景色
        canvas.setFillColor(self.bubble_bg)
        canvas.rect(0, 0, self.page_size[0], self.page_size[1], fill=1)
        
        # 添加封面圖片
        if os.path.exists(story["image"]):
            img_path = self.resize_image(story["image"], 12*cm, 12*cm)
            if img_path:
                img = Image(img_path, width=12*cm, height=12*cm)
                img.drawOn(canvas, 4*cm, 10*cm)
                # 清理臨時文件
                os.remove(img_path)
        
        # 添加標題
        title = Paragraph(story["title"], self.title_style)
        title.wrap(16*cm, 2*cm)
        title.drawOn(canvas, 2*cm, 8*cm)
        
        # 添加副標題
        subtitle = Paragraph(story["subtitle"], self.subtitle_style)
        subtitle.wrap(16*cm, 1*cm)
        subtitle.drawOn(canvas, 2*cm, 7*cm)
        
        # 添加作者信息
        author = Paragraph(story["author"], self.author_style)
        author.wrap(16*cm, 1*cm)
        author.drawOn(canvas, 2*cm, 5.5*cm)
        
        # 添加年份
        year = Paragraph(story["year"], self.author_style)
        year.wrap(16*cm, 1*cm)
        year.drawOn(canvas, 2*cm, 5*cm)
    
    def create_content_page(self, story, canvas, doc):
        """創建內容頁"""
        # 添加背景色
        canvas.setFillColor(colors.white)
        canvas.rect(0, 0, self.page_size[0], self.page_size[1], fill=1)
        
        # 添加頁面圖片
        if os.path.exists(story["image"]):
            img_path = self.resize_image(story["image"], 14*cm, 14*cm)
            if img_path:
                img = Image(img_path, width=14*cm, height=14*cm)
                img.drawOn(canvas, 3*cm, 7.5*cm)
                # 清理臨時文件
                os.remove(img_path)
        
        # 添加文字內容
        y_position = 5*cm
        for text_item in story["texts"]:
            if text_item["type"] == "sound":
                para = Paragraph(text_item["content"], self.sound_style)
                para.wrap(15*cm, 1*cm)
                para.drawOn(canvas, 2.5*cm, y_position)
                y_position -= 0.8*cm
            elif text_item["type"] == "speech":
                para = Paragraph(f"「{text_item['content']}」", self.speech_style)
                para.wrap(15*cm, 1*cm)
                para.drawOn(canvas, 2.5*cm, y_position)
                y_position -= 1*cm
            else:  # normal
                para = Paragraph(text_item["content"], self.normal_style)
                para.wrap(15*cm, 1*cm)
                para.drawOn(canvas, 2.5*cm, y_position)
                y_position -= 0.6*cm
    
    def generate_pdf(self):
        """生成PDF文件"""
        print("🎨 開始生成PDF童書...")
        
        # 創建PDF文檔
        doc = SimpleDocTemplate(
            self.output_path,
            pagesize=self.page_size,
            rightMargin=self.margin,
            leftMargin=self.margin,
            topMargin=self.margin,
            bottomMargin=self.margin
        )
        
        # 構建內容
        story = []
        
        for i, page in enumerate(self.pages):
            if i > 0:
                story.append(PageBreak())
            
            if page["type"] == "cover":
                # 封面頁需要特殊處理
                pass  # 將在canvas中處理
            else:
                # 內容頁
                pass  # 將在canvas中處理
        
        # 自定義頁面模板
        def first_page(canvas, doc):
            self.create_cover_page(self.pages[0], canvas, doc)
        
        def content_pages(canvas, doc):
            page_num = canvas.getPageNumber()
            if page_num <= len(self.pages):
                page_data = self.pages[page_num - 1]
                if page_data["type"] == "content":
                    self.create_content_page(page_data, canvas, doc)
        
        # 構建PDF
        doc.build(story, onFirstPage=first_page, onLaterPages=content_pages)
        
        print(f"✅ PDF生成完成：{self.output_path}")
        return True

def main():
    """主函數"""
    print("📚 《泡泡知道自己在哪裡》PDF童書生成器")
    print("=" * 50)
    
    # 檢查圖片文件
    required_images = [
        "Cover.png", "Page1.png", "Page2.png", "Page3.png", 
        "Page4.png", "Page5.png", "Page6.png", "Page7.png", 
        "Page8.png", "Page9.png"
    ]
    
    missing_images = []
    for img in required_images:
        if not os.path.exists(img):
            missing_images.append(img)
    
    if missing_images:
        print(f"❌ 缺少圖片文件：{', '.join(missing_images)}")
        print("請確保所有圖片文件都在當前目錄中")
        return False
    
    print("✅ 所有圖片文件檢查完成")
    
    # 生成PDF
    generator = ChildrenBookGenerator()
    success = generator.generate_pdf()
    
    if success:
        print("\n🎉 童書生成完成！")
        print(f"📁 文件位置：{generator.output_path}")
        print("📖 你可以使用PDF閱讀器查看你的童書")
    else:
        print("\n❌ 生成失敗")
    
    return success

if __name__ == "__main__":
    try:
        success = main()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️ 生成已取消")
        exit(1)
    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
