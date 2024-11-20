import google.generativeai as genai
import langchain_community
import langchain_core
import langchain_groq
import langchain_text_splitters
import streamlit as str

API_KEY='yourownapikey'

genai.configure(api_key=API_KEY)
model=genai.GenerativeModel(model_name='gemini-pro')

def generate_content(question):
    response=model.generate_content(question)
    return response.text

str.set_page_config(page_title='Demo QA')
str.header('QA Chatbot')
input=str.text_input('Input the question',key='input')
if input:
    response=generate_content(input)
    str.write(response)

