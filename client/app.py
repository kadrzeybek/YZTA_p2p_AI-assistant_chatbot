import streamlit as st
from components.upload import render_uploader
from components.chatUI import render_chat

st.set_page_config(page_title="AI Assistant",layout="wide")
st.title("P2P Assistant Chatbot")

render_uploader()
render_chat()
