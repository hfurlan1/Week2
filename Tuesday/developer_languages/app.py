# ==============================================================================
# "What Do Developers Actually Use?" — Extra Tuesday example (CEN 3352)
# ==============================================================================
# A second worked example in the "Say Something True" spirit: one page, one
# real chart, one honest claim. This one uses Stack Overflow's 2025 Developer
# Survey — the largest annual survey of working developers, 31,771 responses
# to this specific question.
#
# Source: Stack Overflow 2025 Developer Survey, "Most popular technologies"
# (survey.stackoverflow.co/2025/technology), All Respondents category.
#
# Run it:   streamlit run app.py
# ==============================================================================

import streamlit as st
import pandas as pd

st.set_page_config(page_title="What Do Developers Actually Use?", page_icon="\U0001F4BB", layout="centered")

# ------------------------------------------------------------------------------
# DESIGN SYSTEM
# ------------------------------------------------------------------------------
PAPER = "#F5F3EF"    # background
CODE = "#5C4B8A"     # accent
INK = "#2B2A33"      # body text

st.markdown(
    f"""
    <style>
        .stApp {{ background-color: {PAPER}; }}
        .block-container {{ max-width: 680px; padding-top: 3rem; }}
        h1, h2, h3 {{ font-family: Georgia, serif !important; color: {INK} !important; }}
        p, li, span, .stMarkdown, .stCaption {{ color: {INK} !important; }}
        [data-testid="stMetricValue"] {{ color: {CODE} !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("What Do Developers Actually Use?")
st.markdown(
    "One page, one real chart. You're learning Python in this course — "
    "here's exactly where it stands among working developers."
)
st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("The Real Numbers")

languages = pd.DataFrame(
    {
        "Language": ["JavaScript", "HTML/CSS", "SQL", "Python", "Bash/Shell"],
        "% of Developers": [66.0, 61.9, 58.6, 57.9, 48.7],
    }
)

st.bar_chart(languages.set_index("Language"))

python_pct = languages.loc[languages["Language"] == "Python", "% of Developers"].iloc[0]
st.metric(label="Python usage in 2025", value=f"{python_pct}%", delta="+7 points vs. 2024")

st.caption(
    "Source: Stack Overflow 2025 Developer Survey, 31,771 respondents to this "
    "question, published survey.stackoverflow.co/2025/technology."
)

st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("Why It Matters")
st.markdown(
    "Python jumped 7 percentage points in a single year \u2014 the largest "
    "one-year move of any top-5 language in the survey's history. Learning it "
    "first isn't a coincidence in this course; it's the language with the "
    "steepest growth curve among working developers right now."
)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Extra Example \u00b7 CEN 3352 \u00b7 Front-End Development and Design")
