# News-alert# 區塊鏈新聞爬蟲

這個項目爬取多個區塊鏈新聞網站，並將新聞發送到 Discord。

## 安裝

1. 克隆此儲存庫
2. 安裝依賴：`pip install -r requirements.txt`
3. 在 `config.json` 中設置您的 Discord webhook URL

## 運行

執行 `python main.py`

## 添加新的新聞來源

1. 在 `scrapers/` 目錄下創建新的爬蟲文件
2. 在 `utils/data_processing.py` 中添加新的提取邏輯
3. 在 `main.py` 中導入並使用新的爬蟲