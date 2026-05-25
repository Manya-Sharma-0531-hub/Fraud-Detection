import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Fraud Overview")

# Load data
df = pd.read_csv("fraud_data.csv")

# Sidebar filters
risk_filter = st.sidebar.multiselect(
    "Select Risk Tier",
    options=df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

df = df[df['RiskTier'].isin(risk_filter)]

# Metrics
total_transactions = len(df)

fraud_count = df['ActualFraud'].sum()

detection_rate = (
    fraud_count / total_transactions
) * 100

avg_fraud_amount = df[
    df['ActualFraud'] == 1
]['TransactionAmt'].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    total_transactions
)

col2.metric(
    "Fraud Count",
    int(fraud_count)
)

col3.metric(
    "Detection Rate %",
    round(detection_rate,2)
)

col4.metric(
    "Average Fraud Amount",
    round(avg_fraud_amount,2)
)

# Plotly chart
tier_counts = (
    df['RiskTier']
    .value_counts()
    .reset_index()
)

fig = px.bar(
    tier_counts,
    x='RiskTier',
    y='count',
    title="Risk Tier Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)