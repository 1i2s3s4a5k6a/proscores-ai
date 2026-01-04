import streamlit as st
import requests

API = "https://proscores-ai.onrender.com"

st.set_page_config(page_title="ProScore AI", page_icon="⚽", layout="wide")

# 1. Initialize session state
if "token" not in st.session_state:
    st.session_state.token = None

# 2. Login Logic
if not st.session_state.token:
    email = st.text_input("Email")
    if st.button("Login"):
        try:
            r = requests.post(f"{API}/auth/login", params={"email": email})
            # This matches the "access_token" key you added to your backend
            st.session_state.token = r.json()["access_token"]
            st.rerun()
        except Exception as e:
            st.error(f"Login failed: {e}")
    st.stop()  # Stop the script here so the dashboard doesn't show yet

# 3. Dashboard Logic (Only runs if token exists)
st.sidebar.success("Logged in")
st.title("🚀 ProScore AI Dashboard")

