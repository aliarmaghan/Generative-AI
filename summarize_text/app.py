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
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model="gemma2-9b-it")
youtube_api_key=os.getenv("YOUTUBE_API_KEY")
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

### professionalize prompt template
pro_prompt_template="""
As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, passage,or youtube transcript while adhering to these guidelines:

Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.

Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.

Rely strictly on the provided text, without including external information.

Format the summary in paragraph form for easy understanding.

Conclude your notes with [End of Notes, Message #X] to indicate completion, where "X" represents the total number of messages that I have sent. In other words, include a message counter where you start with #1 and add 1 to the message counter every time I send a message :{text}.

"""
pro_prompt = PromptTemplate(input_variables=['text'],template=pro_prompt_template)

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
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=False,language="en")
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()
                
                # Chain For Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=pro_prompt)
                output_summary=chain.run(docs)
            
                st.success(output_summary)
        
        except Exception as e:
            st.exception(f"Exception:{e}")
        except ValueError as ve:
            st.error("Transcripts are not available for this video.")