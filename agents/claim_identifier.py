from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools

def create_claim_identifier_agent():
    """Create and configure the Claim Identifier Agent"""
    
    return Agent(
        name="Claim Identifier",
        role="Identify factual claims that can be verified",
        model=Gemini(id="gemini-2.0-flash"),
        tools=[ReasoningTools(add_instructions=True)],
        instructions=[
            "Parse extracted content to find specific, verifiable factual claims",
            "Ignore opinions, jokes, satire, and subjective statements",
            "Extract key facts: statistics, events, quotes, dates, locations",
            "Prioritize claims that are most important and checkable",
            "Rate each claim's significance and verifiability",
            "Focus on claims that could potentially mislead people if false",
            "Provide clear categorization of each identified claim"
        ],
        add_datetime_to_instructions=True,
        markdown=True
    )