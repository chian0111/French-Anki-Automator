# 📈 Portfolio Daily Report

每天自動寄送投資報告到你的信箱。

**包含：**
- 📊 Private Bank 風格 PDF 報告
- 🤖 AI 繁體中文市場摘要（由 Claude 生成）
- 📰 當日美股 / 台股新聞整合
- 🎯 目標達成進度追蹤

---

## 安裝需求

- macOS（Windows 版本開發中）
- Python 3.9 以上
- Gmail 帳號（需開啟兩步驟驗證）
- Anthropic API Key（免費申請，每月約 $1–3 用量）

---

## 安裝步驟（3 分鐘完成）

### 第一步：下載並解壓縮

將下載的 zip 解壓縮到任意資料夾。

### 第二步：執行安裝腳本

打開「終端機」（Terminal），輸入：

```bash
cd ~/Downloads/portfolio-system   # 換成你的解壓縮路徑
bash setup.sh
```

安裝精靈會引導你完成所有設定，包含：
- Gmail 帳號設定
- Anthropic API Key 設定
- 每日自動執行時間

### 第三步：填入你的持倉

安裝完成後，用文字編輯器打開 `~/Desktop/portfolio.json`：

```json
{
  "goal_twd": 3000000,
  "cash_twd": 0,
  "holdings": {
    "AAPL":    {"shares": 10,  "cost_usd": 150.0},
    "NVDA":    {"shares": 5,   "cost_usd": 420.0},
    "QQQ":     {"shares": 8,   "cost_usd": 380.0},
    "0050.TW": {"shares": 200, "cost_twd": 130.0},
    "2330.TW": {"shares": 10,  "cost_twd": 550.0}
  }
}
```

**美股格式：** `"代號": {"shares": 股數, "cost_usd": 平均成本(美金)}`  
**台股格式：** `"代號.TW": {"shares": 股數, "cost_twd": 平均成本(台幣)}`

---

## 取得 Gmail 應用程式密碼

1. 前往 [Google 帳號安全性設定](https://myaccount.google.com/security)
2. 開啟「兩步驟驗證」
3. 搜尋「應用程式密碼」→ 選擇「郵件」→ 產生
4. 複製 16 碼密碼填入安裝精靈

---

## 取得 Anthropic API Key

1. 前往 [console.anthropic.com](https://console.anthropic.com)
2. 註冊帳號（免費）
3. 點選「API Keys」→「Create Key」
4. 複製 key 填入安裝精靈

> 每月 AI 摘要費用約 $1–3 美金，視使用頻率而定。

---

## 報告範例

每天系統會自動：

1. 抓取最新股價（美股收盤後 / 台股收盤後）
2. 生成 PDF 報告（存到桌面）
3. 寄送 Email（含 PDF 附件 + HTML 摘要）

Email 內容包含：
- 總資產 / 損益 / 目標進度
- 今日市場新聞（美股大盤、台股、個股）
- Claude AI 市場分析摘要（繁體中文）

---

## 常見問題

**Q：我的持股資料安全嗎？**  
A：所有資料只存在你自己的電腦上，程式不會上傳任何資訊到外部伺服器。

**Q：支援哪些股票？**  
A：所有 Yahoo Finance 有資料的股票，包含美股、台股、ETF、部分加密貨幣。

**Q：Mac 關機的時候會跑嗎？**  
A：不會，launchd 排程需要電腦開機才會執行。建議在預計收盤時間前保持開機。

**Q：想改變發送時間怎麼辦？**  
A：編輯 `~/Library/LaunchAgents/com.portfolio.night.plist`，修改 `Hour` 和 `Minute` 的數值（使用 UTC 時間，台灣時間 -8）。

**Q：可以同時追蹤多個帳戶嗎？**  
A：目前版本所有持倉填在同一個 portfolio.json，視為單一組合。

---

## 手動執行

不想等排程，想立即產生報告：

```bash
python3 ~/Desktop/portfolio_system.py
```

---

## 技術支援

使用上有任何問題，歡迎來信：[你的信箱]

---

*資料來源：Yahoo Finance｜僅供參考，不構成投資建議*
