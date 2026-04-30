# Reco — AI Career Intelligence

Reco is a Streamlit-based AI career intelligence demo app.

It helps job seekers understand:
- which jobs fit them best,
- why they fit or do not fit,
- what skills they should improve,
- how to strengthen resume bullets,
- and what salary range they might expect.

## Demo Features

- AI-style job match scoring
- Detailed fit reasoning
- Apply / Skip interaction
- Skill gap analysis
- Resume before/after improvement
- Salary intelligence
- Product roadmap

## Files

```text
app.py
requirements.txt
README.md
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud

1. Upload these files to GitHub.
2. Go to Streamlit Cloud.
3. Click "New app."
4. Select your GitHub repository.
5. Set the main file path as:

```text
app.py
```

6. Deploy.

## Note

This version uses mock data for a safe public demo. A future version could connect real job APIs, resume parsers, salary datasets, and user accounts.
