import streamlit as st

# Login
login_page = st.Page("./pages/auth/login.py", title="Autenticação")

# Logout
logout_page = st.Page("./pages/auth/logout.py", title="Logout", icon=":material/logout:")

# Home
home_page = st.Page("./pages/home/home.py", title="Home", icon=":material/home:")

pg = st.navigation(
    [home_page, logout_page]
)

pg.run()