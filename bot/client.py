from binance.client import Client
from bot.config import settings

client = Client(
    settings.API_KEY,
    settings.API_SECRET,
    testnet=True
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"