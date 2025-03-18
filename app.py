import streamlit as st
import pandas as pd
from openai import OpenAI



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
.stTextInput > div > div > input {
    color: #333333;
    border: 1px solid #CCCCCC;
    border-radius: 5px;
    padding: 10px;
    background-color: white;
}
.stTextInput > label {
    color: #333333;
}
.stButton > button {
    background-color: #EEEEEE;
    color: #333333;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    display: block;
    margin: 20px auto;
}
.stButton > button:hover {
    background-color: #DDDDDD;
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

# Header
st.markdown('<div class="big-font">Angi AI</div>', unsafe_allow_html=True)

# Welcome message
st.markdown("""
<div class="welcome-message">
    Welcome to Angi AI! Primarily trained to help with your querying needs.<br>
    For more information, join the #ai-pilot-project-analytics Slack channel.
</div>
""", unsafe_allow_html=True)

# Load your column definitions from CSV
df = pd.read_csv('table_def.csv')
columns_descriptions = '\n'.join([f"{row['Column of Interest']}: {row['Suggested Definition']}" for index, row in df.iterrows()])

# API Key (Securely handled)
api_key = st.secrets["openai_secret_key"]
client = OpenAI(api_key=api_key)

# Create a container for the text input and button
with st.container():
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        with st.form("my_form"):
            question = st.text_input("Ask me a question about F_SP", placeholder="Ask me a question about F_SP")
            submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Generating SQL query...'):
                detailed_prompt = f"""
                You are a Snowflake SQL generator. Given the following column descriptions, generate an SQL query based on the user's request. The table name is rpt.reports.f_sp.

                Column Descriptions:
                {columns_descriptions}

                User Query: {question}
                """

                response = client.responses.create(
                      model="gpt-3.5-turbo",
                      input=detailed_prompt,
                      max_output_tokens=2048,
                      temperature=0,
                      top_p=1,
                      store=True
                )

                # Process and display the response
                if response.output and isinstance(response.output, list):
                    for message in response.output:
                        if message.role == 'assistant' and message.content:
                            for content_piece in message.content:
                                if content_piece.type == 'output_text' and len(content_piece.text.strip()) > 10:
                                    sql_output = content_piece.text.strip()
                                    st.success(sql_output)
                                else:
                                    st.error("We're still training Angi AI. Please try again in a few weeks.")
                else:
                    st.error("We're still training Angi AI. Please try again in a few weeks.")

# Footer
# st.markdown("<div style='text-align: center; margin-top: 50px; color: #777777;'>© 2024 Angi AI</div>", unsafe_allow_html=True)
