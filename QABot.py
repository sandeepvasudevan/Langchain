#Library Imports
import google.generativeai as genai
import langchain_community
import langchain_core
import langchain_groq
import langchain_text_splitters
import streamlit as str


#Definitions
API_KEY='yourownapikey'

#Configure LLMS
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel(model_name='gemini-pro')

#Function to generate content from LLM
def generate_content(question):
    response=model.generate_content(question)
    return response.text

#Streamlit Section
str.set_page_config(page_title='Demo QA')
str.header('QA Chatbot')
input=str.text_input('Input the question',key='input')
if input:
    response=generate_content(input)
    str.write(response)

