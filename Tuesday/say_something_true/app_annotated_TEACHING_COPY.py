# ==============================================================================
# "Say Something True" — TEACHING COPY (annotated line-by-line)
# ==============================================================================
# This is the SAME app as app.py — same 8 zones, same output. The only
# difference is this version explains its own reasoning, in place, so you
# can read it start to finish like a worked example instead of a reference.
#
# If you're stuck on WHY a line exists (not just what it does), read the
# comment above it here before asking. If a comment doesn't answer it,
# that's a real question — ask it.
#
# Run it exactly like app.py:   streamlit run app_annotated_TEACHING_COPY.py
# ==============================================================================

import streamlit as st
import pandas as pd
# We only need two imports for this entire app. `streamlit` gives us every
# st.something() function that puts things on the page. `pandas` gives us
# DataFrame — the table object almost every chart and data display expects
# as input. You've used pandas before in this program; nothing about the
# DataFrame itself is new here, only what we do with it once it exists.


# ==============================================================================
# ZONE 1 — PAGE IDENTITY
# ==============================================================================
# Every Streamlit app is, underneath, a normal Python script that runs top
# to bottom. st.set_page_config() is special: it configures the BROWSER TAB
# itself (the title text you'd see if you had ten tabs open, and the little
# icon next to it) rather than anything inside the page. Because it touches
# the tab before the page has started rendering, Streamlit requires it to
# be the first Streamlit command in the file, and it can only be called
# once. Call it twice, or call it after some other st.something(), and
# Streamlit raises an error and refuses to run.
#
# page_title  -> the text on the browser tab
# page_icon   -> the small icon on the browser tab (an emoji works fine)
# layout      -> "centered" keeps content in a readable middle column,
#                the same idea as a printed page having margins instead of
#                text running edge-to-edge. "wide" is the alternative —
#                you'll use that starting Thursday, once columns exist.
# ==============================================================================
st.set_page_config(page_title="Say Something True", page_icon="✎", layout="centered")


# ==============================================================================
# ZONE 2 — DESIGN TOKENS
# ==============================================================================
# These three lines don't call any Streamlit function at all — they're
# plain Python variables, exactly like `x = 5`, except each one holds a
# hex color code as a string instead of a number.
#
# Why bother naming them instead of just typing "#5C7A5C" everywhere you
# need moss green? Because this file uses that color in six or seven
# different places below (headings, the accent span, the horizontal rule).
# If you typed the hex code by hand each time and later wanted a different
# green, you'd have to find and fix every occurrence — and if you missed
# one, your app would be subtly, invisibly wrong. Naming it once here means
# changing MOSS on this line changes it everywhere, guaranteed. This
# pattern — name a value once, reference the name everywhere — is called a
# "design token," and it's standard practice in real front-end code, not
# just a classroom simplification.
# ==============================================================================
CREAM = "#F2EDE4"   # background
MOSS = "#5C7A5C"    # accent
INK = "#2B2B26"     # body text


# ==============================================================================
# ZONE 3 — FONTS & THE CSS BLOCK
# ==============================================================================
# This is the zone that looks like it belongs in a different language,
# because it does — everything inside the triple-quoted string between
# <style> and </style> is CSS, not Python. Here's how to read this block
# without panicking:
#
# 1. st.markdown() is a function you already know — it prints text, and it
#    understands **bold**, lists, and links. By default it treats HTML tags
#    as literal text and just prints them on the page instead of running
#    them.
#
# 2. unsafe_allow_html=True is the one argument that changes that. It tells
#    Streamlit "the text I'm handing you is real HTML — render it, don't
#    just print it." Without this argument, everything below would show up
#    on the page as visible <style> tags instead of actually styling
#    anything. Streamlit calls this argument "unsafe" because HTML can also
#    contain <script> tags and other things that could run arbitrary code —
#    that matters if you're ever displaying HTML someone ELSE typed (a
#    comment box, a form). In your own app, writing your own CSS, there's
#    nothing unsafe about it. The name is a general warning label, not a
#    verdict on this specific use.
#
# 3. The f in front of the opening triple-quote makes this an f-string —
#    the same f-string you've used in ordinary Python to drop a variable
#    into text, like f"Hello, {name}". Here, {CREAM}, {MOSS}, and {INK} get
#    replaced with the hex codes from Zone 2 before the string is sent to
#    the browser. That's the entire connection between Zone 2 and Zone 3:
#    Zone 2 defines the colors, Zone 3 uses them.
#
# 4. Reading a CSS selector: `.stApp { background-color: ... }` means "find
#    the element with the class stApp — Streamlit's own name for the whole
#    app container — and set ITS background to this color." `h1, h2, h3`
#    targets every heading Streamlit produces (st.title, st.header,
#    st.subheader). `p, li, span` targets ordinary body text. You don't
#    need to know CSS deeply to use this pattern: find the right selector
#    for the Streamlit element you want to change, set a property on it,
#    done.
#
# 5. The doubled curly braces `{{ }}` (instead of single `{ }`) exist only
#    because this is an f-string. A single `{` inside an f-string means
#    "insert a Python value here" — but CSS also uses single curly braces
#    for its own syntax (to open and close a rule). Doubling them tells
#    Python "this is a literal curly brace for CSS, not a Python
#    placeholder." It's a small, annoying escaping rule — don't worry about
#    memorizing why, just recognize the pattern when you see it.
# ==============================================================================
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


