import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

balance = client.futures_account_balance()
print("Your Futures Balance:")
for asset in balance:
    print(f"{asset['asset']}: {asset['balance']}")
