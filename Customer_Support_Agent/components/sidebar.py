import streamlit as st

def render_sidebar():
    st.sidebar.title("Settings")
    st.sidebar.radio("Select a model", ["OpenAI", "Groq"])
    st.sidebar.markdown("Configure your preferences here.")