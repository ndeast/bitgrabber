#!usr/local/bin/python3

import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

fileID = "PLX OB"
filedate = datetime.now().strftime("%Y-%m-%d %H.%M")
filename = (fileID + " " + str(filedate) + ".txt")
collections = 50
sleepTime = 5
amountToWrite = 3

btcStringList = []

def collector():
    r = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=50")
    soup = BeautifulSoup(r.content, "html.parser")
    btcString = soup.text
    btcStringList.append(btcString)

def main():
    for i in range(collections):
        collector()
        print(i)
        if len(btcStringList) % amountToWrite:
            writeToFile()
        time.sleep(sleepTime)

def writeToFile():
    with open(filename, 'w') as f:
        for i in range(len(btcStringList)):
            f.write(btcStringList[i] + "\n")
    f.close()

if __name__ == '__main__':
    main()
