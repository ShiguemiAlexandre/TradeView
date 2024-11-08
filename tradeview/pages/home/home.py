import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta

lista_ativos = []
# msft = yf.Ticker(["AAPL", "BRK.B", "GOOGL", "INTC", "MSFT"])
ativo = "AAPL"
msft = yf.Ticker(ativo)

st.write(msft.info)