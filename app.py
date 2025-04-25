import streamlit as st

from libs.llm_utils import send_message_to_llm, start_session
from libs.menu_loader import load_menu
#menu
CAKE_MENU = load_menu()


# UI
st.title("🎂 Habibi Home Bakery AI Assistant 🎂")
st.markdown("Serving Dubai & Sharjah | Homemade cakes 🎂 | Payment on Delivery")

if "messages" not in st.session_state:
    start_session()
    welcome_message = (
        "Hi there! Welcome to Habibi Cakes\n\n"
        "Here's our menu:\n" + CAKE_MENU + "\n\n"
        "What would like you like order today?"
    )
    st.session_state.messages = [{
        "role":"ai",
        "content":welcome_message
    }]

user_input = st.chat_input("Enter your message...")

if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content": user_input
    })
    llm_resp = send_message_to_llm(user_input)
    # storing llm resp to chat history
    st.session_state.messages.append({
        "role":"ai",
        "content": llm_resp
    })



for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
