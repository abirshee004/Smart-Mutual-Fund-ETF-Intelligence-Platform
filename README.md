# 📈 Smart Mutual Fund & ETF Intelligence Platform

> **AI-Powered Mutual Fund & ETF Recommendation System using Machine Learning**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Project Overview

The **Smart Mutual Fund & ETF Intelligence Platform** is a data-driven financial analytics and recommendation system developed using **Python**, **Machine Learning**, and **Streamlit**.

The platform collects Mutual Fund and ETF data from **Yahoo Finance**, performs **Web Scraping**, **Data Cleaning**, **Exploratory Data Analysis (EDA)**, builds predictive **Machine Learning models**, and provides intelligent investment recommendations through an interactive dashboard.

---

## 🎯 Project Objectives

- Collect Mutual Fund and ETF data using Web Scraping
- Clean and preprocess financial datasets
- Perform Exploratory Data Analysis (EDA)
- Build Machine Learning models for return prediction
- Recommend investment options based on user preferences
- Develop an interactive Streamlit dashboard

---

## 🚀 Features

- 📈 Mutual Fund Recommendation System
- 📊 ETF Recommendation System
- 🤖 Machine Learning Return Prediction
- 📉 Interactive Charts & Visualizations
- 📊 Financial Performance Analysis
- 📥 Download Recommendation Results
- ⚖ Compare Mutual Funds and ETFs

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| BeautifulSoup | Web Scraping |
| Requests | Data Collection |
| Scikit-Learn | Machine Learning |
| Plotly | Interactive Visualization |
| Streamlit | Dashboard Development |
| Joblib | Model Serialization |

---

# 📂 Project Structure

```text
Smart_Mutual_Fund_ETF/
│
├── app.py
├── requirements.txt
├── README.md
├── utils.py
│
├── data/
│   ├── Mutual_Fund_Clean.csv
│   ├── ETF_Clean.csv
│   ├── Yahoo_Mutual_Funds.csv
│   └── Yahoo_ETFs.csv
│
├── models/
│   ├── MutualFund_Return_Model.pkl
│   └── ETF_Return_Model.pkl
│
├── pages/
│   ├── Home.py
│   ├── Mutual_Fund.py
│   ├── ETF.py
│   ├── Compare.py
│   └── About.py
│
├── images/
│   ├── logo.png
│   ├── home_page.png
│   ├── mutual_fund_page.png
│   ├── etf_page.png
│   └── compare_page.png
│
├── notebooks/
│   ├── Mutual_Fund_Web_Scraping.ipynb
│   ├── ETF_Web_Scraping.ipynb
│   ├── Data_Cleaning.ipynb
│   ├── EDA.ipynb
│   └── Machine_Learning.ipynb
│
├── reports/
│   ├── Final_Report.pdf
│   └── Project_Presentation.pdf
│
└── web_scraping/
    ├── mutual_fund_scraper.py
    └── etf_scraper.py
```

---

# 🔄 Project Workflow

```text
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
```

---

# 📊 Dataset Information

## Mutual Fund Dataset

- Total Records : **9,999**
- Fund Companies : **240**
- Fund Categories : **118**
- Source : Yahoo Finance

---

## ETF Dataset

- Total Records : **2,835**
- Features : **12**
- Source : Yahoo Finance

---

# 🤖 Machine Learning Models

## Mutual Fund Model

**Algorithm:** Random Forest Regressor

**Target Variable:**

- 5-Year Return (%)

**Workflow**

```text
User Input
     │
     ▼
Company Selection
     │
     ▼
Fund Category
     │
     ▼
Return Range
     │
     ▼
Expense Ratio
     │
     ▼
Random Forest Model
     │
     ▼
Predicted 5-Year Return
     │
     ▼
Top Investment Recommendations
```

---

## ETF Model

**Algorithm:** Decision Tree Regressor

**Target Variable**

- 52 Week Change (%)

**Workflow**

```text
User Input
     │
     ▼
Price Range
     │
     ▼
Trading Volume
     │
     ▼
Historical Returns
     │
     ▼
Decision Tree Model
     │
     ▼
Predicted ETF Performance
     │
     ▼
Top ETF Recommendations
```

---

# 📈 Dashboard Pages

- 🏠 Home
- 💰 Mutual Fund Recommendation
- 📈 ETF Recommendation
- ⚖ Compare Investments
- 👨‍💻 About

---

# 📷 Dashboard Screenshots

## Home Page

![Home](images/home_page.png)

---

## Mutual Fund Recommendation

![Mutual Fund](images/mutual_fund_page.png)

---

## ETF Recommendation

![ETF](images/etf_page.png)

---

## Comparison Dashboard

![Compare](images/compare_page.png)

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/abirshee004/Smart_Mutual_Fund_ETF.git
```

Go to the project folder

```bash
cd Smart_Mutual_Fund_ETF
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

- Live Yahoo Finance API Integration
- Portfolio Optimization
- Risk Analysis
- Investment Score Prediction
- AI Financial Assistant
- News Sentiment Analysis
- Mobile Responsive Dashboard

---

# 👨‍💻 Author

**Abir Shee**

B.Tech in Computer Science

B. P. Poddar Institute of Management and Technology

GitHub: https://github.com/abirshee004

LinkedIn: *(Add Your LinkedIn Profile Here)*

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ **If you found this project useful, please consider giving it a star on GitHub!**
