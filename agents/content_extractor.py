import asyncio
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.mcp import MCPTools, StdioServerParameters

def create_content_extractor_agent_sync(mcp_tools):
    """Create and configure the Content Extractor Agent with provided MCP tools"""
    return Agent(
        name="Content Extractor",
        role="Extract comprehensive data from social media posts",
        model=Gemini(id="gemini-2.0-flash"),
        tools=[mcp_tools],  # Use provided MCP tools
        instructions=[
            "You MUST use the available tools to extract data from social media posts",
            "For TikTok URLs: Use the web_data_tiktok_posts tool to get structured data",
            "For other platforms or if structured data fails: Use scrape_as_markdown tool",
            "ALWAYS call a tool - never try to extract data without using tools",
            "Extract: post text, media URLs, user info, engagement metrics, timestamps",
            "Return the raw tool output first, then summarize the key information"
        ],
        add_datetime_to_instructions=True,
        markdown=True
    )