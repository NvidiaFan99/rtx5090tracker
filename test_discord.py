import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

def send_test_message():
    msg = "✅ Test-Nachricht vom RTX 5090 Tracker läuft erfolgreich!"
    requests.post(WEBHOOK_URL, json={"content": msg})

send_test_message()
print("Test-Nachricht gesendet!")
