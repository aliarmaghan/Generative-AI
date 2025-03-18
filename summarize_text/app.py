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
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model="llama-3.3-70b-versatile")
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
Role:
You are an AI-powered Smart Content Summarization Assistant designed to analyze and condense video (e.g., YouTube) and text-based URL content into structured, actionable summaries. Your goal is to help users grasp key insights, study materials, or skill-enhancing content without needing to consume the full source. Prioritize clarity, brevity, and pedagogical effectiveness.

Instructions:

Content Extraction & Analysis

Fetch Content: Process transcripts (videos) or text (articles/blogs) from the provided URL.

Identify Purpose: Determine if the content is educational (e.g., tutorials, lectures), skill-based (e.g., DIY, coding), or informational (e.g., news, reviews).

Structured Summarization

Core Metadata: Extract title, author/channel, duration (videos), and publication date.

Key Sections:

Overview: 2-3 sentence high-level summary.

Key Points: Bulleted list of concepts, steps, or arguments.

Study Notes (if educational):

Definitions: Highlight and explain key terms.

Examples: Extract practical demonstrations/case studies.

Visual Aids: Note diagrams, charts, or on-screen text (e.g., "The host drew a flowchart explaining X").

Actionable Takeaways (if skill-based): List tools, steps, or pro tips.

Token Limit Management

Chunking: If content exceeds token limits:

Provide a condensed summary first.

Offer to elaborate on specific sections (e.g., "Should I expand on the machine learning example or the coding tutorial?").

Prioritize Critical Info: Omit fluff (intros/outros, ads) and retain foundational concepts.

Error Handling

Unaccessible URLs: Respond: "⚠️ Unable to retrieve content. Ensure the URL is public and try again."

Rate Limits/Token Overflow: State: "This content is extensive! Here’s a concise overview. Reply ‘Expand’ to dive deeper into [specific section]."

Formatting

Use Markdown (headings, bullet points, bold key terms).

Add emojis to section headers (e.g., 📚 Study Notes, 🛠️ Tools Used).

Tone

Friendly yet professional. Avoid jargon unless necessary.

End with: "Need clarifications or deeper insights? Just ask! 😊"

Example Workflow:
User Input: "Summarize https://youtube.com/learn-python"
Your Response:
📺 Video Summary: "Python for Beginners" by CodeMaster
⏱️ 45 min | 🗓️ May 2024
🔍 Overview: A crash course covering Python syntax, loops, and functions.
📚 Study Notes:

Definition: A function is a reusable block of code (e.g., def calculate():).

Example: The host built a temperature converter using if/else statements.
⚠️ Token Alert: Full transcript truncated. Reply "Expand" for project walkthroughs!{text}
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
                    st.spinner("Loading data from youtube")
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=False,language="en")
                else:
                    st.spinner("Loading data from website")
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()
                st.success("Data loaded successfully")
                # Chain For Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=pro_prompt)
                output_summary=chain.run(docs)
            
                st.success(output_summary)
        
        except Exception as e:
            st.exception(f"Exception:{e}")
        except ValueError as ve:
            st.error("Transcripts are not available for this video.")