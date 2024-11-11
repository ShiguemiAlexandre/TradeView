import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

title_dol = st.container()
st.divider()

value_dol = yf.Ticker("BRL=X").info["bid"]
title_dol.subheader(f"Dolar: {value_dol}")

lista_ativos = {
    "AAPL": {"valor": 221.8988, "quantidade": 0.02203707, "dol": True},
    "BRK-B": {"valor": 476.4288, "quantidade": 0.02098949, "dol": True},
    "GOOGL": {"valor": 157.5788, "quantidade": 0.03103209, "dol": True},
    "INTC": {"valor": 20.1788, "quantidade": 0.09911392, "dol": True},
    "MSFT": {"valor": 409.9788, "quantidade": 0.01193035, "dol": True},
    "BCFF11.SA": {"valor": 7.44,"quantidade": 1},
    "XPLG11.SA": {"valor": 95.54,"quantidade": 1}, 
    "MXRF11.SA": {"valor": 9.77,"quantidade": 1}
}

valor_real = []
labels = []
sizes = []
total = 0

for symbol in lista_ativos:
    labels.append(symbol)
    current = lista_ativos[symbol]
    value = current["valor"] * current["quantidade"]

    # Caso o ativo for em dolar ele irá converter o valor para real para todos ficarem na mesma moeda
    if lista_ativos[symbol].get("dol"):
        value = value * value_dol
    
    sizes.append(value)
    total = total + value
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
