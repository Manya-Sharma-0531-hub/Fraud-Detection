import streamlit as st
import pandas as pd

st.title("🔎 Transaction Explorer")

df = pd.read_csv("fraud_dashboard_data.csv")

# Sidebar filters
tier_filter = st.sidebar.multiselect(
    "Risk Tier",
    df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

df = df[
    df['RiskTier'].isin(tier_filter)
]

# Search Transaction ID
transaction_id = st.text_input(
    "Enter TransactionID"
)

if transaction_id:

    result = df[
        df['TransactionID']
        .astype(str)
        == transaction_id
    ]

    st.write(result)

# Filterable table
st.dataframe(df)

# Live risk score
if transaction_id:

    result = df[
        df['TransactionID']
        .astype(str)
        == transaction_id
    ]

    if len(result):

        score = result[
            'FraudProbability'
        ].values[0]

        st.metric(
            "Live Risk Score",
            round(score,3)
        )