import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")
print(stock)

startyear=2022
startmonth=1
startday=1

start=dt.datetime(startyear,startmonth,startday)
now=dt.datetime.now()
df=pdr.get_data_yahoo(stock,start,now)

#Moving Average
MA=50
SMA_String="SMA_"+str(MA)
df[SMA_String]=df.iloc[:,4].rolling(window=MA).mean()

countHigher=0
countLower=0

Comparison="Comparison"
for i in df.index:
    if(df["Adj Close"][i]>df[SMA_String][i]):
        df[Comparison]="Close > MA"
        countHigher+=1
    else:
        df[Comparison]="Close < MA"
        countLower+=1
print(df)
print(str(countHigher))
print(str(countLower))