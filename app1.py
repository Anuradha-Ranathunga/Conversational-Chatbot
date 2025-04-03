## Conversationl Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

## Streamlit UI
st.set_page_config(page_title="Conversational Chatbot")
st.header("Hey, Let's Chat")

from dotenv import load_dotenv
load_dotenv()
import os

chat=ChatOpenAI(temperature=0.5)


## Function to load OpenAI model and get response

def get_openai_response(question):
    llm=OpenAI(model_name="text-davinci-003", temperature=0.5)
    response= llm(question)
    return response