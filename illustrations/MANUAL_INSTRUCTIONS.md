# 手動生成說明

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
