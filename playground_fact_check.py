import asyncio
import nest_asyncio
from agno.agent import Agent
from agno.models.google import Gemini
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.mcp import MCPTools, StdioServerParameters
from agno.team.team import Team
import os
from dotenv import load_dotenv

load_dotenv()
nest_asyncio.apply()

agent_storage_file: str = "tmp/fact_check_agents.db"

async def run_playground_server():
    """Run the fact-checking team in playground"""
    
    # Setup MCP tools
    server_params = StdioServerParameters(
        command="npx",
        args=["@brightdata/mcp"],
        env={
            "API_TOKEN": os.getenv("BRIGHT_DATA_API_KEY"),
            "WEB_UNLOCKER_ZONE": "unblocker",
            "BROWSER_ZONE": "scraping_browser"
        }
    )
    
    async with MCPTools(server_params=server_params, timeout_seconds=120) as mcp_tools:
        # Import agent creation functions
        from agents.content_extractor import create_content_extractor_agent_sync
        from agents.claim_identifier import create_claim_identifier_agent
        from agents.cross_reference import create_cross_reference_agent
        from agents.verdict_agent import create_verdict_agent
        
        # Create agents
        content_extractor = create_content_extractor_agent_sync(mcp_tools)
        claim_identifier = create_claim_identifier_agent()
        cross_reference = create_cross_reference_agent(mcp_tools)
        verdict_agent = create_verdict_agent()
        
        fact_check_team = Team(
            name="Social Media Fact Check Team",
            mode="coordinate",
            model=Gemini(id="gemini-2.0-flash"),
            members=[content_extractor, claim_identifier, cross_reference, verdict_agent],
            instructions=[
            "When delegating tasks, always pass the full context including URLs and previous findings to each agent",
            "Work together to comprehensively fact-check social media posts",
            "IMPORTANT: Your final response must include:",
            "1. A detailed summary of the post content (what was shown, said, or claimed)",
            "2. List of all specific claims identified in the post",
            "3. Verification results for each claim with sources and dates",
            "4. Citations with links to authoritative sources",
            "5. Context about why the claims are true/false/misleading",
            "6. Overall verdict with confidence level",
            "Present findings in a structured, easy-to-read format with clear sections",
            "Use markdown formatting with headers, bullet points, and bold text for clarity",
            "Always show the complete fact-checking process transparently"
        ],
            show_members_responses=True,
            enable_agentic_context=True,
            add_datetime_to_instructions=True,
            success_criteria="""Complete fact-check with:
            - Extracted post content with full details
            - All claims clearly identified and numbered
            - Cross-referenced sources with dates and links
            - Evidence-based verdict with confidence score
            - Structured report using markdown headers and formatting
            - Citations in format: [1] Source Name (Date) - URL""",
            markdown=True,
            storage=SqliteAgentStorage(
                table_name="fact_check_team",
                db_file=agent_storage_file,
                auto_upgrade_schema=True
            )
        )

        playground = Playground(teams=[fact_check_team])
        app = playground.get_app()
        
        serve_playground_app(app, port=7777)

if __name__ == "__main__":
    asyncio.run(run_playground_server())