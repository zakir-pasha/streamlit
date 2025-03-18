import streamlit as st
import time

# Set the layout of the page to wide
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
body, .stApp {
    background-color: #f0fcf4;
    color: #333333;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.big-font {
    font-size: 50px !important;
    text-align: center;
    margin-top: 50px;
    color: red;
    font-weight: bold;
}
.welcome-message {
    text-align: center;
    font-size: 18px;
    margin-top: 20px;
}

/* Increased specificity for text input */
.stTextInput > div > div > input {
    color: #333333 !important; /* Force dark gray text */
    border: 1px solid #CCCCCC;
    border-radius: 5px;
    padding: 10px;
    background-color: white !important;
}

.stTextInput > label {
    color: #333333 !important;
}

/* Increased specificity for button */
.stButton > button {
    background-color: #EEEEEE !important; /* Force light gray background */
    color: #333333 !important; /* Force dark gray text */
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    display: block;
    margin: 20px auto;
}
.stButton > button:hover {
    background-color: #DDDDDD !important;
}

.stSpinner > div > div {
    border-color: #1976D2;
}
.stError {
    color: #D32F2F;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Header (optional: add a logo here)
st.markdown('<div class="big-font">Angi AI</div>', unsafe_allow_html=True)

# Welcome message and additional information
st.markdown("""
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
