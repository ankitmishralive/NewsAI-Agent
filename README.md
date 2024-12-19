# NewsScribe AI

An intelligent content creation system that uses AI agents to research current events from the web and craft comprehensive news articles. Built with CrewAI, it specializes in producing detailed coverage of Input Topic through automated research and writing.

## Architecture

The system employs a two-stage process where specialized AI agents handle web research and content writing sequentially.

```mermaid
flowchart TB
    subgraph Input
        topic["user input topic"]
    end

    subgraph CrewAI["CrewAI Framework"]
        direction TB
        crew["Crew Instance"]
        
        subgraph Agents
            researcher["News Researcher Agent"]
            writer["News Writer Agent"]
        end
        
        subgraph Tasks
            research["Research Task"]
            writing["Write Task"]
        end

        subgraph Process
            sequential["Sequential Process"]
        end
    end

    subgraph Output
        result["Final News Content"]
    end

    %% Connections
    topic --> crew
    crew --> Agents
    crew --> Tasks
    crew --> Process
    
    researcher --> research
    writer --> writing
    
    research --> sequential
    writing --> sequential
    
    sequential --> result
    
    %% Styling
    classDef primary fill:#2563eb,stroke:#1e40af,color:white
    classDef secondary fill:#4b5563,stroke:#374151,color:white
    classDef highlight fill:#059669,stroke:#047857,color:white
    
    class crew,sequential primary
    class researcher,writer,research,writing secondary
    class topic,result highlight
```

##  Features

- **Web Research Automation**: Gathers information from diverse online sources
- **Content Creation**: Transforms research findings into well-structured articles
- **Sequential Processing**: Ensures thorough research before writing begins
- **Topic Specialization**: Focused on global warfare and geopolitical news
- **Source Integration**: Combines information from multiple reliable sources

## Getting Started

### Prerequisites

```bash
pip install crewai
```

### Basic Usage

```python
from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# Initialize the crew
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Execute the workflow
result = crew.kickoff(inputs={"topic": "Global Warfare & geopolitics"})
print(result)
```



##  Components

### Agents

1. **News Researcher Agent**
   - Scrapes and collects information from the web
   - Validates source credibility
   - Organizes research findings

2. **News Writer Agent**
   - Creates original content from research
   - Structures articles professionally
   - Maintains journalistic style

### Tasks

1. **Research Task**
   - Web scraping and data collection
   - Source verification
   - Information synthesis

2. **Write Task**
   - Content creation
   - Article structuring
   - Final formatting


##  Acknowledgments

- [CrewAI Framework](https://github.com/joaomdmoura/crewAI)
- Contributors and maintainers
- Open source community

##  Contact

Ankit Mishra - [@ankitmishralive](https://twitter.com/ankitmishralive)
