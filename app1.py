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
os.environ["OPENAI_API_KEY"] = "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"

chat=ChatOpenAI(
    temperature=0.5,
    openai_api_key="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"
    )

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content='You are a comedian AI assistant.')
    ]

## Function to load OpenAI model and get response

def get_chatmodel_response(question):
    
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input= st.text_input("Input: ", key="input")
response= get_chatmodel_response(input)

submit= st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
