# 🎟️ Get Ticket Practicing 練習程式

這是一個基於 **Python + Selenium** 的練習用搶票腳本，專門針對  
[`https://ticket-training.onrender.com/`](https://ticket-training.onrender.com/) 練習網站，  
自動完成從倒數 → 點擊購票 → 選區域 → 選張數 → 填寫驗證碼 → 完成搶票的流程。  

---

## 📌 功能
- 自動啟動瀏覽器並打開指定練習網站
- 自動填入倒數時間並開始
- 自動點擊「購票」按鈕
- 自動選擇區域與票數
- 自動勾選同意條款
- 自動讀取驗證碼（使用 `data-answer` 屬性模擬）
- 自動送出表單並顯示搶票耗時與最佳紀錄
- 支援多次循環測試

---

## 🛠 環境需求
- Python 3.8+
- Google Chrome
- ChromeDriver（由 `webdriver_manager` 自動安裝）

---

## 📦 安裝
1. 下載專案程式碼
2. 安裝必要套件：
   ```bash
   pip install selenium webdriver-manager
