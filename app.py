import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_core.tools import Tool
from datetime import datetime

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

    # Test query
    query = "What is 25 * 4 + 10?"
    response = chat.invoke([HumanMessage(content=query)])  # Wrap HumanMessage in a list

    # Print the response content
    print("🤔 Query:", query)
    print("💡 Response:", response.content)

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    main()