import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.langchain_tool import LangchainTool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

import google.auth
import google.auth.transport.requests
import google.oauth2.id_token

# --- Setup Logging and Environment ---

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()

model_name = os.getenv("MODEL")

# --- Custom Tools ---

def add_prompt_to_state(
    tool_context: ToolContext, prompt: str
) -> dict[str, str]:
    """Saves the user's content and emotional goal to the state."""
    tool_context.state["PROMPT"] = prompt
    logging.info(f"[State updated] Added to PROMPT: {prompt}")
    return {"status": "success"}

# Configuring the Wikipedia Tool for general emotional resonance knowledge
wikipedia_tool = LangchainTool(
    tool=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
)

# --- Agent Definitions ---

# 1. Emotional Resonance Analyzer Agent
comprehensive_researcher = Agent(
    name="emotional_resonance_analyzer",
    model=model_name,
    description="The primary analyzer that examines content and gathers emotional resonance insights.",
    instruction="""
    You are an expert in Emotional Intelligence and Content Psychology. Your goal is to fully analyze the user's PROMPT regarding emotional resonance in their content.
    You have access to two tools:
    1. A tool for researching emotional triggers and psychological principles from Wikipedia.
    2. A tool for analyzing emotional patterns and resonance techniques.

    First, analyze the user's PROMPT which contains both the content to analyze and the target emotion.
    - If the prompt requires general emotional psychology knowledge, use Wikipedia to gather information about emotional triggers.
    - If the prompt requires analysis of emotional resonance techniques, use both tools to gather comprehensive information.
    - Synthesize the results from the tool(s) you use into preliminary emotional resonance analysis.

    PROMPT:
    { PROMPT }
    """,
    tools=[
        wikipedia_tool
    ],
    output_key="research_data" # Stores findings for the next agent
)

# 2. Emotional Resonance Formatter Agent
response_formatter = Agent(
    name="emotional_resonance_formatter",
    model=model_name,
    description="Synthesizes emotional analysis into a comprehensive content optimization report.",
    instruction="""
    You are the voice of the Emotional Resonance Optimization Center. Your task is to take the
    RESEARCH_DATA and present it to the user as a complete emotional resonance analysis and optimization guide.

    - First, present the analysis of the current emotional resonance in the user's content.
    - Then, provide specific recommendations for enhancing the desired emotional response.
    - Include psychological principles and emotional triggers that would be most effective.
    - If some information is missing, provide the best recommendations based on available data.
    - Use a professional, supportive, and actionable tone.

    RESEARCH_DATA:
    { research_data }
    """
)

# --- Workflow Setup ---

emotional_resonance_workflow = SequentialAgent(
    name="emotional_resonance_workflow",
    description="The main workflow for handling a user's request about content emotional optimization.",
    sub_agents=[
        comprehensive_researcher, # Step 1: Gather emotional analysis data
        response_formatter,       # Step 2: Format the optimization report
    ]
)

root_agent = Agent(
    name="emotional_resonance_greeter",
    model=model_name,
    description="The main entry point for the Emotional Resonance Optimization System.",
    instruction="""
    - Welcome the user to the Emotional Resonance Optimization Bureau.
    - Let the user know you can help them analyze and optimize content for specific emotional responses (empathy, excitement, trust, urgency, curiosity, inspiration, nostalgia, humor, serenity, anticipation).
    - When the user responds with their content and target emotion, use the 'add_prompt_to_state' tool to save their response.
    - After using the tool, transfer control to the 'emotional_resonance_workflow' agent.
    """,
    tools=[add_prompt_to_state],
    sub_agents=[emotional_resonance_workflow]
)