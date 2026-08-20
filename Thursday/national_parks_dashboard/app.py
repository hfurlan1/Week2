# ==============================================================================
# National Parks Visitation Dashboard — Extra Thursday example (CEN 3352)
# ==============================================================================
# A second worked example showing all four layout tools together, same
# pattern as worldcup_dashboard/app.py. Every number here is real, official
# National Park Service data for calendar year 2025.
#
# Source: National Park Service, "NPS Recorded More Than 323 Million
# Recreation Visits In 2025" (official press release, March 17, 2026),
# individual park figures from NPS Visitor Use Statistics.
#
# Run it:   streamlit run app.py
# ==============================================================================

import streamlit as st
import pandas as pd

st.set_page_config(page_title="National Parks Dashboard", page_icon="\U0001F3D4\ufe0f", layout="wide")

# ------------------------------------------------------------------------------
# DESIGN SYSTEM — "trailhead" aesthetic
# ------------------------------------------------------------------------------
BARK = "#F3F0E9"     # background
PINE = "#2F5233"     # accent
CARD = "#E7E1D2"     # card panels
INK = "#2B2620"       # body text

st.markdown(
    f"""
    <style>
        .stApp {{ background-color: {BARK}; }}
        h1, h2, h3 {{ font-family: Georgia, serif !important; color: {INK} !important; }}
        p, li, span, .stMarkdown, .stCaption, label {{ color: {INK} !important; }}
        [data-testid="stMetricValue"] {{ color: {PINE} !important; }}
        section[data-testid="stSidebar"] {{ background-color: {CARD}; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# TOP OF THE PAGE — three st.metric columns
# ------------------------------------------------------------------------------
st.title("National Parks \u2014 2025 Visitation Dashboard")
st.caption("Real, verified 2025 NPS data. Columns, tabs, sidebar, and an expander.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Most Visited Park", value="Great Smoky Mtns", delta="11.5M visits")

with col2:
    st.metric(label="Total System Visits", value="323M", delta="\u22122.7% vs. 2024")

with col3:
    st.metric(label="Parks Reporting", value="406", delta="of 433 NPS sites")

st.divider()

# ------------------------------------------------------------------------------
# TABS
# ------------------------------------------------------------------------------
tab1, tab2 = st.tabs(["Top 5 Parks", "Year in Review"])

with tab1:
    st.subheader("Most Visited National Parks, 2025")

    parks = pd.DataFrame(
        {
            "Park": ["Great Smoky Mountains", "Zion", "Yellowstone", "Grand Canyon", "Yosemite"],
            "State(s)": ["TN / NC", "UT", "WY / MT / ID", "AZ", "CA"],
            "2025 Visits": [11_527_939, 4_984_525, 4_762_988, 4_430_000, 4_278_413],
        }
    )

    chart_col, table_col = st.columns([2, 1])

    with chart_col:
        st.bar_chart(parks.set_index("Park")["2025 Visits"])

    with table_col:
        st.dataframe(parks, hide_index=True, width="stretch")

    st.caption(
        "Great Smoky Mountains drew more than double the visits of any other "
        "national park \u2014 partly because it charges no entrance fee."
    )

with tab2:
    st.subheader("Key Facts")

    st.markdown(
        "- **323,014,305** total recreation visits across the National Park System\n"
        "- Visits fell **2.7%** from 2024's record 331.9 million\n"
        "- **26 parks** set new all-time visitation records despite the drop\n"
        "- A **43-day government shutdown** (Oct\u2013Nov 2025) forced many sites "
        "to partially or fully close"
    )

    with st.expander("Where this data came from"):
        st.markdown(
            "Compiled from the National Park Service's official 2025 visitation "
            "press release (nps.gov, March 17, 2026) and individual park "
            "Visitor Use Statistics, cross-checked against National Parks "
            "Traveler's coverage of the same release."
        )

# ------------------------------------------------------------------------------
# SIDEBAR — static context, stays visible on every tab
# ------------------------------------------------------------------------------
with st.sidebar:
    st.header("About This Data")
    st.markdown(
        "**Reporting year:** 2025\n\n"
        "**Total NPS sites:** 433\n\n"
        "**Sites reporting visits:** 406"
    )
    st.caption("This panel stays put no matter which tab above is open.")
