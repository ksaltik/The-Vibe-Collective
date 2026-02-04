from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import os
import json
from openai import OpenAI

router = APIRouter()

# Schema definitions based on the PRD
class Term(BaseModel):
    term: str
    definition: str
    user_insight: str

class Vibe(BaseModel):
    instruction: str
    context: str
    tags: List[str]

class AntiPattern(BaseModel):
    instruction: str
    reason: str

class VibePackSchema(BaseModel):
    title: str = Field(..., description="Suggest a concise Title")
    description: str = Field(..., description="A 1-sentence summary of what this pack achieves")
    terms: List[Term]
    vibes: List[Vibe]
    anti_patterns: List[AntiPattern]

class ExtractionRequest(BaseModel):
    raw_text: str

SYSTEM_PROMPT = """ROLE: Expert Technical Knowledge Engineer & System Prompt Architect.

GOAL:
Analyze the provided text (User Chat Logs, Notes, or Documentation) and extract a structured "Vibe Pack" that can be used to instruct an AI Agent in the future.

INPUT: Unstructured text (chat history, code snippets, messy notes).

OUTPUT SCHEMA (JSON):
{
  "title": "Suggest a concise Title (e.g., 'FastAPI Production Vibes')",
  "description": "A 1-sentence summary of what this pack achieves.",
  "terms": [
    {
      "term": "The technical term (e.g., 'Hydration')",
      "definition": "The technical explanation.",
      "user_insight": "The specific nuance or 'aha!' moment found in the text (e.g., 'It's just making HTML interactive')."
    }
  ],
  "vibes": [
    {
      "instruction": "Positive directive (e.g., 'Use Pydantic V2').",
      "context": "Why? (e.g., 'V1 is deprecated and slower').",
      "tags": ["Syntax", "Performance"]
    }
  ],
  "anti_patterns": [
    {
      "instruction": "Negative constraint (e.g., 'Do NOT use generic try/except').",
      "reason": "Why? (e.g., 'It hides critical DB connection errors')."
    }
  ]
}

RULES FOR EXTRACTION:
1. IGNORE NOISE: Remove conversational filler ("Hello", "Thanks", "Can you help me?").
2. PRIVACY FILTER: Strictly IGNORE any API keys, passwords, IP addresses, or personal names (Kenan, Sarah).
3. GENERALIZATION: If the text says "Fix the bug in my user_profile.ts file," generalize it to "Check TypeScript interfaces for null safety."
4. INSIGHT OVER FACT: Prioritize "how" and "why" over static code. We want the *logic*, not just the snippet.
5. TONE MATCHING: If the user prefers "Concise" answers, add a Vibe: "Keep responses under 200 words."
"""

@router.post("/extract", response_model=VibePackSchema)
async def extract_vibes(request: ExtractionRequest):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # Mock response for when API key is not present (Sandbox environment)
        # In a real scenario, this would raise an error or be handled differently.
        print("Warning: OPENAI_API_KEY not set. Returning mock data.")
        return VibePackSchema(
            title="Mock Vibe Pack",
            description="This is a mock response because OPENAI_API_KEY is missing.",
            terms=[
                Term(term="Mock Term", definition="A fake term.", user_insight="This is mocked.")
            ],
            vibes=[
                Vibe(instruction="Use mock data", context="API key missing", tags=["Mock", "Testing"])
            ],
            anti_patterns=[
                AntiPattern(instruction="Do not use real keys in sandbox", reason="Security")
            ]
        )

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-3.5-turbo" if 4o not available to user
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": request.raw_text}
            ],
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        if not content:
            raise HTTPException(status_code=500, detail="Empty response from AI")

        data = json.loads(content)
        return VibePackSchema(**data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
