# AI Agent Lab
# Python LangChain Agent

An educational demonstration of building AI agents with tool-calling capabilities using Python and LangChain. This project showcases how to create intelligent agents that can autonomously select and execute tools to answer complex queries.


## What is an AI Agent?

An AI agent is an autonomous system that uses a large language model (LLM) to reason about tasks and decide which tools to use to accomplish them. Unlike a simple chatbot that only generates text responses, an agent can:

- **Understand Intent**: Analyze what the user is asking for
- **Plan Actions**: Determine which tools are needed to fulfill the request
- **Execute Tools**: Call appropriate functions with correct parameters
- **Synthesize Results**: Combine tool outputs into a coherent response

## How This Agent Works

This implementation uses LangChain's agent framework with the following architecture:

### 1. **LLM Core (ChatOpenAI)**
The agent uses OpenAI's GPT-4 model accessed through GitHub Models. The LLM serves as the "brain" that:
- Interprets user queries
- Decides which tools to invoke
- Reasons about tool outputs
- Generates natural language responses

### 2. **Tools (Python Functions)**
Tools are Python functions that extend the agent's capabilities beyond text generation. Each tool:
- Has a clear name and description that the LLM uses to understand when to call it
- Accepts string input (as required by LangChain's Tool interface)
- Returns string output
- Performs a specific, deterministic task

Example tools in this project:
- **Calculator**: Evaluates mathematical expressions using Python's eval()
- **get_current_time**: Returns the current system date and time
- **reverse_string**: Reverses a string using Python slice notation

### 3. **Agent Orchestration**
The `create_agent()` function from LangChain creates an agent executor that:
- Receives user input
- Analyzes which tools (if any) are needed
- Invokes tools in the correct sequence
- Passes tool outputs back to the LLM
- Generates a final response

The agent can chain multiple tool calls together. For example, to answer "What's the weather like today?", it might:
1. Call `get_current_time()` to get today's date
2. Call `get_weather(date)` with that date
3. Synthesize a natural language response

## Key Concepts

### Tool Definitions
Tools in LangChain are defined using the `Tool` class from `langchain.tools`. Each tool consists of:

```python
@tool
def my_function(input: str) -> str:
    """Docstring describing what the tool does.
    
    This description helps the LLM understand when to use this tool.
    """
    # Tool implementation
    return result

Tool(my_function)
```

The **description** is critical—it tells the LLM when and how to use the tool. Write clear, specific descriptions that explain:
- What the tool does
- What input format it expects
- What output it returns

### Agent Decision Making
With verbose/debug mode enabled, you can observe the agent's reasoning process:
1. **Thought**: What should I do to answer this query?
2. **Action**: I will use the [tool_name] tool
3. **Action Input**: [parameters to pass]
4. **Observation**: [tool output]
5. **Final Answer**: [synthesized response to user]

This chain-of-thought reasoning is what makes agents powerful—they can break down complex tasks and solve them step by step.

### Why Use Tools?
LLMs alone have limitations:
- **No real-time data**: Cannot access current time, weather, or live information
- **Calculation errors**: May make arithmetic mistakes
- **No side effects**: Cannot interact with files, databases, or APIs
- **Hallucination**: May confidently provide incorrect information

Tools solve these problems by providing:
- **Deterministic operations**: Calculations are always correct
- **Real-world access**: Can read system time, call APIs, etc.
- **Reliability**: Facts come from authoritative sources, not LLM memory

## Project Structure

- **app.py**: Main application with agent configuration and tool definitions
- **requirements.txt**: Python dependencies (LangChain, OpenAI integration, dotenv)
- **INSTRUCTIONS.md**: Complete lab exercises and learning guide
- **.env**: Environment configuration (GitHub token for API access)

## Technologies Used

- **Python 3.9+**: Modern Python with type hints and async support
- **LangChain**: Framework for building LLM-powered applications with agents and tools
- **langchain-openai**: OpenAI model integration for LangChain
- **GitHub Models**: Free access to OpenAI's GPT-4 models through GitHub
- **python-dotenv**: Environment variable management

## Learning Objectives

By working through this project, you'll learn:
- How AI agents differ from simple chatbots
- How to create and register tools for LangChain agents
- How the LLM decides which tools to use based on descriptions
- How to chain multiple tool calls to solve complex problems
- Best practices for tool design and error handling
- The architecture of autonomous AI systems

## Extension Ideas

Once you understand the basics, consider:
- Adding tools for file I/O, web scraping, or API calls
- Implementing conversation memory to maintain context
- Adding logging and performance monitoring
- Securing the calculator tool (replacing eval() with safer alternatives)
- Building a multi-agent system with specialized agents
- Adding streaming responses for real-time feedback

## Additional Resources

- **LangChain Documentation**: https://python.langchain.com/
- **GitHub Models**: https://github.com/marketplace/models
- **Python Official Docs**: https://docs.python.org/3/
