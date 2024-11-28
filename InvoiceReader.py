#Imports
import google.generativeai as genai
import langchain
import langchain_community
import langchain_core
import langchain_groq
import streamlit as str
from PIL import Image

#Model Configuration
gemini_api_key='AIzaSyBlCIwsD6iMOvx6Rn7V3_VfKYyEo2xNGTI'
genai.configure(api_key=gemini_api_key)
model=genai.GenerativeModel(model_name='gemini-1.5-flash-002')

def generate_content(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])  
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

#Streamlit
str.set_page_config('Invoice Reader App')
str.header('Multi Language Invoice Reader')
input=str.text_input("Input text",key='input')
uploaded_file=str.file_uploader('Choose an image',type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    str.image(image,caption="Uploaded Image",use_container_width=True)

submit=str.button("Tell me about the image")

input_prompt=""" 
You are an expert in understanding the invoices.
We will upload the image which is an invoice in any language.
You have to provide the answers based on the questions I ask"""

if submit:
    image_data=input_image_details(uploaded_file)
    response=generate_content(input,image_data,input_prompt)
    str.subheader("The Response is")
    str.write(response)
