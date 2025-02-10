from crewai import Agent
from tools import yt_tool
from crewai import LLM
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import os
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'),
    model="Llama 3.1 70B/8B",
    temperature=0.7)


## Creating a blog content reasearch agent

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)
## creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)