from crewai_tools import YoutubeChannelSearchTool
from crewai_tools import BaseTool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import os
# os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'),
    model="Llama 3.1 70B/8B",
    temperature=0.7)

embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

class CustomYoutubeSearchTool(BaseTool):
    def __init__(self, youtube_channel_handle, llm, embedding_model):
        self.youtube_channel_handle = youtube_channel_handle
        self.llm = llm
        self.embedding_model = embedding_model

    def _run(self, query: str) -> str:
        """
        Custom method to search YouTube channels using Hugging Face embeddings and Groq.
        """
        # Step 1: Generate a refined search query using Groq
        refined_query = self.llm.generate(f"Refine this search query for YouTube: {query}")

        # Step 2: Get embeddings for the refined query
        query_embedding = self.embedding_model.encode(refined_query)

        # Step 3: Simulate searching YouTube channels (replace this with actual YouTube API calls)
        # For demonstration, let's assume we have a list of pre-defined channel descriptions
        channel_descriptions = [
            "This channel focuses on AI and machine learning tutorials.",
            "A channel dedicated to Python programming and software development.",
            "Learn about data science and analytics in this channel.",
            "This channel covers robotics and automation technologies.",
            "A channel for beginners to learn about web development."
        ]

        # Step 4: Compute similarity between the query and channel descriptions
        from sentence_transformers import util
        similarities = []
        for desc in channel_descriptions:
            desc_embedding = self.embedding_model.encode(desc)
            similarity = util.cos_sim(query_embedding, desc_embedding).item()
            similarities.append(similarity)

        # Step 5: Sort channels by similarity and return top results
        import numpy as np
        sorted_indices = np.argsort(similarities)[::-1][:5]  # Top 5 results
        results = [channel_descriptions[i] for i in sorted_indices]

        return "\n".join(results)

# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06',
                                embedding_model=embedding,llm=llm)

