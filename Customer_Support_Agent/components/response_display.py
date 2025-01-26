import streamlit as st

def render_response(result: dict):
    st.write(f"**Category:** {result['category']}")
    st.write(f"**Sentiment:** {result['sentiment']}")
    st.write(f"**Response:** {result['response']}")