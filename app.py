import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Reco — AI Career Intelligence",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #fafafa;
}
.block-container {
    padding-top: 2rem;
}
.hero {
    background: linear-gradient(135deg, #6D28D9, #9333EA);
    padding: 40px;
    border-radius: 24px;
    color: white;
    margin-bottom: 30px;
}
.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
}
.hero p {
    font-size: 18px;
    opacity: 0.95;
}
.card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #eee;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    margin-bottom: 18px;
}
.score {
    font-size: 32px;
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
}
.small {
    color: #6B7280;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🚀 Reco")
st.sidebar.caption("AI Career Intelligence")

name = st.sidebar.text_input("Name", "Cindy")
target_role = st.sidebar.text_input("Target role", "Data Analyst / Marketing Analyst")
experience = st.sidebar.selectbox("Experience level", ["Entry-level", "Junior", "Mid-level"])
skills = st.sidebar.text_area(
    "Your skills",
    "Python, SQL, Excel, Tableau, Marketing Analytics, Data Visualization"
)
location = st.sidebar.text_input("Preferred location", "New York, NY")

st.sidebar.divider()
st.sidebar.success("Demo mode: mock AI data")

# Hero
st.markdown(f"""
<div class="hero">
    <h1>Land the right role, faster.</h1>
    <p>Reco analyzes your profile, compares it with job opportunities, explains your fit, 
    and suggests what to improve before applying.</p>
</div>
""", unsafe_allow_html=True)

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Profile Match", "86%")
col2.metric("Best Role", "Marketing Analyst")
col3.metric("Skill Gaps", "3")
col4.metric("Salary Range", "$78K–$112K")

st.divider()

# Job data
jobs = [
    {
        "title": "Marketing Analyst",
        "company": "Spotify",
        "location": "New York, NY",
        "score": 89,
        "salary": "$82K–$110K",
        "why": "Strong match with marketing analytics, SQL, campaign analysis, and dashboard-building experience.",
        "strengths": ["Marketing Analytics", "SQL", "Data Visualization"],
        "gaps": ["A/B Testing", "Experiment Design"],
        "recommendation": "Apply. This role fits your marketing background and data skill set well."
    },
    {
        "title": "Data Analyst",
        "company": "Google",
        "location": "New York, NY",
        "score": 84,
        "salary": "$90K–$125K",
        "why": "Good fit based on Python, SQL, and analytical communication skills. Some technical depth may need improvement.",
        "strengths": ["Python", "SQL", "Business Insights"],
        "gaps": ["Advanced Statistics", "BigQuery"],
        "recommendation": "Apply if you tailor your resume toward technical analytics impact."
    },
    {
        "title": "Product Analyst",
        "company": "TikTok",
        "location": "New York, NY",
        "score": 78,
        "salary": "$85K–$118K",
        "why": "Your analytics profile is relevant, but product metrics and experimentation should be emphasized more.",
        "strengths": ["User Insight", "Dashboarding", "Communication"],
        "gaps": ["Product Metrics", "Cohort Analysis"],
        "recommendation": "Possible fit. Build one product analytics project before applying."
    }
]

st.markdown("## 🎯 AI Job Match Results")

for job in jobs:
    with st.container():
        left, right = st.columns([4, 1])
        with left:
            st.markdown(f"""
            <div class="card">
                <h3>{job['title']} · {job['company']}</h3>
                <p class="small">📍 {job['location']} · Estimated salary: {job['salary']}</p>
                <span class="badge">{job['strengths'][0]}</span>
                <span class="badge">{job['strengths'][1]}</span>
                <span class="badge">{job['strengths'][2]}</span>
                <br><br>
                <b>AI explanation:</b>
                <p>{job['why']}</p>
                <b>Recommendation:</b>
                <p>{job['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)

        with right:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <div class="score">{job['score']}%</div>
                <p class="small">Fit Score</p>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# Skill gap
st.markdown("## 📉 Skill Gap Analysis")

gap_df = pd.DataFrame({
    "Skill": ["A/B Testing", "Experiment Design", "Advanced SQL", "Product Metrics"],
    "Importance": ["High", "High", "Medium", "Medium"],
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

st.divider()

# Resume section
st.markdown("## 📝 AI Resume Tailoring")

original = st.text_area(
    "Paste one resume bullet",
    "Analyzed customer data and created reports for marketing campaigns."
)

if st.button("Generate stronger bullet"):
    st.success(
        "Improved marketing campaign performance by analyzing customer behavior data in Python and SQL, building dashboards that identified high-value segments and actionable growth opportunities."
    )

st.markdown("""
<div class="card">
<h4>AI Resume Advice</h4>
<ul>
<li>Use stronger action verbs: analyzed, built, improved, automated, identified.</li>
<li>Add measurable outcomes when possible.</li>
<li>Match keywords from the target job description.</li>
<li>Connect marketing experience with analytical impact.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.divider()

# Salary
st.markdown("## 💰 Salary Intelligence")

salary_df = pd.DataFrame({
    "Role": ["Marketing Analyst", "Data Analyst", "Product Analyst"],
    "Entry Level": ["$70K–$88K", "$75K–$95K", "$78K–$98K"],
    "Mid Level": ["$90K–$115K", "$95K–$130K", "$100K–$135K"]
})

st.table(salary_df)

st.info(
    "AI negotiation note: Based on your target roles and NYC location, a reasonable expectation range is around $85K–$105K for entry-to-junior analyst roles."
)

st.divider()

st.markdown("### 🚀 Product Roadmap")
st.write(
    "Next version: connect real job APIs, upload resumes, store user profiles, and generate personalized job application plans."
)
