import streamlit as st
import requests

API = "https://proscores-ai.onrender.com"

st.set_page_config("ProScore AI", "⚽", "wide")

if "token" not in st.session_state:
    st.session_state.token = None

if not st.session_state.token:
    email = st.text_input("Email")
    if st.button("Login"):
        r = requests.post(f"{API}/auth/login"
        st.session_state.token = r.json()["access_token"]
        st.rerun()

st.sidebar.success("Logged in")
st.title("🚀 ProScore AI Dashboard")
