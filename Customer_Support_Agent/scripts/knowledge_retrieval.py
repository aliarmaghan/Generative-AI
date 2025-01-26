from langchain_core.prompts import ChatPromptTemplate
from config.settings import GROQ_API_KEY
from langchain_groq import ChatGroq

def handle_technical(state: dict) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Provide a technical support response to the following query: {query}"
    )
    chain = prompt | ChatGroq(api_key=GROQ_API_KEY)
    response = chain.invoke({"query": state["query"]}).content
    return {"response": response}

def handle_billing(state: dict) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Provide a billing support response to the following query: {query}"
    )
    chain = prompt | ChatGroq(api_key=GROQ_API_KEY)
    response = chain.invoke({"query": state["query"]}).content
    return {"response": response}

def handle_general(state: dict) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Provide a general support response to the following query: {query}"
    )
    chain = prompt | ChatGroq(api_key=GROQ_API_KEY)
    response = chain.invoke({"query": state["query"]}).content
    return {"response": response}

def escalate(state: dict) -> dict:
    return {"response": "This query has been escalated to a human agent due to its negative sentiment."}