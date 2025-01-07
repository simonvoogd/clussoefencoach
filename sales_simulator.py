import json
import streamlit as st
import openai

# OpenAI API-sleutel instellen
openai.api_key = st.secrets["OPENAI_API_KEY"]


st.title("CLUSS-oefencoach - minimale test d")

from openai import OpenAI

client = OpenAI()

completion = client.completions.create(
    model='gpt-3.5-turbo',
    prompt='hey, bro\n\n'
    )
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
