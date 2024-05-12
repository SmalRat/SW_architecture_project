import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("Restaurant app")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            st.page_link("pages/change_menu.py", label="Change menu", icon="📒")
            st.page_link("pages/stats.py", label="Statistics", icon="📊")
            st.page_link("pages/admin_chat.py", label="Client's chat", icon="📤")

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()
        else:
            st.page_link("pages/menu.py", label="Menu", icon="📒")
            st.page_link("pages/make_order.py", label="Make order", icon="🛒")
            st.page_link("pages/reserve_table.py", label="Reserve table", icon="🛎️")
            st.page_link("pages/client_chat.py", label="Connect with a worker", icon="📤")

            st.page_link("pages/admin.py", label="Admin", icon="🔒")


def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("main.py")