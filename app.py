import streamlit as st
import time

# Set the layout of the page to wide
st.set_page_config(layout="wide")

# Define color palette (adjust to your preference)
primary_color = "#1976D2"  # A professional blue
background_color = "#f0fcf4"  # Light minty green background
text_color = "#333333"  # Dark gray text
angi_ai_color = "red"  # Angi AI text color

# Custom CSS for styling
st.markdown(f"""
<style>
body, .stApp {{
    background-color: {background_color};
    color: {text_color};
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}
.big-font {{
    font-size: 50px !important;
    text-align: center;
    margin-top: 50px;
    color: {angi_ai_color};
    font-weight: bold;
}}
.welcome-message {{
    text-align: center;
    font-size: 18px;
    margin-top: 20px;
}}
.stTextInput > div > div > input {{
    color: {text_color} !important;
    border: 1px solid #CCCCCC;
    border-radius: 5px;
    padding: 10px;
}}
.stTextInput > label {{
    color: {text_color} !important;
}}
.stButton > button {{
    background-color: {primary_color};
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    display: block;
    margin: 20px auto;
}}
.stButton > button:hover {{
    background-color: #1565C0;
}}
.stSpinner > div > div {{
    border-color: {primary_color};
}}
.stError {{
    color: #D32F2F;  # A professional red for errors
    text-align: center;
    margin-top: 20px;
}}
</style>
""", unsafe_allow_html=True)

# Header (optional: add a logo here)
st.markdown('<div class="big-font">Angi AI</div>', unsafe_allow_html=True)

# Welcome message and additional information
st.markdown(f"""
<div class="welcome-message">
    Welcome to Angi AI! Primarily trained F_SP to help with your querying needs.<br>
    For more information or context on this team, join the #ai-pilot-project-analytics Slack channel.
</div>
""", unsafe_allow_html=True)

# Create a container for the text input and button
with st.container():
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        with st.form("my_form"):
            question = st.text_input("Ask me a question about F_SP", placeholder="Ask me a question about F_SP")
            submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Loading...'):
                time.sleep(2)  # Simulate a loading time
            st.error("We're still training Angi AI. Please try again in a few weeks.")

# Footer (optional: add copyright or contact information)
# st.markdown("<div style='text-align: center; margin-top: 50px; color: #777777;'>© 2024 Angi AI</div>", unsafe_allow_html=True)
