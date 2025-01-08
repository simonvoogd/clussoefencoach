import json
import streamlit as st
import openai

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CLUSS-oefencoach - minimale test e")

# Maak een API-aanroep
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "Je bent een vriendelijke assistent."},
        {"role": "user", "content": "Hey, bro"}
    ]
)

# Toon resultaten
print(response['choices'][0]['message']['content'])
print(response.get('usage'))  # Laat het gebruik zien (tokens)
