import json
import streamlit as st
import openai

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CLUSS-oefencoach - minimale test!")

# Instructies en introductie
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Je bent een vriendelijke assistent."},
        {"role": "user", "content": "Wat is het weer vandaag?"}
    ]
)

st.write(response["choices"][0]["message"]["content"])

