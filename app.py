import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Reco — AI Career Intelligence",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    background: linear-gradient(135deg, #5B21B6, #7C3AED, #A855F7);
    padding: 42px;
    border-radius: 26px;
    color: white;
    margin-bottom: 30px;
}
.hero h1 {
    font-size: 48px;
    line-height: 1.1;
    margin-bottom: 12px;
}
.hero p {
    font-size: 18px;
    opacity: 0.95;
    max-width: 850px;
}
.card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 8px 24px rgba(0,0,0,0.045);
    margin-bottom: 18px;
}
.mini-card {
    background: #F9FAFB;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #E5E7EB;
    margin-bottom: 12px;
}
.score {
    font-size: 34px;
    font-weight: 800;
    color: #6D28D9;
}
.badge {
    display: inline-block;
    background: #F3E8FF;
    color: #6D28D9;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    margin-right: 6px;
    margin-bottom: 6px;
}
.gap-badge {
    display: inline-block;
    background: #FEF3C7;
    color: #92400E;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    margin-right: 6px;
    margin-bottom: 6px;
}
.small {
    color: #6B7280;
    font-size: 14px;
}
.section-note {
    color: #6B7280;
    font-size: 15px;
    margin-top: -8px;
    margin-bottom: 18px;
}
.before-box {
    background: #F9FAFB;
    border-left: 5px solid #9CA3AF;
    padding: 16px;
    border-radius: 12px;
}
.after-box {
    background: #F5F3FF;
    border-left: 5px solid #7C3AED;
    padding: 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session state
# -----------------------------
if "saved_jobs" not in st.session_state:
    st.session_state.saved_jobs = []
if "skipped_jobs" not in st.session_state:
    st.session_state.skipped_jobs = []
if "generated_resume" not in st.session_state:
    st.session_state.generated_resume = False

# -----------------------------
# Sidebar profile
# -----------------------------
st.sidebar.markdown("## 🚀 Reco")
st.sidebar.caption("AI Career Intelligence")
st.sidebar.divider()

name = st.sidebar.text_input("Name", "Cindy")
target_role = st.sidebar.text_input("Target role", "Marketing Analyst / Data Analyst")
experience = st.sidebar.selectbox("Experience level", ["Entry-level", "Junior", "Mid-level"])
location = st.sidebar.text_input("Preferred location", "New York, NY")
skills = st.sidebar.text_area(
    "Your skills",
    "Python, SQL, Excel, Tableau, Marketing Analytics, Data Visualization"
)

st.sidebar.divider()
st.sidebar.success("Demo mode: AI-style mock data")
st.sidebar.caption("This version is designed for public demo and class presentation.")

# -----------------------------
# Hero
# -----------------------------
st.markdown(f"""
<div class="hero">
    <h1>Land the right role, faster.</h1>
    <p>
    Reco is an AI career intelligence app that turns a user profile into job match scores,
    skill-gap insights, resume recommendations, and salary guidance.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Top metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Profile Match", "86%")
col2.metric("Best Role", "Marketing Analyst")
col3.metric("Saved Jobs", len(st.session_state.saved_jobs))
col4.metric("Salary Range", "$78K–$112K")

st.divider()

# -----------------------------
# Job data
# -----------------------------
jobs = [
    {
        "title": "Marketing Analyst",
        "company": "Spotify",
        "location": "New York, NY",
        "score": 89,
        "salary": "$82K–$110K",
        "fit_level": "Strong Apply",
        "why": "Strong match with marketing analytics, SQL, campaign analysis, and dashboard-building experience.",
        "fit_reasons": [
            "Your marketing background connects directly with campaign performance analysis.",
            "Your SQL and dashboarding skills match the role's reporting and insight-generation needs.",
            "Your communication experience helps translate data into recommendations for non-technical teams."
        ],
        "risk_reasons": [
            "The role may expect stronger A/B testing experience.",
            "Experiment design is not clearly visible in your current profile."
        ],
        "strengths": ["Marketing Analytics", "SQL", "Data Visualization"],
        "gaps": ["A/B Testing", "Experiment Design"],
        "recommendation": "Apply. Tailor your resume toward campaign impact, segmentation, and measurable business results."
    },
    {
        "title": "Data Analyst",
        "company": "Google",
        "location": "New York, NY",
        "score": 84,
        "salary": "$90K–$125K",
        "fit_level": "Apply with Tailoring",
        "why": "Good fit based on Python, SQL, and analytical communication skills. Some technical depth may need improvement.",
        "fit_reasons": [
            "Your Python and SQL skills are relevant for data cleaning, querying, and analysis.",
            "Your quantitative graduate training supports analytical reasoning.",
            "Your visualization experience helps communicate findings clearly."
        ],
        "risk_reasons": [
            "The role may require deeper statistics or large-scale data tools.",
            "Your profile should show more technical project evidence."
        ],
        "strengths": ["Python", "SQL", "Business Insights"],
        "gaps": ["Advanced Statistics", "BigQuery"],
        "recommendation": "Apply if you revise your resume to emphasize technical analytics projects and measurable outcomes."
    },
    {
        "title": "Product Analyst",
        "company": "TikTok",
        "location": "New York, NY",
        "score": 78,
        "salary": "$85K–$118K",
        "fit_level": "Possible Fit",
        "why": "Your analytics profile is relevant, but product metrics and experimentation should be emphasized more.",
        "fit_reasons": [
            "Your user-insight and visualization skills are useful for product performance analysis.",
            "Your marketing background can transfer to growth and engagement analysis.",
            "You can explain data to business stakeholders."
        ],
        "risk_reasons": [
            "Product metrics such as retention, churn, and funnels are not yet central in your profile.",
            "Cohort analysis and experimentation experience need to be stronger."
        ],
        "strengths": ["User Insight", "Dashboarding", "Communication"],
        "gaps": ["Product Metrics", "Cohort Analysis"],
        "recommendation": "Possible fit. Build one product analytics project before applying or tailor an existing project toward product metrics."
    }
]

# -----------------------------
# Job match cards
# -----------------------------
st.markdown("## 🎯 AI Job Match Results")
st.markdown('<div class="section-note">Each role includes an AI-style fit score, explanation, strengths, risks, and an apply/skip decision.</div>', unsafe_allow_html=True)

for i, job in enumerate(jobs):
    left, right = st.columns([4, 1])

    with left:
        st.markdown(f"""
        <div class="card">
            <h3>{job['title']} · {job['company']}</h3>
            <p class="small">📍 {job['location']} · Estimated salary: {job['salary']} · Decision: <b>{job['fit_level']}</b></p>
            <div>
                <span class="badge">{job['strengths'][0]}</span>
                <span class="badge">{job['strengths'][1]}</span>
                <span class="badge">{job['strengths'][2]}</span>
            </div>
            <div>
                <span class="gap-badge">Gap: {job['gaps'][0]}</span>
                <span class="gap-badge">Gap: {job['gaps'][1]}</span>
            </div>
            <br>
            <b>AI explanation:</b>
            <p>{job['why']}</p>
            <b>Recommendation:</b>
            <p>{job['recommendation']}</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander(f"See detailed reasoning for {job['company']}"):
            st.markdown("**Why you fit:**")
            for reason in job["fit_reasons"]:
                st.write(f"- {reason}")

            st.markdown("**Why this is not a perfect match yet:**")
            for risk in job["risk_reasons"]:
                st.write(f"- {risk}")

            st.markdown("**Best resume angle:**")
            st.write("Emphasize measurable impact, analytical tools, and how your work supported better decisions.")

        b1, b2, b3 = st.columns([1, 1, 4])
        with b1:
            if st.button("Save", key=f"save_{i}"):
                if job["title"] + job["company"] not in st.session_state.saved_jobs:
                    st.session_state.saved_jobs.append(job["title"] + job["company"])
                    st.success("Saved.")
        with b2:
            if st.button("Skip", key=f"skip_{i}"):
                if job["title"] + job["company"] not in st.session_state.skipped_jobs:
                    st.session_state.skipped_jobs.append(job["title"] + job["company"])
                    st.warning("Skipped.")

    with right:
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <div class="score">{job['score']}%</div>
            <p class="small">Fit Score</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# Skill gap analysis
# -----------------------------
st.markdown("## 📉 Skill Gap Analysis")
st.markdown('<div class="section-note">Reco turns job requirements into a practical learning plan.</div>', unsafe_allow_html=True)

gap_df = pd.DataFrame({
    "Skill": ["A/B Testing", "Experiment Design", "Advanced SQL", "Product Metrics"],
    "Priority": ["High", "High", "Medium", "Medium"],
    "Why it matters": [
        "Commonly required for marketing and product analyst roles.",
        "Helps explain causal impact instead of only describing trends.",
        "Useful for large-scale company data tasks.",
        "Important for product analyst and growth roles."
    ],
    "Suggested action": [
        "Build one campaign experiment case study.",
        "Learn hypothesis testing and experiment setup.",
        "Practice window functions and joins.",
        "Study retention, churn, funnel, and cohort metrics."
    ]
})

st.dataframe(gap_df, use_container_width=True)

skill_col1, skill_col2 = st.columns(2)
with skill_col1:
    st.markdown("""
    <div class="mini-card">
    <b>Recommended 2-week focus</b>
    <p class="small">A/B testing + experiment design. These gaps appear across multiple analyst roles and are easy to show through a small portfolio project.</p>
    </div>
    """, unsafe_allow_html=True)

with skill_col2:
    st.markdown("""
    <div class="mini-card">
    <b>Portfolio project idea</b>
    <p class="small">Analyze a mock email campaign, compare treatment/control groups, calculate lift, and explain whether the campaign should scale.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# Resume tailoring
# -----------------------------
st.markdown("## 📝 AI Resume Tailoring")
st.markdown('<div class="section-note">Paste a bullet and generate a stronger version that is more measurable and job-specific.</div>', unsafe_allow_html=True)

original = st.text_area(
    "Paste one resume bullet",
    "Analyzed customer data and created reports for marketing campaigns."
)

if st.button("Generate stronger bullet"):
    st.session_state.generated_resume = True

if st.session_state.generated_resume:
    before, after = st.columns(2)

    with before:
        st.markdown("### Before")
        st.markdown(f"""
        <div class="before-box">
        {original}
        </div>
        """, unsafe_allow_html=True)

    with after:
        st.markdown("### After")
        st.markdown("""
        <div class="after-box">
        Improved marketing campaign performance by analyzing customer behavior data in Python and SQL,
        building dashboards that identified high-value segments and actionable growth opportunities.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h4>Why the new bullet is stronger</h4>
    <ul>
        <li>Starts with a stronger action verb.</li>
        <li>Connects technical tools with business impact.</li>
        <li>Uses job-relevant keywords: customer behavior, SQL, dashboard, segment, growth.</li>
        <li>Sounds more targeted for analyst roles.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# Salary
# -----------------------------
st.markdown("## 💰 Salary Intelligence")
st.markdown('<div class="section-note">Estimated salary bands are mock benchmarks for demo purposes.</div>', unsafe_allow_html=True)

salary_df = pd.DataFrame({
    "Role": ["Marketing Analyst", "Data Analyst", "Product Analyst"],
    "Entry Level": ["$70K–$88K", "$75K–$95K", "$78K–$98K"],
    "Junior / Mid Level": ["$90K–$115K", "$95K–$130K", "$100K–$135K"],
    "Best negotiation angle": [
        "Campaign analytics + business impact",
        "Python/SQL + technical project evidence",
        "Product metrics + experimentation"
    ]
})

st.table(salary_df)

st.info(
    "AI negotiation note: Based on the target roles and NYC location, a reasonable expectation range is around $85K–$105K for entry-to-junior analyst roles. The strongest negotiation story should connect analytical skills with measurable business outcomes."
)

st.divider()

# -----------------------------
# Roadmap
# -----------------------------
st.markdown("## 🚀 Product Roadmap")

roadmap = pd.DataFrame({
    "Version": ["v0.1 Demo", "v0.2", "v0.3", "v1.0"],
    "Feature": [
        "Mock AI job matching and resume guidance",
        "Resume upload and real text extraction",
        "Live job API and salary data connection",
        "User accounts, saved jobs, and personalized application tracker"
    ],
    "Status": ["Completed", "Planned", "Planned", "Future"]
})

st.dataframe(roadmap, use_container_width=True)

st.caption("Reco demo built with Streamlit. This public version uses mock data for safe and simple presentation.")
