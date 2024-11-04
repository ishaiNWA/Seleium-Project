import os
from dotenv import load_dotenv
import requests

###############################################################################

# Load environment variables from .env file
load_dotenv()
# Bot configuration
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Ensure the token is set
if not BOT_TOKEN:
    raise ValueError("No bot token set.")

if not CHAT_ID:
    raise ValueError("No chat ID set.")

# Telegram API endpoint to send a message
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    'chat_id': CHAT_ID,
    'text': None
}

###############################################################################

def send_telegram_alarm(message):
    
    payload['text'] = message
    
        # Sending the request
    requests.post(URL, data=payload)

 
###############################################################################    
