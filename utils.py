import pandas as pd
import joblib

from PIL import Image

logo = Image.open("images/logo.png")

st.sidebar.image(
    logo,
    width=180
)

st.sidebar.markdown("## Smart Mutual Fund\nETF Platform")
# ======================================================
# Load Mutual Fund Dataset
# ======================================================

def load_mutual_data():
    """
    Load cleaned Mutual Fund dataset.
    """
    return pd.read_csv("data/Mutual_Fund_Clean.csv")


# ======================================================
# Load ETF Dataset
# ======================================================

def load_etf_data():
    """
    Load cleaned ETF dataset.
    """
    return pd.read_csv("data/ETF_Clean.csv")


# ======================================================
# Load Mutual Fund Model
# ======================================================

def load_mutual_model():
    """
    Load Random Forest model.
    """
    return joblib.load("models/MutualFund_Return_Model.pkl")


# ======================================================
# Load ETF Model
# ======================================================

def load_etf_model():
    """
    Load Decision Tree model.
    """
    return joblib.load("models/ETF_Return_Model.pkl")


# ======================================================
# Mutual Fund Features
# ======================================================

def mutual_features():
    return [
        "Price (Intraday)",
        "Change",
        "Change (%)",
        "YTD Return (%)",
        "3-Mo Return (%)",
        "1-Year Return (%)",
        "3-Year Return (%)",
        "Net Expense Ratio (%)",
        "Gross Expense Ratio (%)",
        "Net Assets",
        "50 Day Avg",
        "200 Day Avg",
        "52 Week Low",
        "52 Week High"
    ]


# ======================================================
# ETF Features
# ======================================================

def etf_features():
    return [
        "Price",
        "Change",
        "Change (%)",
        "Volume",
        "50 Day Average",
        "200 Day Average",
        "3 Month Return (%)",
        "YTD Return (%)",
        "52 Week Low",
        "52 Week High"
    ]


# ======================================================
# Mutual Fund Recommendation
# ======================================================

def recommend_mutual(
    data,
    model,
    company,
    category,
    min_return,
    max_return,
    min_expense,
    max_expense,
    top_n=10
):

    filtered = data[
        (data["Funds by Company"] == company) &
        (data["Funds by Category"] == category) &
        (data["3-Year Return (%)"] >= min_return) &
        (data["3-Year Return (%)"] <= max_return) &
        (data["Net Expense Ratio (%)"] >= min_expense) &
        (data["Net Expense Ratio (%)"] <= max_expense)
    ].copy()

    if filtered.empty:
        return filtered

    X = filtered[mutual_features()]

    filtered["Predicted 5-Year Return (%)"] = model.predict(X)

    filtered = filtered.sort_values(
        by="Predicted 5-Year Return (%)",
        ascending=False
    )

    return filtered.head(top_n)


# ======================================================
# ETF Recommendation
# ======================================================

def recommend_etf(
    data,
    model,
    min_price,
    max_price,
    min_volume,
    max_volume,
    min_return,
    max_return,
    min_ytd,
    max_ytd,
    top_n=10
):

    filtered = data[
        (data["Price"] >= min_price) &
        (data["Price"] <= max_price) &
        (data["Volume"] >= min_volume) &
        (data["Volume"] <= max_volume) &
        (data["3 Month Return (%)"] >= min_return) &
        (data["3 Month Return (%)"] <= max_return) &
        (data["YTD Return (%)"] >= min_ytd) &
        (data["YTD Return (%)"] <= max_ytd)
    ].copy()

    if filtered.empty:
        return filtered

    X = filtered[etf_features()]

    filtered["Predicted 52 Wk Return (%)"] = model.predict(X)

    filtered = filtered.sort_values(
        by="Predicted 52 Wk Return (%)",
        ascending=False
    )

    return filtered.head(top_n)