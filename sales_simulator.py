import streamlit as st
import openai
import openai.error  # Zorg ervoor dat de error-module correct wordt geïmporteerd

# Controleer de OpenAI-versie (debug)
st.write(f"OpenAI library version: {openai.__version__}")

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CLUSS-oefencoach - minimale test3!")

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

except openai.error.RateLimitError:
    st.error("Je hebt je API-quota overschreden. Controleer je OpenAI-account.")
except openai.error.AuthenticationError:
    st.error("Er is een probleem met je API-sleutel. Controleer je Streamlit Secrets.")
except openai.error.OpenAIError as e:
    st.error(f"Er trad een algemene fout op: {str(e)}")
