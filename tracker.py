import requests
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

NVIDIA_API = "https://api.store.nvidia.com/partner/v1/widget/gpu?category=GPU&gpu=5090&locale=de-de"

def send(msg):
    requests.post(WEBHOOK_URL, json={"content": msg})

def check_nvidia():
    try:
        data = requests.get(NVIDIA_API, timeout=8).json()
        for item in data.get("List", []):
            if item.get("isForSale"):
                return item.get("productURL")
        return None
    except:
        return None

url = check_nvidia()

if url:
    send(f"🚨 **RTX 5090 Founders Edition verfügbar!**\n{url}")
