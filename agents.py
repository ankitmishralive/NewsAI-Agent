

from crewai import Agent , LLM


from tools import tool 

from dotenv import load_dotenv
import os 

load_dotenv()
from litellm import completion

# from langchain_google_genai import ChatGoogleGenerativeAI

llm = LLM(model="groq/gemma2-9b-it")

# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))


## Senior Research Agent 

news_researcher = Agent(
        role = "Senior Researcher",
        goal = "Uncover ground breaking technologies in {topic}",
        verbose = True, 
        memory = True, 
        backstory= (
        "Driven by Curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could  change"
        "the world"
            ),

        tools = [tool],
            llm = llm,

        allow_delegation=True, # I want this agent to communicate with other agents

)





news_writer = Agent(

    role = "News Writer",
    goal = "Write a news article on {topic}",
    verbose=True,
    memory=True,
    backstory= (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
            ),

    tools = [tool],
    llm=llm,
    allow_delegation=False,


)


