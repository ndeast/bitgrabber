#!usr/local/bin/python3

import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

filename = "PLX OB"
filedate = datetime.now().strftime("%Y-%m-%d %H.%M")
collections = 50
sleepTime = 10

def collector():
    with open(/data/filename + " " + str(filedate) + ".txt", 'w') as f:
        r = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=50")
        soup = BeautifulSoup(r.content, "html.parser")
        btcString = soup.text
        f.write(btcString+"\n")
    f.close()

def main():
    for i in range(collections):
        collector()
        print(i)
        time.sleep(sleepTime)

if __name__ == '__main__':
    main()
