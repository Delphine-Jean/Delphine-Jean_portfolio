import logging
import requests
import pprint

logger = logging.getLogger()

def get_contracts():
    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    print(response_object.status_code)

    contracts= []

    for contract in response_object.json()["symbols"]:
        contracts.append(contract['pair'])
    return contracts

print(get_contracts())


"https://fapi.binance.com"
"https://testnet.binancefuture.com"
"wss://stream.binance.com:9443"

