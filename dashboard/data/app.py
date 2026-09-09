import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Churn & LTV Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    churn = pd.read_csv("dashboard/data/churn_risk_data.csv")
    ltv = pd.read_csv("dashboard/data/ltv_segment_data.csv")
    retention = pd.read_csv("dashboard/data/retention_data.csv")
    summary = pd.read_csv("dashboard/data/dashboard_summary.csv")

    return churn, ltv, retention, summary


churn_df, ltv_df, retention_df, summary_df = load_data()

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 Customer Churn & Lifetime Value Dashboard")
st.markdown(
    "Interactive dashboard for analyzing customer churn risk, "
    "lifetime value, and retention priorities."
)

st.divider()

# ---------------------------------------------------
# KPI CALCULATIONS
# ---------------------------------------------------

total_customers = len(churn_df)

high_risk = (churn_df["churn_risk"] == "High Risk").sum()
medium_risk = (churn_df["churn_risk"] == "Medium Risk").sum()
low_risk = (churn_df["churn_risk"] == "Low Risk").sum()

avg_ltv = churn_df["ltv"].mean()

high_priority = (
    churn_df["retention_priority"] == "High"
).sum()

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "High Risk Customers",
    f"{high_risk:,}"
)

col3.metric(
    "Average LTV",
    f"${avg_ltv:,.2f}"
)

col4.metric(
    "High Retention Priority",
    f"{high_priority:,}"
)

st.divider()

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("Dashboard Filters")

risk_options = ["All"] + sorted(
    churn_df["churn_risk"].dropna().unique().tolist()
)

segment_options = ["All"] + sorted(
    churn_df["customer_segment"].dropna().unique().tolist()
)

priority_options = ["All"] + sorted(
    churn_df["retention_priority"].dropna().unique().tolist()
)

selected_risk = st.sidebar.selectbox(
    "Churn Risk",
    risk_options
)

selected_segment = st.sidebar.selectbox(
    "Customer Segment",
    segment_options
)

selected_priority = st.sidebar.selectbox(
    "Retention Priority",
    priority_options
)

# ---------------------------------------------------
# APPLY FILTERS
# ---------------------------------------------------

filtered_df = churn_df.copy()

if selected_risk != "All":
    filtered_df = filtered_df[
        filtered_df["churn_risk"] == selected_risk
    ]

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["customer_segment"] == selected_segment
    ]

if selected_priority != "All":
    filtered_df = filtered_df[
        filtered_df["retention_priority"] == selected_priority
    ]

# ---------------------------------------------------
# CHURN RISK DISTRIBUTION
# ---------------------------------------------------

st.subheader("Churn Risk Analysis")

col1, col2 = st.columns(2)

with col1:

    risk_counts = filtered_df["churn_risk"].value_counts().reset_index()

    risk_counts.columns = ["Churn Risk", "Customers"]

    fig_risk = px.bar(
        risk_counts,
        x="Churn Risk",
        y="Customers",
        title="Customers by Churn Risk",
        text="Customers"
    )

    fig_risk.update_layout(
        xaxis_title="Churn Risk",
        yaxis_title="Number of Customers"
    )

    st.plotly_chart(
        fig_risk,
        use_container_width=True
    )


with col2:

    segment_counts = (
        filtered_df["customer_segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = [
        "Customer Segment",
        "Customers"
    ]

    fig_segment = px.pie(
        segment_counts,
        names="Customer Segment",
        values="Customers",
        title="Customer Segment Distribution"
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )

# ---------------------------------------------------
# LTV ANALYSIS
# ---------------------------------------------------

st.subheader("Lifetime Value Analysis")

col1, col2 = st.columns(2)

with col1:

    ltv_segment = (
        filtered_df.groupby("customer_segment")["ltv"]
        .mean()
        .reset_index()
        .sort_values("ltv", ascending=False)
    )

    fig_ltv = px.bar(
        ltv_segment,
        x="customer_segment",
        y="ltv",
        title="Average LTV by Customer Segment",
        text_auto=".2f"
    )

    fig_ltv.update_layout(
        xaxis_title="Customer Segment",
        yaxis_title="Average LTV"
    )

    st.plotly_chart(
        fig_ltv,
        use_container_width=True
    )


with col2:

    fig_scatter = px.scatter(
        filtered_df,
        x="churn_probability",
        y="ltv",
        color="churn_risk",
        hover_data=[
            "customer_id",
            "customer_segment",
            "retention_priority"
        ],
        title="Churn Probability vs LTV"
    )

    fig_scatter.update_layout(
        xaxis_title="Churn Probability",
        yaxis_title="LTV"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

# ---------------------------------------------------
# RETENTION ANALYSIS
# ---------------------------------------------------

st.subheader("Retention Priority Analysis")

priority_counts = (
    filtered_df["retention_priority"]
    .value_counts()
    .reset_index()
)

priority_counts.columns = [
    "Retention Priority",
    "Customers"
]

fig_priority = px.bar(
    priority_counts,
    x="Retention Priority",
    y="Customers",
    title="Customers by Retention Priority",
    text="Customers"
)

st.plotly_chart(
    fig_priority,
    use_container_width=True
)

# ---------------------------------------------------
# HIGH PRIORITY CUSTOMER TABLE
# ---------------------------------------------------

st.subheader("High-Priority Customers")

priority_customers = filtered_df[
    filtered_df["retention_priority"] == "High"
].sort_values(
    "retention_priority_score",
    ascending=False
)

st.dataframe(
    priority_customers[
        [
            "customer_id",
            "churn_probability",
            "churn_risk",
            "ltv",
            "customer_segment",
            "retention_priority_score",
            "retention_priority"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "Customer Churn & LTV Analytics Project"
)