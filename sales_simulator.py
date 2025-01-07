import streamlit as st
import openai

# Controleer de OpenAI-versie (debug)
st.write(f"OpenAI library version: {openai.__version__}")

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CLUSS-oefencoach - minimale test7!")

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

except Exception as e:  # Algemene foutafhandeling
    st.error(f"Er trad een fout op: {str(e)}")
