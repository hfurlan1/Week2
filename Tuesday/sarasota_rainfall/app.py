# ==============================================================================
# "Sarasota's Rainy Season" — Extra Tuesday example (CEN 3352)
# ==============================================================================
# A second worked example in the "Say Something True" spirit: one page, one
# real chart, one honest claim. This one uses NOAA's official 30-year climate
# normals (1991–2020) for Sarasota, FL — real numbers, not illustrative ones.
#
# Source: NOAA National Centers for Environmental Information (NCEI),
# U.S. Climate Normals 1991-2020, Sarasota Bradenton Airport station.
#
# Run it:   streamlit run app.py
# ==============================================================================

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sarasota's Rainy Season", page_icon="\U0001F327", layout="centered")

# ------------------------------------------------------------------------------
# DESIGN SYSTEM
# ------------------------------------------------------------------------------
SKY = "#EAF2F4"     # background
RAIN = "#3B7EA1"    # accent
INK = "#20303A"     # body text

st.markdown(
    f"""
    <style>
        .stApp {{ background-color: {SKY}; }}
        .block-container {{ max-width: 680px; padding-top: 3rem; }}
        h1, h2, h3 {{ font-family: Georgia, serif !important; color: {INK} !important; }}
        p, li, span, .stMarkdown, .stCaption {{ color: {INK} !important; }}
        [data-testid="stMetricValue"] {{ color: {RAIN} !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Sarasota's Rainy Season")
st.markdown(
    "One page, one real chart. Sarasota's rainfall doesn't just vary month to "
    "month — it swings by a factor of four."
)
st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("The Real Numbers")

rainfall = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Inches of Rain": [2.77, 1.99, 3.01, 2.46, 2.85, 7.38,
                            7.55, 8.39, 6.58, 2.71, 1.90, 2.36],
    }
)

st.bar_chart(rainfall.set_index("Month"))

wettest = rainfall.loc[rainfall["Inches of Rain"].idxmax()]
driest = rainfall.loc[rainfall["Inches of Rain"].idxmin()]
st.metric(label="Wettest month", value=wettest["Month"], delta=f"{wettest['Inches of Rain']} in")
#july_row = rainfall.loc[rainfall["Month"] == "Jul"].iloc[0]
#st.metric(label="July Rainfall", value=f"{july_row['Inches of Rain']} in")


july_rain = rainfall.loc[rainfall["Month"] == "Jul", "Inches of Rain"].values[0]
st.write(f"Rainfall in July: {july_rain} inches")

st.caption(
    "Source: NOAA National Centers for Environmental Information, U.S. Climate "
    "Normals 1991\u20132020, Sarasota Bradenton Airport station."
)

st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("Why It Matters")
st.markdown(
    f"August averages {wettest['Inches of Rain']} inches of rain — more than "
    f"four times {driest['Month']}'s {driest['Inches of Rain']} inches. If your app's "
    "audience needs to plan anything outdoors in Sarasota, the month you pick "
    "matters more than almost any other variable."
)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Extra Example \u00b7 CEN 3352 \u00b7 Front-End Development and Design")
