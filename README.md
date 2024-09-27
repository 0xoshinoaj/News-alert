# 區塊鏈新聞爬蟲 [v1.2.1]

這個項目自動爬取多個區塊鏈新聞網站，並將新聞發送到 Discord 頻道。

## 首次使用說明

1. 安裝依賴
   確保您已安裝 Python 3.7 或更高版本，然後運行：
   ```
   pip install -r requirements.txt
   ```

2. 設置文件
   - 將 `config-SAMPLE.json` 重新命名為 `config.json`
   - 在 `config.json` 中填入您的 Discord webhook URL 和目標新聞網站資訊

3. 運行程序
   在命令行中運行：
   ```
   python main.py
   ```

4. 驗證
   檢查您的 Discord 頻道，確認新聞是否正確發送 (第一次會大量發送，可以先執行一次並中止後重新啟動)

## 如何新增網站

1. 更新 `config.json`
   在 `websites` 數組中添加新網站信息，例如：
   ```json
   {
     "name": "NewWebsite",
     "url": "https://www.newwebsite.com/news"
   }
   ```

2. 修改 `utils/data_processing.py`
   在 `extract_articles` 函數中添加新網站的解析邏輯：
   ```python
   elif source == 'NewWebsite':
       elements = soup.find_all('div', class_='article-title')  # 根據新網站的HTML結構調整
   ```

3. 測試