# ==============================================================================
# ZONE 4 — HEADLINE & INTRO
# ==============================================================================
# Everything from here down is CONTENT — no more CSS, no more setup. This
# is the part of the file you'll spend the most time editing for your own
# assignment.
#
# st.title() is the single biggest heading available and Streamlit only
# lets a page have one — think of it like the <h1> of an HTML document, or
# the title of an essay: there's exactly one, and everything else nests
# below it. st.markdown() below it is plain descriptive text; because
# there's no HTML in this particular string, unsafe_allow_html isn't
# needed here — that argument only matters when the string contains actual
# HTML tags to render.
# ==============================================================================
st.title("Something I Know Is True")

st.markdown(
    "One page. One honest claim about a problem I actually care about. "
    "No widgets — just layout, and something worth looking at."
)

st.markdown("<hr>", unsafe_allow_html=True)
# A quick aside on this line: "<hr>" IS an HTML tag (a horizontal rule —
# a divider line), so this call DOES need unsafe_allow_html=True. Compare
# this to the st.markdown() call two lines above with plain text and no
# HTML — same function, different argument, because the content is
# different. Get in the habit of asking "does this string contain an HTML
# tag?" before deciding whether you need that argument.


# ==============================================================================
# ZONE 5 — PROBLEM STATEMENT
# ==============================================================================
# st.subheader() is one size down from st.title() — the equivalent of an
# <h2>. Below it, the persona and problem statement you wrote in Week 1
# become the actual words on the page. The <span class='accent'> wrapper
# is what makes the word "guess" render in moss green: `span` is an inline
# HTML tag (it doesn't start a new line, unlike a `<div>`), and
# `class='accent'` connects this specific span to the `.accent { }` rule
# you defined back in Zone 3. If you deleted the span tags entirely, the
# text would still display — you'd just lose the color highlight. Nothing
# would break.
# ==============================================================================
st.subheader("The Problem")
st.markdown(
    "Commuter students plan their whole morning around a "
    "<span class='accent'>guess</span> about parking availability, "
    "because there's no way to check ahead of time.",
    unsafe_allow_html=True,
)


# ==============================================================================
# ZONE 6 — YOUR REAL DATA
# ==============================================================================
# pd.DataFrame() is how a plain Python dictionary becomes a table pandas
# (and therefore Streamlit's charts) can work with. Read the dictionary
# literally: each KEY becomes a column header, each LIST becomes that
# column's values, read top to bottom in order. So "Mon" pairs with 4,
# "Tue" pairs with 19, and so on — position in each list is what links
# them, the same way zip() would pair up two parallel lists in plain
# Python.
#
# This dataframe isn't drawn yet — this zone only builds the table in
# memory. Nothing appears on the page from these lines alone. Drawing it
# happens in Zone 7.
# ==============================================================================
st.subheader("A Fact Worth Seeing")

commute_log = pd.DataFrame(
    {
        "Morning": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Minutes spent searching for parking": [4, 19, 7, 24, 11],
    }
)


# ==============================================================================
# ZONE 7 — CHART TYPE
# ==============================================================================
# st.bar_chart() takes the dataframe from Zone 6 and actually draws it.
# .set_index("Morning") happens first, inline, before the chart function
# ever sees the data: it tells pandas "use the Morning column as row
# labels, not as a column of data to plot." Without it, Streamlit would
# try to treat "Mon", "Tue", "Wed" as values on the chart's vertical axis,
# which makes no sense for text — you'd get an error or a nonsensical
# chart. .set_index() is what turns "a table with a day-name column" into
# "a table whose rows ARE labeled by day," which is what a chart needs.
#
# st.bar_chart, st.line_chart, and st.area_chart all accept the exact same
# input shape. That means the choice between them is a DESIGN decision,
# not a technical one — swap the function name and the same data tells a
# different visual story:
#   - bar:  emphasizes each morning as its own separate event to compare
#   - line: emphasizes the trend, the rise and fall, across the week
#   - area: like a line, but the filled space under it emphasizes total
#           accumulated time, not just the shape
# Try switching this one word and look at the same five numbers three
# different ways before deciding which is honest about what you're
# claiming.
# ==============================================================================
st.bar_chart(commute_log.set_index("Morning"))

st.caption(
    "Source: five mornings of my own commute, logged by hand. "
    "Illustrative only — replace with your own real numbers."
)
# st.caption() is deliberately the smallest, most muted text function
# Streamlit has. Use it for exactly this purpose: telling the reader where
# a number came from, without competing for attention with the number
# itself. A chart with no source note is a chart asking to be trusted on
# faith — this line is what keeps this app honest.

st.markdown("<hr>", unsafe_allow_html=True)


# ==============================================================================
# ZONE 8 — CLOSING INSIGHT
# ==============================================================================
# This is the zone it's easiest to skip, and the one that matters most.
# A chart shows WHAT is true. It doesn't say why anyone should care. This
# closing paragraph is where you answer "so what" in plain language — the
# same move a good data journalist makes at the end of an article, or a
# scientist makes in a paper's discussion section. Never let your app end
# on a chart with no sentence after it; a reader shouldn't have to do your
# interpretation for you.
# ==============================================================================
st.subheader("Why It Matters")
st.markdown(
    "A 20-minute swing across one week isn't a rounding error — it's the "
    "difference between making an 8am class and missing the first ten minutes of it."
)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Week 2 · Say Something True · CEN 3352 · Front-End Development and Design")

# ==============================================================================
# WHAT TO DO NEXT
# ==============================================================================
# Go back to app.py (the plain version, without these comments) and start
# replacing Zone 5's problem statement and Zone 6's data with your own
# persona and your own real numbers from Week 1. Keep the zone structure —
# change the content inside each zone. If a zone's job stops making sense
# for your problem, that's worth raising in class, not silently working
# around.
# ==============================================================================
