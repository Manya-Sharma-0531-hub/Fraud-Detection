import streamlit as st

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

st.title("💳 Real-Time Fraud Detection Dashboard")

st.markdown("""
Welcome to the Fraud Operations Dashboard.

Use the sidebar to navigate between:

- Overview
- Transaction Explorer
- SHAP Explainer
""")
