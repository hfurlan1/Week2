# ==============================================================================
# 2025-26 NBA Season Dashboard — Thursday live demo (CEN 3352)
# ==============================================================================
# Instructor-led demo file for Week 2, Day Two. Every number in this file is
# real, verified 2025-26 NBA season data (Finals clincher: June 13, 2026) —
# see the sourcing note in the Season Snapshot tab's expander.
#
# This file exists to show all four layout tools working together, the way
# Tuesday's app.py showed the four content zones working together:
#   st.columns   — three metrics up top, then a 2:1 split for chart + table
#   st.tabs      — Scoring Leaders / The Final Four / Season Snapshot
#   st.sidebar   — champion, team count, Finals dates (stays put always)
#   st.expander  — full sourcing note, tucked away until someone wants it
#
# Run it:   streamlit run apptest.py
# ==============================================================================

import streamlit as st
import pandas as pd

st.set_page_config(page_title="2025-26 NBA Season Dashboard", page_icon="\U0001F3C0", layout="wide")

# ------------------------------------------------------------------------------
# DESIGN SYSTEM — "courtside" aesthetic
# ------------------------------------------------------------------------------
#   Background : #0D1B2A  (near-black hardwood navy — arena-at-night feel)
#   Accent     : #C9082A  (NBA red, used sparingly)
#   Card       : #13233A  (lighter navy for contrast panels)
#   Headers    : Georgia (serif — matches the rest of the course's slides)
#   Body       : system sans — legible at a glance across a room
# ------------------------------------------------------------------------------

NAVY = "#0D1B2A"
RED = "#C9082A"
CARD = "#13233A"
INK = "#F5F5F0"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {NAVY};
        }}
        h1, h2, h3 {{
            font-family: Georgia, serif !important;
            color: {INK} !important;
        }}
        p, li, span, .stMarkdown, .stCaption, label {{
            color: {INK} !important;
        }}
        [data-testid="stMetricValue"] {{
            color: {RED} !important;
        }}
        [data-testid="stMetricLabel"] {{
            color: {INK} !important;
        }}
        section[data-testid="stSidebar"] {{
            background-color: {CARD};
        }}
        .stTabs [data-baseweb="tab"] {{
            color: {INK};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# TOP OF THE PAGE — three st.metric columns
# ------------------------------------------------------------------------------
st.title("2025-26 NBA Season — Dashboard")
st.caption("Real, verified season data. Built entirely with columns, tabs, sidebar, and an expander.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Champion", value="New York Knicks", delta="3rd title")

with col2:
    st.metric(label="Scoring Leader", value="Doncic", delta="33.5 PPG")

with col3:
    st.metric(label="Finals Clincher", value="94–90", delta="Knicks, Game 5 at San Antonio")

st.divider()

# ------------------------------------------------------------------------------
# THREE TABS
# ------------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["Scoring Leaders", "The Final Four", "Season Snapshot"])

# --- Tab 1: Scoring Leaders ----------------------------------------------------
with tab1:
    st.subheader("Race for the Scoring Title")

    scorers = pd.DataFrame(
        {
            "Player": ["Doncic", "Gilgeous-Alexander", "Edwards", "Brown", "Maxey"],
            "Team": ["Lakers", "Thunder", "Timberwolves", "Celtics", "76ers"],
            "PPG": [33.5, 31.1, 28.8, 28.7, 28.3],
        }
    )

    chart_col, table_col = st.columns([2, 1])

    with chart_col:
        st.bar_chart(scorers.set_index("Player")["PPG"])

    with table_col:
        st.dataframe(scorers, hide_index=True, use_container_width=True)

    st.caption(
        "Doncic wins his first career scoring title, averaging 33.5 points per "
        "game in his first full season with the Lakers after the February 2025 trade."
    )

# --- Tab 2: The Final Four -----------------------------------------------------
with tab2:
    st.subheader("How the Podium Finished")

    podium = pd.DataFrame(
        {
            "Place": [1, 2, 3, 4],
            "Team": ["New York Knicks", "San Antonio Spurs", "Cleveland Cavaliers", "Oklahoma City Thunder"],
            "Result": [
                "Champion",
                "Runner-up",
                "Lost East Finals to Knicks, 4–0",
                "Lost West Finals to Spurs, 4–3",
            ],
        }
    )
    st.dataframe(podium, hide_index=True, use_container_width=True)

    st.caption(
        "The Knicks trailed by double digits in all four of their Finals wins "
        "— including a 29-point comeback in Game 4, the largest in NBA Finals "
        "history — to capture their first title since 1973."
    )

# --- Tab 3: Season Snapshot ------------------------------------------------------
with tab3:
    st.subheader("Key Facts")

    st.markdown(
        "- **30 teams**, 82-game regular season plus the Play-In Tournament\n"
        "- **Jalen Brunson** named Finals MVP, averaging 32.6 points per game in the Finals\n"
        "- Brunson's **45-point Game 5** ties Michael Jordan's record for most points on "
        "the road in a series-clinching Finals game\n"
        "- Finals clinched **June 13, 2026**, at Frost Bank Center, San Antonio"
    )

    with st.expander("Where this data came from"):
        st.markdown(
            "Compiled from NBA.com, ESPN, Basketball-Reference, and Wikipedia "
            "coverage of the 2025-26 NBA season and the 2026 NBA Finals, "
            "cross-checked against reporting published in June 2026 following "
            "the Knicks' championship-clinching win."
        )

# ------------------------------------------------------------------------------
# SIDEBAR — static context, stays visible on every tab
# ------------------------------------------------------------------------------
with st.sidebar:
    st.header("About This Season")
    st.markdown(
        "**Champion:** New York Knicks\n\n"
        "**Teams:** 30\n\n"
        "**Finals:** June 3–13, 2026"
    )
    st.caption("This panel doesn't change no matter which tab above is open — that's what st.sidebar is for.")
