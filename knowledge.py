from typing import Any, Dict

INDUSTRY_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    "E-Commerce & Retail": {
        "cx_frictions": [
            "High shopping cart abandonment on mobile web checkout",
            "Slow response times on post-purchase tracking inquiries",
            "Low email open rates (sub-15%) for promotional campaigns",
            "Customer drop-off during manual returns and exchange requests",
        ],
        "solution_capabilities": [
            "Automated abandoned cart recovery notifications via WhatsApp with 45%+ open rates",
            "Interactive product catalogs with 1-click in-chat checkout",
            "Real-time shipment tracking and automated delivery alerts",
            "24/7 automated return/exchange flow with automated label generation",
        ],
        "metric_proof": "4x higher conversion vs. email, 68% cart recovery rate within 2 hours",
        "primary_objection": "Meta conversation costs will eat into our e-commerce margins.",
        "objection_rebuttal": "By automating cart recovery and repeat orders, clients see a 12x ROI per conversation cost, recovering significantly more revenue than passive email reminders.",
    },
    "BFSI & FinTech": {
        "cx_frictions": [
            "Severe drop-offs during complex digital KYC and document submission",
            "Long wait times for loan eligibility and application status updates",
            "High operational costs for manual payment reminders and collections",
            "Security risks with unverified SMS channels for transactional alerts",
        ],
        "solution_capabilities": [
            "End-to-end encrypted document upload (PAN/Aadhaar/Pay slips) inside verified chat",
            "Instant AI-driven loan pre-qualification and credit card application bots",
            "Automated payment reminders with integrated 1-click payment links",
            "Meta-verified Green Tick channel establishing instant institutional trust",
        ],
        "metric_proof": "55% reduction in loan application turnaround time, 3.2x faster KYC completion",
        "primary_objection": "We have stringent compliance and data privacy regulations that prevent third-party messaging.",
        "objection_rebuttal": "Enterprise conversational platforms support bank-grade AES-256 encryption, ISO 27001/SOC-2 compliance, and on-prem or VPC deployments with zero customer data retention.",
    },
    "Real Estate & Construction": {
        "cx_frictions": [
            "Slow lead qualification leads to lost buyer interest within the first 15 minutes",
            "Sales teams wasting 60% of their time calling cold, unqualified web leads",
            "Difficulty coordinating weekend property site visits and follow-ups",
            "Low engagement on passive PDF brochures sent via email",
        ],
        "solution_capabilities": [
            "Instant conversational qualification: budget, location preference, and possession timeline",
            "Automated site visit scheduling integrated directly into sales team Google/Outlook calendars",
            "Interactive digital brochures and virtual 3D tour delivery over WhatsApp",
            "Automated milestone updates during construction and payment schedules",
        ],
        "metric_proof": "3.5x increase in qualified site visits, 80% of inquiries qualified in under 3 minutes",
        "primary_objection": "Real estate transactions are high-ticket and need human brokers, not chatbots.",
        "objection_rebuttal": "The AI bot doesn't close the deal—it filters out tyre-kickers and schedules pre-qualified, high-intent buyers directly into your brokers' calendars.",
    },
    "EdTech & Higher Education": {
        "cx_frictions": [
            "Massive drop-off between inquiry submission and counselor callback",
            "Counselors struggling to reach students during busy school/college hours",
            "Low attendance rates for webinars and demo lectures",
            "Tedious manual fee installment reminders",
        ],
        "solution_capabilities": [
            "Instant course recommendation chatbot qualifying student intent and budget",
            "Automated calendar booking for 1-on-1 counseling calls",
            "Interactive webinar reminders with 1-click join links (driving 70%+ attendance)",
            "Automated fee payment link reminders with instant receipt generation",
        ],
        "metric_proof": "2.8x higher demo lecture attendance, 40% reduction in lead acquisition cost",
        "primary_objection": "Students ignore automated messages and prefer talking directly to counselors.",
        "objection_rebuttal": "Students open 98% of WhatsApp messages within 3 minutes; conversational bots let them book their own counseling slot when convenient.",
    },
    "Travel & Hospitality": {
        "cx_frictions": [
            "Customer anxiety regarding flight delays, gate changes, and check-in times",
            "High call center overhead for basic booking modifications and cancellations",
            "Fragmented guest communication between booking engine and hotel front desk",
            "Missed opportunities for ancillary upsells (room upgrades, airport transfers)",
        ],
        "solution_capabilities": [
            "Real-time itinerary updates, mobile boarding passes, and booking confirmations",
            "Self-service cancellation and date change workflows handled via chat",
            "Personalized pre-arrival upsell campaigns (spa packages, dining reservations)",
            "Multi-lingual automated guest concierge for hotel amenities and local guides",
        ],
        "metric_proof": "65% reduction in support call volume, 22% uptake on ancillary travel upsells",
        "primary_objection": "Our existing booking engine already sends automated emails and SMS.",
        "objection_rebuttal": "SMS has zero interactivity and email open rates are declining, while rich conversational messaging lets travelers make instant modifications without app installation.",
    },
}
