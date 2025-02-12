
# import streamlit as st 
# from langchain_groq import ChatGroq
# from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
# from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
# from langchain.agents import initialize_agent,AgentType
# # from langchain.callbacks import StreamlitCallbackHandler
# from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
# from langchain_huggingface import HuggingFaceEmbeddings
# import time
# import os
# from dotenv import load_dotenv
# load_dotenv()

# os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
# groq_api_key=os.getenv("GROQ_API_KEY")

# ## Tools integration
# api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=2500)
# wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

# api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=2500)
# arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

# search = DuckDuckGoSearchRun(name="search")


# st.title("🔎 LangChain - Chat with search")
# """
# In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
# Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
# """

# embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# ## Sidebar for settings

# if "messages" not in st.session_state:
#     st.session_state["messages"]=[
#         {"role":"assisstant","content":"Hi,I'm a chatbot who can search the web. How can I help you?"}
#     ]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg['content'])

# prompt=st.chat_input(placeholder="What is machine learning?")
# # Pin/Attach icon section
# col1, col2 = st.columns([0.1, 0.9])  # Layout with columns for placing the icon and text box
# with col1:
#     attach_clicked = st.button("📎")  # Pin/Attach button
# with col2:
#     st.write("Click the pin icon to attach files.")

# # File upload section
# if attach_clicked:
#     st.subheader("Attach Your Files")
#     uploaded_files = st.file_uploader(
#         "Upload multiple files", accept_multiple_files=True
#     )
#     if uploaded_files:
#         st.success(f"Uploaded {len(uploaded_files)} files.")
#         for file in uploaded_files:
#             st.write(f"File name: {file.name}")

# if prompt:
#     st.session_state.messages.append({"role":"user","content":prompt})
#     st.chat_message("user").write(prompt)

#     llm=ChatGroq(groq_api_key=groq_api_key,model_name="Llama3-8b-8192",streaming=True)
#     tools=[search,arxiv,wiki]

#     search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=False)

#     with st.chat_message("assistant"):
#         st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
#         response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
#         st.session_state.messages.append({'role':'assistant',"content":response})
#         st.write(response)





import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
# from langchain.callbacks import StreamlitCallbackHandler
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_huggingface import HuggingFaceEmbeddings
import time
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")
groq_api_key = os.getenv("GROQ_API_KEY")

## Tools integration
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2500)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=2500)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name="search")

st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

## Sidebar for settings
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# File upload section moved to left corner
col1, col2 = st.columns([0.1, 0.9])  # Layout with columns for placing the icon and text box
with col1:
    attach_clicked = st.button("📎", key="attach")  # Pin/Attach button
with col2:
    prompt = st.chat_input(placeholder="What is machine learning?")

# Attach files if the button is clicked
if attach_clicked:
    st.subheader("Attach Your Files")
    uploaded_files = st.file_uploader(
        "Upload multiple files", accept_multiple_files=True
    )
    if uploaded_files:
        st.success(f"Uploaded {len(uploaded_files)} files.")
        for file in uploaded_files:
            st.write(f"File name: {file.name}")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", streaming=True)
    tools = [search, arxiv, wiki]

    search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=False)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role': 'assistant', "content": response})
        st.write(response)

