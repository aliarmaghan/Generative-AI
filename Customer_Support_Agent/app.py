import streamlit as st
from scripts.workflow_engine import run_customer_support
from components.sidebar import render_sidebar
from components.response_display import render_response

# Main app
def main():
    st.set_page_config(page_title="Intelligent Customer Support Agent", layout="wide")
    
    # Render sidebar
    render_sidebar()
    
    # Main content
    st.title("Intelligent Customer Support Agent")
    query = st.text_input("Enter your query:")
    
    if st.button("Submit"):
        if query:
            result = run_customer_support(query)
            render_response(result)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()