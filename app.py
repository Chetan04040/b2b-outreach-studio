import json
import streamlit as st

from generator import OutreachGenerator
from knowledge import INDUSTRY_KNOWLEDGE_BASE
from scraper import WebScraper

st.set_page_config(
    page_title="B2B Multichannel Sales Outreach Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 8px;
        padding: 16px;
        border: 1px solid #E2E8F0;
        margin-bottom: 12px;
    }
    .badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
        background-color: #E0F2FE;
        color: #0369A1;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Target Persona & Settings")
    target_persona = st.selectbox(
        "Target Persona",
        [
            "VP of Growth / Demand Gen",
            "Head of Customer Experience (CX)",
            "Chief Marketing Officer (CMO)",
            "Chief Technology Officer (CTO)",
            "Founder / CEO",
        ],
    )

    tone = st.selectbox(
        "Outreach Tone",
        ["Consultative & Value-Led", "Challenger & Insight-Driven", "Direct & Action-Oriented"],
    )

    st.markdown("---")
    st.subheader("LLM Configuration")
    provider = st.radio("Provider", ["Groq (Fast)", "OpenAI (GPT-4o-mini)"], index=0)
    api_key_input = st.text_input(
        "API Key (Optional)",
        type="password",
        help="Leave blank to use intelligent offline heuristic mode for instant generation.",
    )

    st.info("💡 **Pro-Tip**: If no API key is provided, the studio uses its deterministic heuristic engine.")

# Main Application Header
st.markdown('<div class="main-header">⚡ B2B Multichannel Sales Outreach Studio</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">AI-Powered Prospect Intelligence, CX Friction Extraction & Multi-Touch Outreach Sequencing</div>',
    unsafe_allow_html=True,
)

# Input Row
col1, col2 = st.columns([2, 1])

with col1:
    company_url = st.text_input(
        "Target Company Website URL",
        placeholder="e.g. stripe.com or https://nykaa.com",
        help="The engine fetches live metadata and customer journey copy.",
    )

with col2:
    industry = st.selectbox("Target Industry Vertical", list(INDUSTRY_KNOWLEDGE_BASE.keys()))

company_name_manual = st.text_input(
    "Target Company Name (Optional override)",
    placeholder="Leave blank to auto-detect from website",
)

generate_btn = st.button("🚀 Analyze & Generate Sequence", type="primary", use_container_width=True)

if generate_btn:
    if not company_url and not company_name_manual:
        st.error("Please enter a target company URL or company name.")
    else:
        with st.spinner("Analyzing target company digital presence and conversational friction points..."):
            scraped = {"title": "", "meta_description": "", "content_snippet": "", "success": False}
            if company_url:
                scraped = WebScraper.scrape_url(company_url)

            # Detect company name
            detected_company = company_name_manual.strip()
            if not detected_company:
                if scraped.get("title"):
                    detected_company = scraped["title"].split("-")[0].split("|")[0].strip()
                elif company_url:
                    detected_company = (
                        company_url.replace("https://", "").replace("http://", "").split("/")[0].split(".")[0].capitalize()
                    )
                else:
                    detected_company = "Target Enterprise"

            provider_name = "groq" if "Groq" in provider else "openai"
            generator = OutreachGenerator(api_key=api_key_input.strip() or None, provider=provider_name)
            result = generator.generate(detected_company, industry, target_persona, tone, scraped)

            # Store in session state
            st.session_state["result"] = result
            st.session_state["company"] = detected_company
            st.session_state["industry"] = industry
            st.session_state["scraped"] = scraped

# Display Results
if "result" in st.session_state:
    res = st.session_state["result"]
    comp = st.session_state["company"]
    ind = st.session_state["industry"]
    scraped = st.session_state.get("scraped", {})

    st.success(f"Analysis completed for **{comp}** ({ind})")

    # CX Friction Points Summary
    st.subheader("🔍 Identified CX & Conversational Friction Points")
    cols = st.columns(3)
    frictions = res.get("identified_frictions", [])
    for idx, f in enumerate(frictions[:3]):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="metric-card">
                    <span class="badge">Friction {idx+1}</span>
                    <p style="margin-top: 8px; font-weight: 500;">{f}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")

    # Multichannel Sequence Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📧 Cold Email",
            "💼 LinkedIn InMail",
            "💬 WhatsApp Journey Hook",
            "🛡️ Objection Battlecard",
            "📦 Raw JSON & Export",
        ]
    )

    with tab1:
        email = res.get("cold_email", {})
        st.markdown(f"**Subject:** `{email.get('subject', '')}`")
        st.text_area("Email Copy", email.get("body", ""), height=240)
        st.caption("Structured with: Hook $\\to$ Validated Industry Proof Point $\\to$ Frictionless Soft CTA.")

    with tab2:
        inmail = res.get("linkedin_inmail", "")
        st.text_area("LinkedIn Message (< 300 Characters)", inmail, height=120)
        st.caption(f"Character count: {len(inmail)} / 300")

    with tab3:
        wa = res.get("whatsapp_hook", {})
        st.markdown(f"**Template Concept:** {wa.get('template_title', 'Interactive Notification')}")
        st.info(wa.get("body_text", ""))
        st.markdown("**Interactive Action Buttons:**")
        b_cols = st.columns(3)
        for i, btn in enumerate(wa.get("call_to_action_buttons", [])):
            with b_cols[i]:
                st.button(f"🔘 {btn}", key=f"wa_btn_{i}", disabled=True)

    with tab4:
        battlecard = res.get("objection_battlecard", {})
        st.markdown(f"### ⚠️ Anticipated Objection:\n> *\"{battlecard.get('anticipated_objection')}\"*")
        st.markdown(f"### 🎯 Winning BDA/Solutions Rebuttal:\n{battlecard.get('winning_rebuttal')}")

    with tab5:
        st.json(res)
        json_str = json.dumps(res, indent=2)
        st.download_button(
            label="📥 Download Sequence as JSON",
            data=json_str,
            file_name=f"{comp.lower().replace(' ', '_')}_outreach_sequence.json",
            mime="application/json",
        )
