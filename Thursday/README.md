# CEN 3352 — Thursday Example Apps (Week 2)

Multi-section apps: st.columns, st.tabs, st.sidebar, st.expander, all
working together. Every number is real and sourced — no placeholders.

| Folder | What it shows | Real data source |
|---|---|---|
| `worldcup_dashboard/` | The official Week 2 Thursday live-demo file | 2026 FIFA World Cup official results (FIFA.com) |
| `olympics_dashboard/` | 2026 Winter Olympics medal table | IOC official results (olympics.com) |
| `national_parks_dashboard/` | Most-visited U.S. national parks | National Park Service 2025 visitation data (nps.gov) |

## Running any app locally

```bash
cd <folder-name>
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt
streamlit run app.py
```

## Deploying to Streamlit Community Cloud

Each folder's `requirements.txt` is what Streamlit Cloud reads to know what
to install — see Thursday's "Get It Onto GitHub" and "Ship It" slides for
the full walkthrough.
