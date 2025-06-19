import asyncio
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.mcp import MCPTools, StdioServerParameters

def create_cross_reference_agent(mcp_tools):
    """Create and configure the Cross-Reference Verifier Agent"""
    return Agent(
        name="Cross-Reference Verifier",
        role="Verify claims against multiple authoritative sources",
        model=Gemini(id="gemini-2.0-flash"),
        tools=[mcp_tools, ReasoningTools(add_instructions=True)],
        instructions=[
            "For each claim, search multiple authoritative sources automatically",
            "Check news sites, fact-checkers, government sources, academic sources",
            "For media content, perform reverse image/video searches",
            "Find original sources vs secondary reporting when possible",
            "Document all sources and their credibility levels",
            "Look for consensus patterns across multiple reliable sources",
            "Pay special attention to recent updates or corrections",
            "Always include source URLs and publication dates"
        ],
        add_datetime_to_instructions=True,
        markdown=True
    )