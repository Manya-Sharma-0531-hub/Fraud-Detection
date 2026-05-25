import streamlit as st
import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

st.title("🧠 SHAP Explainer")

# Load files
model = joblib.load("best_model.pkl")

df = pd.read_csv("fraud_data.csv")

transaction_id = st.text_input(
    "Enter TransactionID"
)

if transaction_id:

    row = df[
        df['TransactionID']
        .astype(str)
        == transaction_id
    ]

    if len(row):

        st.write(row)

        # Remove non-feature columns
        X = row.drop(
            columns=[
                'ActualFraud',
                'FraudProbability',
                'RiskTier'
            ],
            errors='ignore'
        )

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(X)

        fig = plt.figure()

        shap.plots.waterfall(
            shap.Explanation(
                values=shap_values[0],
                base_values=explainer.expected_value,
                data=X.iloc[0],
                feature_names=X.columns
            ),
            show=False
        )

        st.pyplot(fig)

        # Plain English explanation
        prob = row[
            'FraudProbability'
        ].values[0]

        if prob >= 0.75:
            st.error(
                "Critical risk transaction. Strong fraud indicators detected."
            )

        elif prob >= 0.40:
            st.warning(
                "Borderline transaction. Manual analyst review recommended."
            )

        else:
            st.success(
                "Transaction appears legitimate."
            )