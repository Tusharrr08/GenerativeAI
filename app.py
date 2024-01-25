from dotenv import load_dotenv
load_dotenv() #loading all the environment variable

import streamlit as st 
import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load model & get response
model=genai.GenerativeModel("gemini-pro")
def get_response(question):
    response=model.generate_content(question)
    return response.text

#setting streamlit app

st.set_page_config(page_title="Q&A")
st.header("GEMINI LLM APPLICATION")

input=st.text_input("Input:",key=input)
submit=st.button("ASK THE QUESTION")

if submit:
    response=get_response(input)
    st.subheader("THE RESPONSE IS : ")
    st.write(response)