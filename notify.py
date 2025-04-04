import yfinance as yf
import requests

# === 获取汇率 ===
aud_to_cny = yf.Ticker("AUDCNY=X").info.get('regularMarketPrice')
aud_to_usd = yf.Ticker("AUDUSD=X").info.get('regularMarketPrice')
usd_to_cny = yf.Ticker("USDCNY=X").info.get('regularMarketPrice')

# === 构建推送内容 ===
title = "📈 实时汇率提醒"
body = (
    f"{aud_to_cny:.4f} | 澳币 -> 人民币\n"
    f"{aud_to_usd:.4f} | 澳币 -> 美元\n"
    f"{usd_to_cny:.4f} | 美元 -> 人民币"
)

# === 两个 Bark 设备地址（你可以加更多）
bark_urls = [
    "https://api.day.app/y7xVEauFG52S5uBxXyoktf",   # 设备 1
    "https://api.day.app/4TAKsQdSQmmXG6FrSRQtLW"    # 设备 2
]

# === 循环推送到所有设备
for url in bark_urls:
    requests.get(f"{url}/{title}/{body}")
    print(f"📲 推送成功：{url}")

print("✅ 所有设备汇率推送完成")
