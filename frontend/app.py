import streamlit as st
import requests

API = "http://backend:8000"

st.set_page_config("ProScore AI", "⚽", "wide")

if "token" not in st.session_state:
    st.session_state.token = None

if not st.session_state.token:
    email = st.text_input("Email")
    if st.button("Login"):
        r = requests.post(f"{API}/auth/login", params={"email": email})
        st.session_state.token = r.json()["access_token"]
        st.rerun()

st.sidebar.success("Logged in")
st.title("🚀 ProScore AI Dashboard")
