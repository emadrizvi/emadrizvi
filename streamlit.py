# -*- coding: utf-8 -*-
"""streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BYI4Mj9YRyX_7qYBIcnR_edPsKPc7jJa
"""


# import yfinance as yf
# import streamlit as st
# import pandas as pd

st.write("""
#simple stock price app
""")
tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerdf=tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')
st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)

