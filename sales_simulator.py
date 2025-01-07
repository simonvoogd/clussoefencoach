import json
import streamlit as st
import openai

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CLUSS-oefencoach - minimale test9")

# Instructies en introductie
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Je bent een vriendelijke assistent."},
            {"role": "user", "content": "Wat is het weer vandaag?"}
        ]
    )
    # Show the response in Streamlit
    st.write(response["choices"][0]["message"]["content"])

except Exception as e:  # General error handling
    st.error(f"Er trad een fout op: {str(e)}")
