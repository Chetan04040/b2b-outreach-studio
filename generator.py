import os
from typing import Any, Dict, Optional
from knowledge import INDUSTRY_KNOWLEDGE_BASE


class OutreachGenerator:
    """Generates multi-channel B2B sales outreach sequences and objection battlecards."""

    def __init__(self, api_key: Optional[str] = None, provider: str = "groq"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
        self.provider = provider

    def generate(
        self,
        company_name: str,
        industry: str,
        target_persona: str,
        tone: str,
        scraped_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate multi-channel sequence based on scraped context and vertical intelligence."""
        industry_info = INDUSTRY_KNOWLEDGE_BASE.get(
            industry,
            INDUSTRY_KNOWLEDGE_BASE["E-Commerce & Retail"],
        )

        title = scraped_data.get("title", "")
        meta = scraped_data.get("meta_description", "")
        snippet = scraped_data.get("content_snippet", "")

        # Try live LLM call if API key exists
        if self.api_key:
            try:
                return self._call_llm(
                    company_name, industry, target_persona, tone, industry_info, title, meta, snippet
                )
            except Exception as e:
                # Fall back to heuristic engine if API fails
                pass

        return self._generate_heuristic(
            company_name, industry, target_persona, tone, industry_info, title, meta, snippet
        )

    def _call_llm(
        self,
        company_name: str,
        industry: str,
        target_persona: str,
        tone: str,
        info: Dict[str, Any],
        title: str,
        meta: str,
        snippet: str,
    ) -> Dict[str, Any]:
        """Call Groq or OpenAI chat completion."""
        import json
        from openai import OpenAI

        if self.provider == "groq":
            client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=self.api_key)
            model = "llama-3.1-70b-versatile"
        else:
            client = OpenAI(api_key=self.api_key)
            model = "gpt-4o-mini"

        system_prompt = (
            "You are an elite B2B Enterprise Solutions Consultant and SDR. "
            "Generate high-converting, concise, multi-channel outreach for conversational CX and messaging automation. "
            "Return valid JSON only matching the specified keys."
        )

        user_prompt = f"""
Target Company: {company_name}
Industry: {industry}
Target Persona: {target_persona}
Tone: {tone}
Context: {title} | {meta} | {snippet[:800]}
Industry Proof Point: {info['metric_proof']}
Key CX Friction: {info['cx_frictions'][0]}
Proposed Capability: {info['solution_capabilities'][0]}

Return a JSON object with EXACTLY these keys:
{{
  "identified_frictions": ["bullet 1", "bullet 2", "bullet 3"],
  "cold_email": {{
    "subject": "Compelling short subject",
    "body": "3-paragraph concise email with hook, value prop, and soft CTA"
  }},
  "linkedin_inmail": "Under 300 character message",
  "whatsapp_hook": {{
    "template_title": "Short title",
    "body_text": "Interactive WhatsApp template demonstrating customer experience",
    "call_to_action_buttons": ["Button 1", "Button 2"]
  }},
  "objection_battlecard": {{
    "anticipated_objection": "{info['primary_objection']}",
    "winning_rebuttal": "{info['objection_rebuttal']}"
  }}
}}
"""

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.7,
        )

        return json.loads(response.choices[0].message.content)

    def _generate_heuristic(
        self,
        company_name: str,
        industry: str,
        target_persona: str,
        tone: str,
        info: Dict[str, Any],
        title: str,
        meta: str,
        snippet: str,
    ) -> Dict[str, Any]:
        """Deterministic heuristic fallback providing professional, battle-tested templates."""
        clean_company = company_name.strip() or "your team"
        friction_1 = info["cx_frictions"][0]
        friction_2 = info["cx_frictions"][1]
        friction_3 = info["cx_frictions"][2]

        sol_1 = info["solution_capabilities"][0]
        sol_2 = info["solution_capabilities"][1]
        metric = info["metric_proof"]

        subject_line = f"Quick question regarding customer conversion at {clean_company}"
        if tone == "Direct":
            subject_line = f"Eliminating {industry.split('&')[0].strip()} funnel drop-offs for {clean_company}"
        elif tone == "Challenger":
            subject_line = f"Are manual touchpoints costing {clean_company} 30%+ of pipeline?"

        email_body = f"""Hi {target_persona.split()[-1] if target_persona != 'Founder / CEO' else 'Team'},

I was reviewing {clean_company}'s customer journey and noticed how quickly your team is scaling. However, across leading {industry.split('&')[0].strip()} enterprises, one silent bottleneck repeatedly surfaces: {friction_1.lower()}.

We recently helped enterprises in your space automate this using verified conversational CX channels—enabling {sol_1.lower()}. This delivered a validated **{metric}**.

Would you be open to a 5-minute conversation next Tuesday to see how {clean_company} could deploy a similar conversational workflow?

Best regards,
Chetan Rupchandani
Technical Solutions Consultant"""

        linkedin_msg = (
            f"Hi {target_persona.split()[-1]} - noticed {clean_company}'s impressive growth in {industry.split('&')[0].strip()}. "
            f"We recently helped peer enterprises solve {friction_1.lower()}, yielding {metric}. "
            f"Would love to connect and share a 2-minute architectural teardown."
        )

        whatsapp_sample = {
            "template_title": f"Interactive Customer Journey - {clean_company}",
            "body_text": (
                f"Hello {{1}}, thank you for choosing {clean_company}! 👋\n\n"
                f"Your request has been prioritized. To speed up your onboarding without waiting on a call, "
                f"please choose an action below:"
            ),
            "call_to_action_buttons": ["Track Status", "Schedule Call", "Talk to Specialist"],
        }

        return {
            "identified_frictions": [
                f"{friction_1} ({clean_company})",
                f"{friction_2} during peak customer hours",
                f"{friction_3}",
            ],
            "cold_email": {
                "subject": subject_line,
                "body": email_body,
            },
            "linkedin_inmail": linkedin_msg,
            "whatsapp_hook": whatsapp_sample,
            "objection_battlecard": {
                "anticipated_objection": info["primary_objection"],
                "winning_rebuttal": info["objection_rebuttal"],
            },
        }
