# ==============================================================================
# 2026 World Cup Dashboard — Thursday live demo (CEN 3352)
# ==============================================================================
# Instructor-led demo file for Week 2, Day Two. Every number in this file is
# real, verified 2026 FIFA World Cup data (final: July 19, 2026) — see the
# sourcing note in the Tournament Snapshot tab's expander.
#
# This file exists to show all four layout tools working together, the way
# Tuesday's app.py showed the four content zones working together:
#   st.columns   — three metrics up top, then a 2:1 split for chart + table
#   st.tabs      — Golden Boot / The Final Four / Tournament Snapshot
#   st.sidebar   — host nations, team count, final date (stays put always)
#   st.expander  — full sourcing note, tucked away until someone wants it
#
# Run it:   streamlit run app.py
# ==============================================================================

import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 World Cup Dashboard", page_icon="\U0001F3C6", layout="wide")

# ------------------------------------------------------------------------------
# DESIGN SYSTEM — "match day" aesthetic
# ------------------------------------------------------------------------------
#   Background : #0B1F3A  (deep navy — night-match broadcast feel)
#   Accent     : #D4AF37  (trophy gold, used sparingly)
#   Card       : #142A4D  (lighter navy for contrast panels)
#   Headers    : Georgia (serif — matches the rest of the course's slides)
#   Body       : system sans — legible at a glance across a room
# ------------------------------------------------------------------------------

NAVY = "#0B1F3A"
GOLD = "#D4AF37"
CARD = "#142A4D"
INK = "#F2EDE4"

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
            color: {GOLD} !important;
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
st.title("2026 FIFA World Cup — Dashboard")
st.caption("Real, verified tournament data. Built entirely with columns, tabs, sidebar, and an expander.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Champion", value="Spain", delta="2nd title")

with col2:
    st.metric(label="Golden Boot", value="Mbapp\u00e9", delta="10 goals")

with col3:
    st.metric(label="Final Score", value="1\u20130", delta="Spain, after extra time")

st.divider()

# ------------------------------------------------------------------------------
# THREE TABS
# ------------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["Golden Boot", "The Final Four", "Tournament Snapshot"])

# --- Tab 1: Golden Boot -------------------------------------------------------
with tab1:
    st.subheader("Race for the Golden Boot")

    scorers = pd.DataFrame(
        {
            "Player": ["Mbapp\u00e9", "Messi", "Haaland", "Bellingham", "Kane"],
            "Country": ["France", "Argentina", "Norway", "England", "England"],
            "Goals": [10, 8, 7, 7, 6],
        }
    )

    chart_col, table_col = st.columns([2, 1])

    with chart_col:
        st.bar_chart(scorers.set_index("Player")["Goals"])

    with table_col:
        st.dataframe(scorers, hide_index=True, use_container_width=True)

    st.caption(
        "Mbapp\u00e9 becomes the first player to win the Golden Boot twice "
        "(also 2022) and finishes as the World Cup's all-time top scorer with 22."
    )

# --- Tab 2: The Final Four -----------------------------------------------------
with tab2:
    st.subheader("How the Podium Finished")

    podium = pd.DataFrame(
        {
            "Place": [1, 2, 3, 4],
            "Team": ["Spain", "Argentina", "England", "France"],
            "Result": [
                "Champion",
                "Runner-up",
                "3rd (beat France 6\u20134 in the third-place play-off)",
                "4th (lost the semifinal to Spain, 2\u20130)",
            ],
        }
    )
    st.dataframe(podium, hide_index=True, use_container_width=True)

    st.caption(
        "Spain conceded only one goal in the entire tournament — a record for a champion — "
        "and enters the final unbeaten in 38 straight matches."
    )

# --- Tab 3: Tournament Snapshot -------------------------------------------------
with tab3:
    st.subheader("Key Facts")

    st.markdown(
        "- **48 teams**, the first expanded World Cup (up from 32 in 2022)\n"
        "- **3 host nations** for the first time in World Cup history\n"
        "- **16 host cities** across the United States, Mexico, and Canada\n"
        "- Final played at **MetLife Stadium**, East Rutherford, New Jersey"
    )

    with st.expander("Where this data came from"):
        st.markdown(
            "Compiled from FIFA's official 2026 World Cup results page "
            "(fifa.com), cross-checked against NPR, CBS News, and Sky Sports "
            "match reports published July 19\u201320, 2026, the days immediately "
            "following the final."
        )

# ------------------------------------------------------------------------------
# SIDEBAR — static context, stays visible on every tab
# ------------------------------------------------------------------------------
with st.sidebar:
    st.header("About This Tournament")
    st.markdown(
        "**Host nations:** United States, Mexico, Canada\n\n"
        "**Teams:** 48\n\n"
        "**Final:** July 19, 2026"
    )
    st.caption("This panel doesn't change no matter which tab above is open — that's what st.sidebar is for.")
