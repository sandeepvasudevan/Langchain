#Imports 
import langchain
import langchain_core
import langchain_community
import langchain_groq
import streamlit as str
import google.generativeai as genai
from PIL import Image

#Gemini Pro --> API_KEY
API_KEY='AIzaSyBlCIwsD6iMOvx6Rn7V3_VfKYyEo2xNGTI'

#Set up LLM
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel(model_name='gemini-1.5-flash-001')

#Generate content from uploaded image
def generate_content(input,image):
    if input:
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text        
    

#Streamlit Section    
str.set_page_config('Gemini Image Demo')
str.header('Image Descriptor')
input=str.text_input('Type your question',key='input')
uploadedfile=str.file_uploader("Choose an image",type=["jpg","jpeg","png"],key='image')
image=""
if uploadedfile is not None:
    image=Image.open(uploadedfile)
    str.image(image,caption='Uploaded Image',use_container_width=True)

submit=str.button("Tell me about the image")

if submit:
    response=generate_content(input,image)
    str.header("description")
    str.write(response)