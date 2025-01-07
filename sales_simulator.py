import streamlit as st
import openai
from openai.error import OpenAIError, RateLimitError, AuthenticationError  # Specifieke fouten importeren

# Controleer de OpenAI-versie (debug)
st.write(f"OpenAI library version: {openai.__version__}")

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CLUSS-oefencoach - minimale test5!")

# Maak een voorbeeldaanroep naar de API
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Je bent een vriendelijke assistent."},
            {"role": "user", "content": "Wat is het weer vandaag?"}
        ]
    )
    # Toon het antwoord van de GPT in Streamlit
    st.write(response["choices"][0]["message"]["content"])

except RateLimitError:
    st.error("Je hebt je API-quota overschreden. Controleer je OpenAI-account.")
except AuthenticationError:
    st.error("Er is een probleem met je API-sleutel. Controleer je Streamlit Secrets.")
except OpenAIError as e:
    st.error(f"Er trad een algemene fout op: {str(e)}")
