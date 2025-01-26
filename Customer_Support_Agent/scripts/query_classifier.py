from langchain_core.prompts import ChatPromptTemplate
from config.settings import GROQ_API_KEY
from langchain_groq import ChatGroq

def categorize(state: dict) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Categorize the following customer query into one of these categories: "
        "Technical, Billing, General. Query: {query}"
    )
    chain = prompt | ChatGroq(api_key=GROQ_API_KEY)
    category = chain.invoke({"query": state["query"]}).content
    return {"category": category}