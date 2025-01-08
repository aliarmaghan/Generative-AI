import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
import pyodbc

os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
groq_api_key=os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜")
st.title("🦜 LangChain: Chat with SQL DB")

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"
SQLSERVER="USE_SQLSERVER"
connect_button = False
db = None 

radio_opt=["Use SQLLite 3 Database","Connect to you MySQL Database","Connect to sql server"]

selected_opt=st.sidebar.radio(label="Choose the DB which you want to chat",options=radio_opt)

if radio_opt.index(selected_opt)==1:
    db_uri=MYSQL
    if not db_uri:
        st.info("Please enter the database information and uri")
    mysql_host=st.sidebar.text_input("Provide MySQL Host")
    mysql_user=st.sidebar.text_input("MYSQL User")
    mysql_password=st.sidebar.text_input("MYSQL password",type="password")
    mysql_db=st.sidebar.text_input("MySQL database")
    connect_button = st.sidebar.button("Connect to MySQL Database")
elif radio_opt.index(selected_opt)==2:

    db_uri = SQLSERVER
    sqlserver_server = st.sidebar.text_input("Provide SQL Server Server")
    sqlserver_user = st.sidebar.text_input("SQL Server User (Leave blank for Windows Authentication)")
    sqlserver_password = st.sidebar.text_input("SQL Server Password (Leave blank if not required)", type="password")
    sqlserver_db = st.sidebar.text_input("SQL Server Database")
    connect_button = st.sidebar.button("Connect to SQL Server")

else:
    db_uri=LOCALDB


## LLM Model
llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama3-8b-8192",streaming=True)

@st.cache_resource(ttl="2h")

def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None, sqlserver_driver=None,
                sqlserver_server=None, sqlserver_user=None, sqlserver_password=None, sqlserver_db=None):
    if db_uri == LOCALDB:
        dbfilepath = (Path(__file__).parent / "student.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))
    elif db_uri == SQLSERVER:
        if not sqlserver_server or not sqlserver_db:
            st.error("Please provide SQL Server Server and Database details.")
            st.stop()

        if sqlserver_user and sqlserver_password:
            # Connect with username and password
            # connection_string = f"mssql+pyodbc://{sqlserver_user}:{sqlserver_password}@{sqlserver_server}/{sqlserver_db}?driver=SQL Server Native Client 11.0"
            connection_string = (f"mssql+pyodbc://{sqlserver_user}:{sqlserver_password}@{sqlserver_server}/{sqlserver_db}""?driver=ODBC+Driver+17+for+SQL+Server")

        else:
            # Use Windows Authentication
            # connection_string = f"mssql+pyodbc://{sqlserver_server}/{sqlserver_db}?driver=SQL Server Native Client 11.0;trusted_connection=yes"
            connection_string = (f"mssql+pyodbc://{sqlserver_server}/{sqlserver_db}?""driver=ODBC+Driver+17+for+SQL+Server;trusted_connection=yes")


        return SQLDatabase(create_engine(connection_string))



# Updated code:
if connect_button:
    with st.spinner("Connecting to the database..."):
        try:
            if db_uri == MYSQL:
                db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
            elif db_uri == SQLSERVER:
                if sqlserver_user and sqlserver_password:
                    db = configure_db(db_uri, sqlserver_server, sqlserver_user, sqlserver_password, sqlserver_db)
                else:
                    db = configure_db(db_uri, sqlserver_server=sqlserver_server, sqlserver_db=sqlserver_db)
            else:
                db = configure_db(db_uri)
            
            st.success("Connected to the database successfully!")
        except Exception as e:
            st.error(f"Failed to connect to the database: {e}")
            db = None


if db:
    try:
        # Create the toolkit
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        # Create the SQL agent
        agent = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )

        st.success("Agent and toolkit successfully initialized.")
    except Exception as e:
        st.error(f"Failed to create the toolkit or agent: {e}")
else:
    st.warning("No valid database connection. Please connect to a database first.")

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)
