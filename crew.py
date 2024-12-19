


from crewai import Crew,Process
from agents import news_researcher,news_writer
from tasks import research_task, write_task
#

crew = Crew(


  agents=[news_researcher,news_writer],

  tasks=[research_task,write_task],

  process=Process.sequential,



)


## starting  the task execution process with enhanced feedback 

result = crew.kickoff(inputs={"topic":"Global Warfare & geopolitcs"})

print(result)

