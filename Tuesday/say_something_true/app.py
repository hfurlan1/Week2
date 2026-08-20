# ==============================================================================
# "Say Something True" — Week 2 starter (CEN 3352)
# ==============================================================================
# The assignment: build the smallest possible Streamlit app that says
# something true and interesting about a problem you care about.
#
# Rules for this one:
#   - No widgets yet. That's Week 3. This week is layout and honesty only.
#   - At least one chart or image.
#   - It has to be TRUE — a real fact, even a small one, not a placeholder.
#
# This file is filled in with a worked example so there's something to run
# and look at on day one. The example continues the commuter-parking problem
# used as a running example in Week 1's slides — swap it for your own
# problem and your own real numbers. Keep the structure; change the content.
#
# Run it:   streamlit run app.py
#
# 8 EDIT ZONES — this file is organized into the same 8 zones the Tuesday
# slides walk through. Ctrl+F "ZONE" to jump between them.
# ==============================================================================

import streamlit as st
import pandas as pd

# ------------------------------------------------------------------------------
# ZONE 1 — PAGE IDENTITY
# ------------------------------------------------------------------------------
# st.set_page_config() controls the browser tab: its title and its icon.
# It has to run once, and it has to run before anything else that draws to
# the page — that's a Streamlit rule, not a style choice.
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Say Something True", page_icon="✎", layout="centered")

# ------------------------------------------------------------------------------
# ZONE 2 — DESIGN TOKENS
# ------------------------------------------------------------------------------
# Name each color once, here, then reuse the name everywhere below. This is
# the same idea as a variable in any Python script — it just happens to hold
# a color instead of a number. Change MOSS on this one line and every accent
# in the app updates at once, instead of hunting through the file for every
# place "#5C7A5C" was typed by hand.
# ------------------------------------------------------------------------------
CREAM = "#F2EDE4"   # background
MOSS = "#5C7A5C"    # accent
INK = "#2B2B26"     # body text

# ------------------------------------------------------------------------------
# ZONE 3 — FONTS & THE CSS BLOCK  (the scariest-looking zone — see slide notes)
# ------------------------------------------------------------------------------
# DESIGN SYSTEM — "field notebook" aesthetic. Deliberately NOT the Streamlit
# default look. Cream background, one accent color, a serif/mono pairing
# instead of the default sans-serif. Every choice here should be something
# you could explain out loud if asked — that's the whole point of doing this
# instead of leaving Streamlit's defaults in place.
#
#   Background : #F2EDE4  (cream, not white — softer, feels like paper)
#   Accent     : #5C7A5C  (moss green, used sparingly, never as a wall of color)
#   Headers    : Libre Baskerville (serif — feels written, not generated)
#   Body       : IBM Plex Mono (monospace — feels like field notes / a log)
# ------------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap');

        .stApp {{
            background-color: {CREAM};
        }}
        .block-container {{
            max-width: 680px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }}
        h1, h2, h3 {{
            font-family: 'Libre Baskerville', serif !important;
            color: {INK} !important;
        }}
        p, li, span, .stMarkdown, .stCaption {{
            font-family: 'IBM Plex Mono', monospace !important;
            color: {INK} !important;
        }}
        .accent {{
            color: {MOSS};
            font-weight: 600;
        }}
        hr {{
            border: none;
            border-top: 1px solid {MOSS};
            opacity: 0.35;
            margin: 1.6rem 0;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# ZONE 4 — HEADLINE & INTRO
# ------------------------------------------------------------------------------
# Plain strings — no HTML needed here. st.title() is always the single
# biggest heading on the page, and Streamlit only lets you have one.
# ------------------------------------------------------------------------------
st.title("Something I Know Is True")

st.markdown(
    "One page. One honest claim about a problem I actually care about. "
    "No widgets — just layout, and something worth looking at."
)

st.markdown("<hr>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ZONE 5 — PROBLEM STATEMENT
# ------------------------------------------------------------------------------
# Your persona and problem statement from Week 1 go here. The
# <span class='accent'> wrapper is optional styling defined back in Zone 3 —
# it is not required for the assignment. Delete it and this still works.
# ------------------------------------------------------------------------------
st.subheader("The Problem")
st.markdown(
    "Commuter students plan their whole morning around a "
    "<span class='accent'>guess</span> about parking availability, "
    "because there's no way to check ahead of time.",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# ZONE 6 — YOUR REAL DATA
# ------------------------------------------------------------------------------
# A Python dictionary becomes a table with pd.DataFrame(). Each key becomes
# a column name; each list becomes that column's values, in order.
# set_index("Morning") tells the chart below "use this column as the labels
# along the bottom, not as data to plot" — without it, Streamlit would try
# to chart the day names as if they were numbers.
#
# Replace this block with your own real data. These five numbers are
# illustrative only — a made-up week of mornings, not a real parking study.
# The point is the shape of the app, not these specific numbers.
# ------------------------------------------------------------------------------
st.subheader("A Fact Worth Seeing")

commute_log = pd.DataFrame(
    {
        "Morning": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Minutes spent searching for parking": [4, 19, 7, 24, 11],
    }
)

# ------------------------------------------------------------------------------
# ZONE 7 — CHART TYPE
# ------------------------------------------------------------------------------
# st.bar_chart, st.line_chart, and st.area_chart all take the exact same
# input — a DataFrame with an index. Swapping one word swaps the whole
# story: bars compare discrete mornings, a line emphasizes the trend across
# the week, an area fills in the "how much" underneath. Try all three on
# the same commute_log and decide which one is honest about this data.
# ------------------------------------------------------------------------------
st.bar_chart(commute_log.set_index("Morning"))

st.caption(
    "Source: five mornings of my own commute, logged by hand. "
    "Illustrative only — replace with your own real numbers."
)

st.markdown("<hr>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ZONE 8 — CLOSING INSIGHT
# ------------------------------------------------------------------------------
# The "so what." Every app should end by answering this, not just stop
# after showing data. A chart without a takeaway asks the reader to do the
# interpreting themselves — this is where you do it for them.
# ------------------------------------------------------------------------------
st.subheader("Why It Matters")
st.markdown(
    "A 20-minute swing across one week isn't a rounding error — it's the "
    "difference between making an 8am class and missing the first ten minutes of it."
)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Week 2 · Say Something True · CEN 3352 · Front-End Development and Design")
