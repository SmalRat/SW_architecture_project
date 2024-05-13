import streamlit as st
from navigation import make_sidebar

make_sidebar()

st.switch_page("pages/menu.py")
