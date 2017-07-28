
#!usr/local/bin/python3

# Created 7/28/17 by ndeast

import requests
import time

from bs4 import BeautifulSoup
from datetime import datetime

fileID = "PLX OB"
filedate = datetime.now().strftime("%Y-%m-%d %H.%M")
filename = (fileID + " " + str(filedate) + ".txt")
btcStringList = []

# Settings ########
collections = 50
sleepTime = 5
amountToWrite = 3
###################

# Main function collects and writes data based on settings. 
def main():
    for i in range(collections):
        print("list length is: " + str(len(btcStringList)))
        collector()
        print(i)
        if len(btcStringList) == amountToWrite:
            writeToFile()
        time.sleep(sleepTime)

# Retrieves api request, parses html to string, and appends string to list
def collector():
    r = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=50")
    soup = BeautifulSoup(r.content, "html.parser")
    btcString = soup.text + ""
    btcStringList.append(btcString)

# Opens text file for appending, and writes each string in the btcStringList onto a new line in the file.
def writeToFile():
    print("writing to file")
    with open(filename, 'a') as f:
        for i in range(len(btcStringList)):
            f.write(btcStringList[i] + "\n")
    f.close()
    btcStringList.clear()

if __name__ == '__main__':
    main()
