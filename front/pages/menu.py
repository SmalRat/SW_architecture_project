import streamlit as st
import requests

from config import get_settings

from navigation import make_sidebar

make_sidebar()
settings = get_settings()


st.write("# Welcome to our Restaurant! 👋")
response = requests.get(f"{settings.backend_url_guest}/menu")

if response.status_code != 404:
    menu = response.json()

    formatted_menu_data = []
    for item in menu:
        name = item["name"]
        price = item["price"]
        formatted_price = f"${price:.2f}"
        formatted_menu_data.append({"name": name, "price": formatted_price})


    st.table(formatted_menu_data)

else:
    st.error("Service is temporarily unavailable")
