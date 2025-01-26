from langgraph.graph import StateGraph, END
from typing import Dict, TypedDict
from scripts.query_classifier import categorize
from scripts.sentiment_analysis import analyze_sentiment
from scripts.knowledge_retrieval import handle_technical, handle_billing, handle_general, escalate

# Define State Structure
class State(TypedDict):
    query: str
    category: str
    sentiment: str
    response: str


def route_query(state: dict) -> str:
    if state["sentiment"] == "Negative":
        return "escalate"
    elif state["category"] == "Technical":
        return "handle_technical"
    elif state["category"] == "Billing":
        return "handle_billing"
    elif state["category"] == "General":
        return "handle_general"
    else:
        return "handle_general"  # Default fallback


# Create and Configure the Graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("categorize", categorize)
workflow.add_node("analyze_sentiment", analyze_sentiment)
workflow.add_node("handle_technical", handle_technical)
workflow.add_node("handle_billing", handle_billing)
workflow.add_node("handle_general", handle_general)
workflow.add_node("escalate", escalate)

# Add edges
workflow.add_edge("categorize", "analyze_sentiment")
workflow.add_conditional_edges(
    "analyze_sentiment",
    route_query,
    {
        "handle_technical": "handle_technical",
        "handle_billing": "handle_billing",
        "handle_general": "handle_general",
        "escalate": "escalate"
    }
)
workflow.add_edge("handle_technical", END)
workflow.add_edge("handle_billing", END)
workflow.add_edge("handle_general", END)
workflow.add_edge("escalate", END)

# Set entry point
workflow.set_entry_point("categorize")

# Compile the graph
app = workflow.compile()

def run_customer_support(query: str) -> dict:
    results = app.invoke({"query": query})
    return {
        "category": results["category"],
        "sentiment": results["sentiment"],
        "response": results["response"]
    }