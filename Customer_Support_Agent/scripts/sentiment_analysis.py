from langchain_core.prompts import ChatPromptTemplate
from config.settings import GROQ_API_KEY
from langchain_groq import ChatGroq

def analyze_sentiment(state: dict) -> dict:
    prompt = ChatPromptTemplate.from_template(
        "Analyze the sentiment of the following customer query. "
        "Respond with either 'Positive', 'Neutral', or 'Negative'. Query: {query}"
    )
    chain = prompt | ChatGroq(api_key=GROQ_API_KEY)
    sentiment = chain.invoke({"query": state["query"]}).content
    return {"sentiment": sentiment}