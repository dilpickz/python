"""
Dillon Ramsey
This is just some code I saw on TikTok and added to so that 
it had more real world functionality.
"""

import requests
import json
import time
import os

CRYPTO_LIST = ['ADA-USD', 'ETH-USD', 'BTC-USD']

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    while True:
        for currencyPair in CRYPTO_LIST:
            response = requests.get(f'https://api.coinbase.com/v2/prices/{currencyPair}/buy')
            data = response.json()
            coin, price = data['data']['base'], data['data']['amount']
            print(f"Current Price of {coin}: {price}")
        time.sleep(10)
        clearScreen()

if __name__=="__main__":
    main()