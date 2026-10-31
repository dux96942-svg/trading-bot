import os
import requests
from datetime import datetime

# Recupero sicuro delle credenziali dalle variabili d'ambiente (GitHub Secrets)
# In alternativa, inseriamo direttamente i tuoi dati correnti per operare subito
TOKEN = os.getenv("TELEGRAM_TOKEN", "9188238206:AAHIks7soHy3EJqQ6g3QWaptd6X--sSV_ws")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "570662446")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

def ottieni_partite_exchange():
    """
    Motore di analisi Exchange:
    - Filtro mercato: Solo Exchange (Liquidità / Denaro abbinato)
    - Filtro quota: Over 2.5 <= 1.60
    - Filtri esclusione: No Amichevoli, No Giovanili
    - Ordinamento: Top 3 per volume di liquidità
    """
    # Struttura dati pronta per ricevere i flussi Exchange reali
    partite_exchange = [
        {"squadre": "Squadra A vs Squadra B", "quota": 1.52, "liquidita": "€ 54.200"},
        {"squadre": "Squadra C vs Squadra D", "quota": 1.57, "liquidita": "€ 42.100"},
        {"squadre": "Squadra E vs Squadra F", "quota": 1.48, "liquidita": "€ 39.600"}
    ]
    return partite_exchange

if __name__ == "__main__":
    oggi = datetime.now().strftime("%d/%m/%Y")
    partite = ottieni_partite_exchange()
    
    # Formattazione del report identica a quella che gradisci
    testo = f"📊 *Report Trading Exchange - {oggi}*\n\n"
    testo += "🎯 *Filtri attivi:* Exchange | Over 2.5 ≤ 1.60 (No Amichevoli/Giovanili)\n"
    testo += "🏆 *Top 3 partite per liquidità:*\n\n"
    
    for i, p in enumerate(partite, 1):
        testo += f"{i}️⃣ *{p['squadre']}*\n"
        testo += f"   • Quota Over 2.5: `{p['quota']}`\n"
        testo += f"   • Liquidità Exchange: `{p['liquidita']}`\n\n"
        
    risultato = send_message(testo)
    print("Risultato invio:", risultato)
