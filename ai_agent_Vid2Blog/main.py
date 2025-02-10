from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task

from dotenv import load_dotenv
load_dotenv()

import os
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# llm = LLM(
#     model="Llama 3.1 70B/8B",
#     temperature=0.7
# )


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True,
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
print(result)