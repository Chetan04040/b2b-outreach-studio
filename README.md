# B2B Multichannel Sales Outreach Studio

An AI-driven **Sales Prospecting, CX Friction Analysis & Multichannel Outreach Engine** built with Python, Streamlit, and modern LLMs.

Designed for enterprise **Business Development Associates (BDAs)** and **Technical Solutions Consultants (TSCs)** to accelerate account research, identify conversational customer touchpoint gaps, and generate high-converting, personalized outreach sequences in seconds.

---

## The Problem It Solves

Most outbound sales prospecting relies on generic, low-converting email blasts that ignore the prospect's actual customer journey. 

This studio automates the research-to-pitch workflow:
1. **Scrapes Target URL:** Extracts target company positioning, value proposition, and customer onboarding flow.
2. **Detects CX Frictions:** Pinpoints high-friction communication drop-offs (abandoned carts, slow lead qualification, cumbersome KYC document submission).
3. **Injects Validated Metrics:** Cross-references industry-specific proof points across BFSI, E-Commerce, Real Estate, EdTech, and Hospitality.
4. **Generates Multichannel Touches:** Crafts cold email, LinkedIn InMail (<300 chars), interactive WhatsApp template previews, and objection-handling battlecards.

---

## Key Features

- **Live Context Scraping:** Robust HTML/DOM parsing of headers, meta tags, and body copy using `BeautifulSoup`.
- **Vertical Knowledge Base:** Pre-configured with pain points, solutions, and validated ROI metrics across 5 major enterprise verticals.
- **Multichannel Copy Generator:**
  - **Cold Email:** Problem hook $\to$ Quantified enterprise proof point $\to$ Frictionless soft CTA.
  - **LinkedIn InMail:** Character-capped, high-response networking pitch.
  - **WhatsApp Journey Hook:** Interactive message mock demonstrating what the prospect's customers would see.
- **Objection Battlecard:** Automatically prepares the sales rep with the top anticipated buyer objection and winning rebuttal.
- **Dual-Mode Engine:** Works with live **Groq (Llama 3.1)** / **OpenAI (GPT-4o-mini)**, or runs instantaneously in **offline heuristic mode** without any API key.

---

## Architecture Flow

```
Prospect URL ──► [ WebScraper ] ──► Context Extraction (DOM / Headings)
                      │
                      ▼
Target Persona + Industry Vertical ──► [ Knowledge Base ] (CX Frictions & Metrics)
                      │
                      ▼
            [ OutreachGenerator ] (Groq / OpenAI / Heuristic Engine)
                      │
   ┌──────────────────┼──────────────────┬──────────────────┐
   ▼                  ▼                  ▼                  ▼
Cold Email       LinkedIn InMail   WhatsApp Hook     Objection Battlecard
```

---

## Quickstart

### 1. Clone & Setup Virtual Environment

```bash
git clone https://github.com/Chetan04040/b2b-outreach-studio.git
cd b2b-outreach-studio

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment (Optional)

```bash
cp .env.example .env
```
Add your `GROQ_API_KEY` or `OPENAI_API_KEY`, or leave blank to use the built-in heuristic engine.

### 3. Launch the Streamlit App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## License

Built and maintained by [Chetan Rupchandani](https://github.com/Chetan04040). Released under the [MIT License](LICENSE).
