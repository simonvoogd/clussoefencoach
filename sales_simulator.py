import json
import streamlit as st
import openai

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CLUSS-oefencoach")

# Instructies en introductie
st.markdown("""
Deze applicatie simuleert verkoopgesprekken volgens de CLUSS-methode (Context, Latente Behoefte, Urgentie, Solution Benefits, Shared Vision). 
Het doel is om verkoopvaardigheden te oefenen met een virtuele klant en een gedetailleerd feedbackrapport te ontvangen.
""")

# Instellen van gesprek
st.header("Stap 1: Instellingen")
bedrijf = st.text_input("Welk bedrijf of sector vertegenwoordigt u?")
propositie = st.text_area("Beschrijf kort uw propositie:")
type_gesprek = st.selectbox("Kies het type gesprek:", 
                            ["Cold call", "Netwerkgesprek", "Klantinitiatief", "Koffieautomaatmoment", "Bekende klant met nieuwe propositie"])
moeilijkheidsgraad = st.radio("Kies de moeilijkheidsgraad:", ["Beginner", "Gevorderd", "Expert"])

if st.button("Start gesprek"):
    # Voorbeeld API-aanroep met OpenAI (vervang 'YOUR_API_KEY' met je eigen API-sleutel)
    # openai.api_key = 'YOUR_API_KEY'
    prompt = f"""
    Simuleer een verkoopgesprek volgens de CLUSS-methode.
    Bedrijf: {bedrijf}
    Propositie: {propositie}
    Type gesprek: {type_gesprek}
    Moeilijkheidsgraad: {moeilijkheidsgraad}
    Begin het gesprek door de virtuele klant zichzelf voor te laten stellen en het gesprek te openen volgens CLUSS.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Je bent een CLUSS-coach."},
                  {"role": "user", "content": prompt}]
    )
    
    # Toon de eerste reactie van de virtuele klant
    st.subheader("Virtuele Klant:")
    st.write(response['choices'][0]['message']['content'])

# Feedback genereren na het gesprek
st.header("Stap 2: Feedbackrapport")
if st.button("Genereer rapport"):
    feedback_prompt = f"""
    Genereer een feedbackrapport voor het bovenstaande gesprek volgens de CLUSS-methode:
    1. Context
    2. Latente Behoefte
    3. Urgentie
    4. Solution Benefits
    5. Shared Vision
    Geef ook algemene feedback en drie concrete verbeterpunten.
    """
    feedback_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Je bent een feedbackspecialist voor CLUSS-methodologie."},
                  {"role": "user", "content": feedback_prompt}]
    )
    
    st.subheader("Feedbackrapport:")
    st.write(feedback_response['choices'][0]['message']['content'])

