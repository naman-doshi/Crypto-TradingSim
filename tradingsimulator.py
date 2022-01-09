import yfinance as yf
import pandas as pd
import time
from binance.client import Client
from matplotlib import pyplot as plt
import scipy
from scipy import spatial
import math
import pyautogui as p
from multiprocessing import Process
import sys

api_key = ''
api_secret = ''
client = Client(api_key, api_secret)
capital = 600

print('Welcome to TradingSim v1.0!')
lposition = ''


while True:
    decision = input()
    decision = decision.split()
    command = decision[0]
    a = decision[1]

    if command == 'long':
        lposition = 'long'
        lev = input('Leverage? \n')
        pr = input('Percentage of Capital? \n')
        price = client.get_symbol_ticker(symbol=a)
        bprice = price['price']
        bprice = float(bprice)
        numberofassets = (int(lev)*(int(pr)/100)*capital)/bprice
        symbol = a
        print('Successfully bought ' + str(numberofassets) + ' ' + a + ' at the price of ' + str(bprice))

    if command == 'short':
        lposition = 'short'
        lev = input('Leverage? \n')
        pr = input('Percentage of Capital? \n')
        price = client.get_symbol_ticker(symbol=a)
        bprice = price['price']
        bprice = float(bprice)
        numberofassets = (int(lev)*(int(pr)/100)*capital)/bprice
        symbol = a
        print('Successfully shorted ' + str(numberofassets) + ' ' + a + ' at the price of ' + str(bprice))

    if command == 'check':
        if lposition == 'long':
            price = client.get_symbol_ticker(symbol=a)
            price = price['price']
            price = float(price)
            pnl = numberofassets*price - numberofassets*bprice
            print('PnL stands at ' + str(pnl))
            
        if lposition == 'short':
            price = client.get_symbol_ticker(symbol=a)
            price = price['price']
            price = float(price)
            pnl = numberofassets*bprice - numberofassets*price
            print('PnL stands at ' + str(pnl))

    if command == 'close':
        if lposition == 'long':
            price = client.get_symbol_ticker(symbol=a)
            price = price['price']
            price = float(price)
            pnl = numberofassets*price - numberofassets*bprice
            capital = pnl+capital-2
            print('Position closed. Balance now stands at ' + str(capital))
            
        if lposition == 'short':
            price = client.get_symbol_ticker(symbol=a)
            price = price['price']
            price = float(price)
            pnl = numberofassets*bprice - numberofassets*price
            capital = pnl+capital-2
            print('Position closed. Balance now stands at ' + str(capital))
            
'''    
def subpy():
    while True:
        if lposition == 'long':
                price = client.get_symbol_ticker(symbol=a)
                price = price['price']
                price = float(price)
                pnl = numberofassets*price - numberofassets*bprice

                
        if lposition == 'short':
            price = client.get_symbol_ticker(symbol=a)
            price = price['price']
            price = float(price)
            pnl = numberofassets*bprice - numberofassets*price

        if pnl*-1 > capital:
            print('You have been liquidated.')


if __name__ == '__main__':
    Process(target=mainpy).start()
    Process(target=subpy).start()
'''

    
    


