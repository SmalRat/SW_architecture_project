import streamlit as st
import requests

from config import get_settings

from navigation import make_sidebar

make_sidebar()
settings = get_settings()

response = requests.get(f"{settings.reservation_url}/bookings")

bookings = response.json()

st.table(bookings)
