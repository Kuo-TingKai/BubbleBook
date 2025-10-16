#!/bin/bash

# GitHub Pages 部署腳本
# 用於快速部署《泡泡知道自己在哪裡》童書網站

echo "🚀 開始部署《泡泡知道自己在哪裡》到 GitHub Pages"
echo "=" * 60

# 檢查是否已初始化git倉庫
if [ ! -d ".git" ]; then
    echo "📁 初始化Git倉庫..."
    git init
fi

# 檢查GitHub用戶名
echo "請輸入你的GitHub用戶名："
read -r GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ GitHub用戶名不能為空"
    exit 1
fi

# 更新README中的用戶名
echo "📝 更新README文件中的用戶名..."
sed -i '' "s/yourusername/$GITHUB_USERNAME/g" README.md
sed -i '' "s/yourusername/$GITHUB_USERNAME/g" index.html

echo "✅ 已更新用戶名為: $GITHUB_USERNAME"

# 添加所有文件
echo "📦 添加文件到Git..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "🎉 初始提交：《泡泡知道自己在哪裡》童書網站

✨ 特色功能：
- 互動式網頁版本
- AI生成的精美插圖
- 響應式設計
- 多格式支援 (HTML/PDF/LaTeX)
- 哲學啟蒙教育內容

📚 包含內容：
- 封面 + 9頁完整故事
- 對話泡泡互動效果
- 彩虹文字動畫
- 音效文字效果"

# 檢查是否已設置遠端倉庫
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 設置GitHub遠端倉庫..."
    git remote add origin "https://github.com/$GITHUB_USERNAME/baby_book.git"
fi

# 推送到GitHub
echo "📤 推送到GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "🎉 部署完成！"
echo "=" * 60
echo "📖 你的童書網站將在以下網址上線："
echo "   https://$GITHUB_USERNAME.github.io/baby_book"
echo ""
echo "📋 下一步："
echo "1. 訪問 https://github.com/$GITHUB_USERNAME/baby_book"
echo "2. 進入 Settings > Pages"
echo "3. 在 Source 下選擇 'Deploy from a branch'"
echo "4. 選擇 'main' 分支和 '/ (root)' 資料夾"
echo "5. 點擊 Save"
echo ""
echo "⏳ 等待幾分鐘後，你的網站就會上線！"
echo ""
echo "💡 提示："
echo "- 網站更新後，重新運行此腳本即可部署最新版本"
echo "- 可以在GitHub倉庫的Actions頁面查看部署狀態"
echo ""
echo "🎊 恭喜！你的《泡泡知道自己在哪裡》童書網站已經部署成功！"
