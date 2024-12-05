import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



## streamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')



## Get the Groq API Key and url(YT or website)to be summarized
import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model="Gemma-7b-It")

generic_url=st.text_input("URL",label_visibility="collapsed")


## Prompt template for stuff summarization technique
prompt_template="""
Provide a summary of the following content in 1000 words:
Content:{text}
"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

## Prompt template for Map-Reduce summarization technique
final_prompt='''
Provide the final summary of the entire speech with these important points.
Add a Motivation Title,Start the precise summary with an introduction and provide the summary in number 
points for the speech.
Speech:{text}
'''
final_prompt_template=PromptTemplate(input_variables=['text'],template=final_prompt)




## summarize work
if st.button("Summarize"):
    ## validate all inputs
    if not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can may be a YT video utl or website url")

    
    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()
                
                # Chain For Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)
            
                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception:{e}")