import streamlit as st

def logout_page():
    st.title("Logout")
    st.write("You have been logged out.")
    st.session_state['logged_in'] = False
