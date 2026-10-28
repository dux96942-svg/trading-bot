import requests
import time

# Il tuo Token Telegram ufficiale
TOKEN = "9188238206:AAHIks7soHy3EJqQ6g3QWaptd6X--sSV_ws"
CHAT_ID = None  # Si collegherà automaticamente al primo che scrive al bot

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        response = requests.get(url)
        return response.json()
    except:
        return None

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

print("Bot avviato e in attesa di connessione...")
