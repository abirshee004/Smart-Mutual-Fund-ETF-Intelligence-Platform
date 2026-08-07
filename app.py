import streamlit as st

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Smart Mutual Fund & ETF Intelligence Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------

st.markdown("""
<style>
.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
    max-width:100%;
}

[data-testid="stMetricValue"]{
    font-size:32px;
    font-weight:bold;
}

[data-testid="stMetricLabel"]{
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
<h1 style='text-align:center;color:#2E86C1;'>
📈 Smart Mutual Fund & ETF Intelligence Platform
</h1>

<h4 style='text-align:center;color:gray;'>
AI-Powered Investment Analysis & Recommendation System
</h4>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------------------------------
# KPI CARDS
# -------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Mutual Funds", "9,999")

with col2:
    st.metric("ETFs", "2,835")

with col3:
    st.metric("Fund Companies", "240")

with col4:
    st.metric("ML Models", "2")

st.divider()

# -------------------------------------------------------
# PROJECT OVERVIEW
# -------------------------------------------------------

left, right = st.columns([2,1])

with left:

    st.subheader("📌 Project Overview")

    st.write("""
The **Smart Mutual Fund & ETF Intelligence Platform** is an AI-powered
financial analysis system developed using **Python**, **Machine Learning**
and **Streamlit**.

The platform collects Mutual Fund and ETF data from Yahoo Finance,
performs data cleaning, exploratory data analysis,
predicts future returns using Machine Learning models,
and recommends suitable investment options based on user preferences.
""")

with right:

    st.subheader("🎯 Objectives")

    st.success("✔ Web Scraping")

    st.success("✔ Data Cleaning")

    st.success("✔ Exploratory Data Analysis")

    st.success("✔ Machine Learning")

    st.success("✔ Recommendation System")

    st.success("✔ Interactive Dashboard")

st.divider()

# -------------------------------------------------------
# FEATURES
# -------------------------------------------------------

st.subheader("🚀 Platform Features")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### 💰 Mutual Fund Module

- Mutual Fund Analysis
- Return Prediction
- Company & Category Filters
- Top Investment Recommendation
""")

    st.info("""
### 📈 ETF Module

- ETF Analysis
- Return Prediction
- Price & Volume Filters
- Smart ETF Recommendation
""")

with c2:

    st.info("""
### ⚖ Comparison Module

- Compare Mutual Funds
- Compare ETFs
- Performance Comparison
- Interactive Charts
""")

    st.info("""
### 📊 Dashboard

- KPI Cards
- Interactive Charts
- Download CSV
- Business Insights
""")

st.divider()

# -------------------------------------------------------
# PROJECT WORKFLOW
# -------------------------------------------------------

st.subheader("🔄 Project Workflow")

st.code("""
Yahoo Finance
      │
      ▼
Web Scraping
      │
      ▼
Data Cleaning & Preprocessing
      │
      ▼
Exploratory Data Analysis (EDA)
      │
      ▼
Machine Learning Models
      │
      ▼
Recommendation Engine
      │
      ▼
Interactive Dashboard
""")

st.divider()

# -------------------------------------------------------
# TECHNOLOGY STACK
# -------------------------------------------------------

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.success("""
### Programming

• Python

• Pandas

• NumPy
""")

with tech2:

    st.success("""
### Machine Learning

• Scikit-Learn

• Random Forest

• Decision Tree
""")

with tech3:

    st.success("""
### Visualization

• Streamlit

• Plotly

• Matplotlib
""")

st.divider()

# -------------------------------------------------------
# DATASET SUMMARY
# -------------------------------------------------------

st.subheader("📊 Dataset Summary")

d1, d2 = st.columns(2)

with d1:

    st.info("""
### Mutual Fund Dataset

• Total Records : **9,999**

• Companies : **240**

• Categories : **118**

• Source : **Yahoo Finance**
""")

with d2:

    st.info("""
### ETF Dataset

• Total Records : **2,835**

• Features : **12**

• Source : **Yahoo Finance**

• Machine Learning Ready
""")

st.divider()

# -------------------------------------------------------
# APPLICATION PAGES
# -------------------------------------------------------

st.subheader("📑 Application Pages")

page1, page2, page3, page4, page5 = st.columns(5)

with page1:
    st.success("🏠 Home")

with page2:
    st.success("💰 Mutual Fund")

with page3:
    st.success("📈 ETF")

with page4:
    st.success("⚖ Compare")

with page5:
    st.success("👨‍💻 About")

st.write("")

st.info("👈 Use the navigation menu on the left sidebar to explore the application.")

st.divider()

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.caption(
    "Smart Mutual Fund & ETF Intelligence Platform | Developed using Python, Machine Learning & Streamlit"
)