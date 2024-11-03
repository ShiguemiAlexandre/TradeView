import streamlit as st
import yfinance as yf

msft = yf.Ticker("^BCFF11")
st.write(msft.info)