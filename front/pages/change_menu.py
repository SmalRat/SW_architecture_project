import streamlit as st

from config import get_settings
from navigation import make_sidebar
from pages.change_menu_func.add_item import add_item
from pages.change_menu_func.change_stock import change_stock
from pages.change_menu_func.get_menu import get_menu


make_sidebar()
settings = get_settings()


st.title("Admin Dashboard")

# Sidebar menu
selected_option = st.sidebar.radio(
    "Select an Option", ("Get Menu", "Add Menu Item", "Change Stock")
)

if selected_option == "Add Menu Item":
    add_item()

elif selected_option == "Change Stock":
    change_stock()

elif selected_option == "Get Menu":
    get_menu()
