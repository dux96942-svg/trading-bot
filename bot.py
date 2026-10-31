import requests
import json
from datetime import datetime

# Token ufficiale del bot Telegram e tuo ID personale
TOKEN = "9188238206:AAHIks7soHy3EJqQ6g3QWaptd6X--sSV_ws"
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

def ottieni_partite_filtrate():
    """
    Funzione di elaborazione: qui inseriamo la logica di filtraggio 
    (Over 2.5 <= 1.60, esclusione amichevoli e giovanili, ordinamento per liquidità).
    Per adesso, simuliamo l'estrazione con i parametri richiesti per verificare il flusso.
    """
    # Esempio di struttura dati filtrata pronta per l'invio
    partite_esempio = [
        {"squadre": "Squadra A vs Squadra B", "quota": 1.52, "liquidita": "€ 45.000"},
        {"squadre": "Squadra C vs Squadra D", "quota": 1.58, "liquidita": "€ 38.500"},
        {"squadre": "Squadra E vs Squadra F", "quota": 1.45, "liquidita": "€ 31.200"}
    ]
    return partite_esempio

if __name__ == "__main__":
    oggi = datetime.now().strftime("%d/%m/%Y")
    partite = ottieni_partite_filtrate()
    
    # Costruiamo il messaggio formattato per Telegram
    testo = f"📊 *Report Trading Exchange - {oggi}*\n\n"
    testo += "🎯 *Filtri attivi:* Over 2.5 ≤ 1.60 (No Amichevoli/Giovanili)\n"
    testo += "🏆 *Top 3 partite per liquidità:*\n\n"
    
    for i, p in enumerate(partite, 1):
        testo += f"{i}️⃣ *{p['squadre']}*\n"
        testo += f"   • Quota Over 2.5: `{p['quota']}`\n"
        testo += f"   • Liquidità: `{p['liquidita']}`\n\n"
        
    risultato = send_message(testo)
    print("Risultato invio:", risultato)
