{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import datetime as dt\
\
st.set_page_config(page_title="Sales Call Prep AI Agent", layout="wide")\
\
st.title("\uc0\u55357 \u56542  Sales Call Preparation \'96 AI Agent Demo")\
st.markdown(\
    "This demo simulates how an AI agent can analyze recent customer interactions "\
    "and generate a concise pre-call briefing, agenda, and recommendations."\
)\
\
# --- LEFT: INPUTS ------------------------------------------------------------\
st.header("\uc0\u55358 \u56830  Customer & Interaction Snapshot")\
\
col1, col2 = st.columns(2)\
\
with col1:\
    customer_name = st.text_input("Customer / Household Name", "John Doe")\
    segment = st.selectbox(\
        "Segment / Life Stage",\
        ["Mass Retail", "Affluent", "SME Owner", "Professional"],\
        index=1\
    )\
    last_contact_date = st.date_input(\
        "Last Contact Date",\
        value=dt.date.today() - dt.timedelta(days=45)\
    )\
    last_contact_channel = st.selectbox(\
        "Last Contact Channel",\
        ["Phone", "Branch Visit", "Video Meeting", "Email", "Chat"],\
        index=0\
    )\
    last_contact_topics = st.text_area(\
        "Key Topics from Last Call (comma\uc0\u8209 separated)",\
        "Mobile app login issue resolved, asked about home loan refinance, opened new savings account"\
    )\
\
with col2:\
    open_issues = st.text_area(\
        "Open Issues / Promises Made",\
        "RM to send updated fee schedule; customer waiting for rate quote on refinance"\
    )\
    new_activity = st.text_area(\
        "What changed since last contact?",\
        "Salary credited to account regularly; higher card spend on travel; no new complaints"\
    )\
    nbp_suggestions = st.multiselect(\
        "Existing Next Best Product Suggestions",\
        [\
            "High-yield savings / term deposit",\
            "Home loan refinance",\
            "Travel rewards credit card",\
            "Wealth management review"\
        ],\
        default=["High-yield savings / term deposit", "Home loan refinance"]\
    )\
    retention_flag = st.selectbox(\
        "Experience / Retention Flag",\
        ["None", "Recently dissatisfied", "At-risk: low engagement"],\
        index=0\
    )\
\
st.markdown("---")\
\
# --- RIGHT: AGENT OUTPUT -----------------------------------------------------\
st.header("\uc0\u55358 \u56598  AI Agent \'96 Pre\u8209 Call Briefing")\
\
if st.button("Generate Pre\uc0\u8209 Call Briefing", type="primary", use_container_width=True):\
\
    # Simple "reasoning" based on dates and flags\
    days_since_last = (dt.date.today() - last_contact_date).days\
    recency_label = (\
        "very recent" if days_since_last <= 14\
        else "recent" if days_since_last <= 45\
        else "stale"\
    )\
\
    # 1. Snapshot\
    st.subheader("1. Snapshot")\
    st.write(\
        f"- **Customer**: \{customer_name\} (\{segment\})  \\n"\
        f"- **Last contact**: \{days_since_last\} days ago via **\{last_contact_channel\}** "\
        f"(\{recency_label\})  \\n"\
        f"- **Last topics**: \{last_contact_topics\}"\
    )\
\
    # 2. Last 3 Contacts Summary (simple demo)\
    st.subheader("2. Last 3 Contacts (Illustrative)")\
    st.write(\
        "- Mobile app login issue \'96 resolved successfully.  \\n"\
        "- Inquiry about home loan refinance options.  \\n"\
        "- Follow\uc0\u8209 up on new savings account opening."\
    )\
\
    # 3. What Changed Since Last Contact\
    st.subheader("3. Changes Since Last Contact")\
    st.write(f"- \{new_activity\}")\
\
    # 4. Suggested Agenda & Talking Points\
    st.subheader("4. Suggested Agenda & Talking Points")\
\
    agenda_points = []\
\
    # Always follow up on open issues\
    if open_issues.strip():\
        agenda_points.append("Close the loop on open issues and promises:")\
        for line in open_issues.split(";"):\
            line = line.strip()\
            if line:\
                agenda_points.append(f"\'95 \{line\}")\
\
    # Use NBP suggestions\
    if nbp_suggestions:\
        agenda_points.append("Discuss product opportunities tailored to recent behavior:")\
        for prod in nbp_suggestions:\
            agenda_points.append(f"\'95 Explore \{prod\}")\
\
    # Retention / experience\
    if retention_flag != "None":\
        agenda_points.append(\
            "Address recent satisfaction/engagement concerns and agree on concrete next steps."\
        )\
\
    # Generic discovery questions\
    agenda_points.append("Ask 2\'963 discovery questions:")\
    agenda_points.append("\'95 Any upcoming large expenses or life events (education, travel, home)?")\
    agenda_points.append("\'95 Preferred channel and timing for future check\uc0\u8209 ins?")\
    agenda_points.append("\'95 How can the bank better support day\uc0\u8209 to\u8209 day money management?")\
\
    for item in agenda_points:\
        st.write(item)\
\
    # 5. Recommended Next Best Offers (simple rule-based for demo)\
    st.subheader("5. Recommended Offers for This Call")\
\
    offer_list = []\
    if "Home loan refinance" in nbp_suggestions:\
        offer_list.append("- Outline 2\'963 refinance scenarios (tenor, EMI, savings).")\
    if "High-yield savings / term deposit" in nbp_suggestions:\
        offer_list.append("- Propose moving surplus balances into high\uc0\u8209 yield savings or a short\u8209 term deposit.")\
    if "Travel rewards credit card" in nbp_suggestions or "travel" in new_activity.lower():\
        offer_list.append("- Position a travel rewards credit card aligned to current spend.")\
    if "Wealth management review" in nbp_suggestions:\
        offer_list.append("- Offer a dedicated wealth/financial planning review.")\
\
    if not offer_list:\
        offer_list.append("- Focus on service quality, then ask permission to share tailored offers in the next call.")\
\
    for o in offer_list:\
        st.write(o)\
\
    # 6. Post\uc0\u8209 Call Note Draft\
    st.subheader("6. Post\uc0\u8209 Call Note (Draft)")\
\
    draft_note = (\
        f"\{dt.date.today().isoformat()\} \'96 Spoke with \{customer_name\}. "\
        f"Reviewed progress on: \{open_issues or 'no outstanding items noted'\}. "\
        f"Discussed: \{', '.join(nbp_suggestions) if nbp_suggestions else 'service experience and future goals'\}. "\
        "Captured updated preferences and agreed next steps."\
    )\
    st.text_area("Editable Call Note", draft_note, height=120)\
\
else:\
    st.info("Fill in the customer snapshot on the left, then click **Generate Pre\uc0\u8209 Call Briefing**.")\
\
st.caption("Demo only \'96 uses simple rules to simulate an AI agent preparing sales calls.")\
}