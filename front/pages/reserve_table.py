import streamlit as st
import requests
from navigation import make_sidebar
from time import sleep
make_sidebar()
from config import get_settings

settings = get_settings()

all_times = set(i for i in range(8, 23))
def fetch_tables():
    response = requests.get(f"{settings.reservation_url}/tables")

    tables = response.json()
    return tables

def fetch_available_times(table_id):
    response = requests.get(f"{settings.reservation_url}/tables/{table_id}")

    tables = response.json()
    booked_times = set(table["booking_time"] for table in tables)

    return [f"{time}:00" for time in all_times - booked_times]

def reserve_table(table_id, time, user):
    data = {
      "user_name": user,
      "table_number": table_id,
      "booking_time": time
    }
    response = requests.post(f"{settings.reservation_url}/create_booking", json=data)

    result = response.json()

    return response.status_code == 200

tables_resp = fetch_tables()

if "tables" not in st.session_state:
    st.session_state["tables"] = {table["_id"]: False for table in tables_resp}
tables_length = len(tables_resp)
if tables_length != len(st.session_state["tables"]):
    for table in tables_resp:
        if not st.session_state["tables"].get(table["_id"]):
            st.session_state["tables"][table["_id"]] = False

tables = st.session_state["tables"]

def on_advanced_button_click(buttons: dict[str, bool], id: str) -> None:
    buttons[id] = True


def on_less_click(buttons: dict[str, bool], id: str) -> None:
    buttons[id] = False


def display_tables(tables_resp, tables):
    for idx, table in enumerate(tables_resp):


        if tables[table["_id"]]:
            st.button(
                "less",
                key=f"table_{idx}",
                on_click=on_less_click,
                args=(tables, table["_id"]),
                use_container_width=True,
            )

            available_times = fetch_available_times(table["_id"])
            if available_times:
                st.write("Available times:")

                # Create a grid of buttons in a single row
                # Adjust the number of columns based on the number of available times
                cols_per_row = 8  # Define how many columns per row you want
                num_rows = (len(available_times) + cols_per_row - 1) // cols_per_row  # Calculate needed rows
                grid = [st.columns(cols_per_row) for _ in range(num_rows)]

                if 'selected_time' not in st.session_state:
                    st.session_state.selected_time = None
                if 'form_submitted' not in st.session_state:
                    st.session_state.form_submitted = False

                idx = 0
                for time in available_times:
                    row = idx // cols_per_row
                    col = idx % cols_per_row
                    if grid[row][col].button(time, key=time, use_container_width=True):
                        st.session_state.selected_time = time
                        st.session_state.form_submitted = False
                    idx += 1

                if st.session_state.selected_time and not st.session_state.form_submitted:
                    selected_time = st.session_state.selected_time
                    st.write(f"You selected {selected_time}. Please enter your details to confirm.")

                    with st.form(key='user_details_form'):
                        name = st.text_input("Name", key='name')
                        submit_button = st.form_submit_button("Submit Reservation")

                        if submit_button:
                            st.session_state.form_submitted = True
                            if reserve_table(table["_id"], selected_time.split(":")[0], name):
                                st.success(f"Reservation confirmed for {name} at {selected_time}")
                                sleep(2)
                                on_less_click(tables, table["_id"])
                                st.rerun()

            else:
                st.error("No available times for this table.")

        else:
            st.button(
                (
                    f"Table number: {table['_id']}, seats: {table['number_of_seats']}"
                ),
                key=f"table_{idx}",
                on_click=on_advanced_button_click,
                args=(tables, table["_id"]),
                type="secondary",
                use_container_width=True,
            )

display_tables(tables_resp,tables)