import streamlit as st
import requests

from config import get_settings

from navigation import make_sidebar

make_sidebar()
settings = get_settings()

response = requests.get(f"{settings.reservation_url}/bookings")

if response.status_code != 404:
    bookings = response.json()

    st.table(bookings)
else:
    st.error("Service is temporarily unavailable")
