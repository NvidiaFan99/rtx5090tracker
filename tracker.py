import requests
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

URLS = {
    "NVIDIA_DE": "https://store.nvidia.com/store/nvidia/de_DE/Content/pbPage.SKUList/productID.123456700",
    "BestBuy": "https://www.bestbuy.com/site/nvidia-geforce-rtx-5090-founders-edition/yourSkuID.p",
    "ScanUK": "https://www.scan.co.uk/products/nvidia-geforce-rtx-5090-founders-edition"
}

def send(msg):
    requests.post(WEBHOOK_URL, json={"content": msg})

def check_stock(url):
    try:
        html = requests.get(url, timeout=8).text.lower()
        keywords = ["in stock", "add to cart", "add to basket", "available", "in den warenkorb"]
        return any(k in html for k in keywords)
    except:
        return False

for shop, url in URLS.items():
    if check_stock(url):
        send(f"🚨 **RESTOCK! RTX 5090 FE verfügbar bei {shop}**\n{url}")
