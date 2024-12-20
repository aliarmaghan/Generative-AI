import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Open-Source Model"
groq_api_key=os.getenv("GROQ_API_KEY")


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    # llm=Ollama(model=llm)
    llm=ChatGroq(model=engine,groq_api_key=groq_api_key)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Enhanced Q&A Chatbot With Open-Source Model")


## Select the OpenAI model
llm=st.sidebar.selectbox("Select Open Source model",["gemma2-9b-it","mixtral-8x7b-32768","llama-3.2-90b-text-preview"])
# llm=st.sidebar.selectbox("Select Open Source model",["gemma2:2b"])


## Adjust response parameter
temperature=st.sidebar.slider("Temperature: This controls how creative or random the model's responses are. Lower values (e.g., 0.2) make the output focused and predictable, while higher values (e.g., 0.8 or 1.0) make it more diverse and creative.",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens: This limits the length of the model’s response. A smaller value produces shorter, concise answers, while a larger value allows for longer, more detailed outputs.", min_value=50, max_value=300, value=150)

## MAin interface for user input
user_input=st.text_input("Go ahead and ask any question")



if user_input :
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")


