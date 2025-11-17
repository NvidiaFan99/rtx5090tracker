import requests
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

# Nur NVIDIA Deutschland
NVIDIA_API = "https://api.store.nvidia.com/partner/v1/widget/gpu?category=GPU&gpu=5090&locale=de-de"

def send(msg):
    # @everyone für den Ping
    requests.post(WEBHOOK_URL, json={"content": f"@everyone {msg}"} )

def check_nvidia():
    try:
        data = requests.get(NVIDIA_API, timeout=8).json()
        for item in data.get("List", []):
            if item.get("isForSale"):
                return item.get("productURL")
        return None
    except Exception as e:
        print("Fehler beim Abrufen der API:", e)
        return None

url = check_nvidia()

if url:
    send(f"🚨 **RTX 5090 Founders Edition verfügbar!**\n{url}")
    print("Restock gefunden! Nachricht gesendet.")
else:
    print("Kein Restock aktuell.")
