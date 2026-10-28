import requests

# Token ufficiale del bot Telegram
TOKEN = "9188238206:AAHIks7soHy3EJqQ6g3QWaptd6X--sSV_ws"
# Il tuo ID Telegram personale
CHAT_ID = "570662446"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    messaggio = (
        "🤖 *Bot Trading Exchange Avviato!*\n\n"
        "Ciao Francesco! Il collegamento è riuscito alla perfezione. "
        "Da questo momento il bot è pronto per inviarti le 3 migliori partite del giorno."
    )
    risultato = send_message(messaggio)
    print("Risultato invio:", risultato)
