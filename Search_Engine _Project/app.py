
import streamlit as st 
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_huggingface import HuggingFaceEmbeddings
import time
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
groq_api_key=os.getenv("GROQ_API_KEY")

## Tools integration
api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=2500)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=2500)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name="search")


st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

# embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assisstant","content":"Hi,I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

chat_box = st.chat_input("What do you want to do?")
if "uploader_visible" not in st.session_state:
    st.session_state["uploader_visible"] = False
def show_upload(state:bool):
    st.session_state["uploader_visible"] = state
    
with st.chat_message("system"):
    cols= st.columns((3,1,1))
    cols[0].write("Do you want to upload a file?")
    cols[1].button("yes", use_container_width=True, on_click=show_upload, args=[True])
    cols[2].button("no", use_container_width=True, on_click=show_upload, args=[False])

if st.session_state["uploader_visible"]:
    with st.chat_message("system"):
        file = st.file_uploader("Upload your data")
        if file:
            with st.spinner("Processing your file"):
                time.sleep(5) 
if prompt:=st.chat_input(placeholder="What is machine learning?"):
    # uploaded_file = st.file_uploader("📎 Attach a file", type=["txt", "pdf", "png", "jpg"], label_visibility="collapsed")

    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm=ChatGroq(groq_api_key=groq_api_key,model_name="Llama3-8b-8192",streaming=True)
    tools=[search,arxiv,wiki]

    search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',"content":response})
        st.write(response)
