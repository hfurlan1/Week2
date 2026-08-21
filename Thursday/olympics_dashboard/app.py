# ==============================================================================
# 2026 Winter Olympics Dashboard — Extra Thursday example (CEN 3352)
# ==============================================================================
# A second worked example showing all four layout tools together, same
# pattern as worldcup_dashboard/app.py. Every number here is real, official
# Milano Cortina 2026 data.
#
# Source: International Olympic Committee official results
# (olympics.com/en/milano-cortina-2026/medals), verified against AP and
# Reuters closing-ceremony coverage, February 22-23, 2026.
#
# Run it:   streamlit run app.py
# ==============================================================================

import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 Winter Olympics Dashboard", page_icon="\u2744\ufe0f", layout="wide")

# ------------------------------------------------------------------------------
# DESIGN SYSTEM — "alpine" aesthetic
# ------------------------------------------------------------------------------
SNOW = "#F4F7FA"     # background
ICE = "#2E5C8A"      # accent
CARD = "#E4ECF2"     # card panels
INK = "#1B2A38"       # body text

st.markdown(
    f"""
    <style>
        .stApp {{ background-color: {SNOW}; }}
        h1, h2, h3 {{ font-family: Georgia, serif !important; color: {INK} !important; }}
        p, li, span, .stMarkdown, .stCaption, label {{ color: {INK} !important; }}
        [data-testid="stMetricValue"] {{ color: {ICE} !important; }}
        section[data-testid="stSidebar"] {{ background-color: {CARD}; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# TOP OF THE PAGE — three st.metric columns
# ------------------------------------------------------------------------------
st.title("2026 Winter Olympics \u2014 Dashboard")
st.caption("Real, verified Milano Cortina 2026 results. Columns, tabs, sidebar, and an expander.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Top Nation", value="Norway", delta="18 golds")

with col2:
    st.metric(label="Total Medals (Norway)", value="41", delta="12 silver, 11 bronze")

with col3:
    st.metric(label="Nations Medaling", value="29", delta="of 92 competing")

st.divider()

# ------------------------------------------------------------------------------
# TABS
# ------------------------------------------------------------------------------
tab1, tab2 = st.tabs(["Medal Table", "Games Snapshot"])

with tab1:
    st.subheader("Top 5 Nations by Total Medals")

    medals = pd.DataFrame(
        {
            "Nation": ["Norway", "United States", "Italy", "Netherlands", "Germany"],
            "Gold": [18, 12, 10, 10, 8],
            "Silver": [12, 12, 6, 7, 10],
            "Bronze": [11, 9, 14, 3, 8],
            "Total": [41, 33, 30, 20, 26],
        }
    )

    chart_col, table_col = st.columns([2, 1])

    with chart_col:
        st.bar_chart(medals.set_index("Nation")["Total"])

    with table_col:
        st.dataframe(medals, hide_index=True, use_container_width=True)

    st.caption(
        "Norway topped the table for the fourth straight Winter Games, powered "
        "by cross-country skiing, biathlon, and ski jumping."
    )

with tab2:
    st.subheader("Key Facts")

    st.markdown(
        "- Held in **Milan and Cortina d'Ampezzo, Italy** \u2014 the first Winter "
        "Games split across two host cities in this way\n"
        "- **February 6\u201322, 2026** \u2014 116 events across 8 sports\n"
        "- **2,884 athletes** from **92 nations** competed\n"
        "- Team USA set a national record with 12 golds"
    )

    with st.expander("Where this data came from"):
        st.markdown(
            "Compiled from the IOC's official Milano Cortina 2026 results page "
            "(olympics.com), cross-checked against AP and Yahoo Sports coverage "
            "of the closing ceremony, February 22\u201323, 2026."
        )

# ------------------------------------------------------------------------------
# SIDEBAR — static context, stays visible on every tab
# ------------------------------------------------------------------------------
with st.sidebar:
    st.header("About These Games")
    st.markdown(
        "**Host cities:** Milan & Cortina d'Ampezzo, Italy\n\n"
        "**Dates:** February 6\u201322, 2026\n\n"
        "**Nations competing:** 92"
    )
    st.caption("This panel stays put no matter which tab above is open.")
