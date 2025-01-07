import json
import streamlit as st
import openai

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]


st.title("CLUSS-oefencoach - minimale test b")

# Instructies en introductie
from openai import OpenAI
client = OpenAI()

def get_completion(prompt, client_instance, model="gpt-3.5-turbo"):
  messages = [{"role": "user", "content": prompt}]
  response = client_instance.chat.completions.create(
  model=model,
  messages=messages,
  max_tokens=50,
  temperature=0,
  )
  return response.choices[0].message["content"]

get_completion(prompt, client) # call your function
