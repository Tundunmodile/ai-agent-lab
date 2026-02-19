from json import tool
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.tools import tool
from langchain.agents import create_agent
from datetime import datetime




@tool
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression provided as a string.

    Parameters:
    expression (str): The mathematical expression to evaluate.

    Returns:
    str: The result of the evaluation as a string.

    Note:
    This function uses eval() for demonstration purposes. Ensure inputs are sanitized
    in a production environment to avoid security risks.
    """
    try:
        result = eval(expression)  # Evaluate the expression
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@tool
def get_current_time() -> str:
    """
    Returns the current date and time as a formatted string.

    Returns:
    str: The current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def reverse_string(input_string: str) -> str:
    """
    Reverses a given string.

    Parameters:
    input_string (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    return input_string[::-1]

@tool
# Correctly define the weather tool without additional arguments
def weather_tool(date: str) -> str:
    """
    Accepts a date parameter (formatted as 'YYYY-MM-DD') and returns weather information for the given date.

    Parameters:
    date (str): The date in the format "YYYY-MM-DD".

    Returns:
    str: Weather information for the given date.
    """
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        if date == today:
            return "Sunny, 72°F"
        else:
            return "Rainy, 55°F"
    except Exception as e:
        return f"Error: {str(e)}"

# Update tools array
    tools = [calculator, get_current_time, reverse_string, weather_tool]

def main() -> None:
    """
    Entry point for the Python LangChain AI Agent application.

    This function initializes the application, checks for required environment variables,
    and prints a startup message.
    """
    print("🚀 Starting the Python LangChain AI Agent...")

    # Check if GITHUB_TOKEN exists in environment variables
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("❌ Error: GITHUB_TOKEN not found in environment variables.")
        print("💡 Please create a .env file and add your GitHub token as follows:")
        print("   GITHUB_TOKEN=your_personal_access_token")
        return  # Exit early if the token is not found

    print("✅ GITHUB_TOKEN loaded successfully!")

    # Create a ChatOpenAI instance
    chat = ChatOpenAI(
        model="openai/gpt-4o",
        temperature=0,  # Deterministic responses
        base_url="https://models.github.ai/inference",
        api_key=github_token  # Use the GITHUB_TOKEN from environment variables
    )

    print("🤖 ChatOpenAI instance created successfully!")

    system_msg = SystemMessage(content="You are a helpful assistant that can perform various tasks using tools. Use the tools when necessary to provide accurate and concise answers.")

    # Define tools
    tools = [calculator, get_current_time, reverse_string, weather_tool]

    # Create an agent executor
    agent_executor = create_agent(
        chat,
        tools=tools,
        name='shege_agent',
        #debug=True,
        #system_prompt="Act as a professional and succinct AI assistant. Provide concise and accurate responses."
    )

    # Define a list of test queries
    test_queries = [
        "What time is it right now?",
        "What is 25 * 4 + 10?",
        "Reverse the string 'Hello World'"
    ]

    print("Running example queries:\n")
    

    # Iterate through each query
    for query in test_queries:
        print("📝 Query:", query)
        print("─" * 50)
        try:
            result = agent_executor.invoke({
                "messages": [{"role": "user", "content": query}]
            })
            # Extract and print only the response content
            response_content = result['messages'][-1].content
            print("✅ Response:", response_content)
        except Exception as e:
            print("❌ Error while executing the query:", e)
        print("\n")  # Add spacing between queries

    print("🎉 Agent demo complete!")

  # Check today's weather
    today_date = datetime.now().strftime("%Y-%m-%d")
    print("Today's weather:", weather_tool.func(today_date))

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    main()

  