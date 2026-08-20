# CEN 3352 — Tuesday Example Apps (Week 2)

Single-view apps: one page, one real chart, no widgets. Every number is real
and sourced — no placeholders.

| Folder | What it shows | Real data source |
|---|---|---|
| `say_something_true/` | The official Week 2 Tuesday starter file (commuter-parking example), plus a fully annotated teaching copy | Illustrative commute log, clearly labeled as such |
| `sarasota_rainfall/` | Sarasota's rainy season, month by month | NOAA Climate Normals 1991–2020 |
| `developer_languages/` | What languages developers actually use | Stack Overflow 2025 Developer Survey (31,771 respondents) |

## Running any app locally

```bash
cd <folder-name>
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt
streamlit run app.py
```
