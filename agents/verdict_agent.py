from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.thinking import ThinkingTools
from agno.tools.reasoning import ReasoningTools


def create_verdict_agent():
    """Create and configure the Verdict Synthesizer Agent"""
    
    return Agent(
        name="Verdict Synthesizer",
        role="Analyze all evidence and deliver final fact-check verdict",
        model=Gemini(id="gemini-2.0-flash"),
        tools=[ThinkingTools(add_instructions=True), ReasoningTools(add_instructions=True)],
        instructions=[
            "Systematically review all extracted content, identified claims, and verification results",
            "Structure your response with these sections:",
            "## Post Summary - Describe what the post contained",
            "## Claims Identified - List each claim found",
            "## Verification Results - Detail findings for each claim with sources",
            "## Citations - Provide numbered list of all sources used",
            "## Context & Analysis - Explain why claims are true/false",
            "## Final Verdict - Clear verdict with confidence score (0-100%)",
            "Weigh source credibility, evidence quality, and consensus patterns",
            "Deliver clear verdict: TRUE/FALSE/MISLEADING/INSUFFICIENT_EVIDENCE",
            "Provide detailed reasoning chain and flag any uncertainties",
            "Consider social context and potential manipulation indicators",
            "Be conservative - if evidence is weak, say so clearly",
            "Include recommendations for readers on how to verify independently"
        ],
        add_datetime_to_instructions=True,
        markdown=True
    )