https://fraud-detection-system06.streamlit.app/

# Real-Time Fraud Detection System with Explainable AI & Live Dashboard

## Overview

This project presents an end-to-end Fraud Detection System built using Machine Learning, Explainable AI (SHAP), and an interactive Streamlit dashboard.

The system detects fraudulent financial transactions in real time while also explaining predictions transparently for fraud analysts and non-technical stakeholders.

The project simulates a real-world fintech fraud analytics workflow and focuses on:
- Fraud prediction
- Severe class imbalance handling
- Explainable AI
- Risk segmentation
- Interactive visualization
- Dashboard deployment

---

# Dataset

Dataset Used: IEEE-CIS Fraud Detection Dataset

Source:  
https://www.kaggle.com/c/ieee-fraud-detection/data

Files Used:
- `train_transaction.csv`
- `train_identity.csv`

Dataset Statistics:
- ~590,000 transactions
- 430+ features
- ~3.5% fraud rate

---

# Technologies Used

## Programming Language
- Python

## Libraries & Frameworks
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- XGBoost
- LightGBM
- SHAP
- Imbalanced-learn (SMOTE)
- Streamlit
- Joblib

---

# Project Workflow

## 1. Data Loading & Merging
- Loaded transaction and identity datasets
- Merged datasets using `TransactionID`
- Performed exploratory data analysis

## 2. Data Preprocessing
- Removed columns with excessive missing values
- Imputed numerical and categorical values
- Encoded categorical features
- Applied feature scaling using `RobustScaler`

## 3. Feature Engineering
Created custom features including:
- `HourOfDay`
- `AmtToMeanRatio`
- `DeviceRisk`

## 4. Class Imbalance Handling
- Applied SMOTE on training data only
- Improved fraud minority-class detection

## 5. Model Training
Trained and compared:
- LightGBM Classifier
- XGBoost Classifier
- Isolation Forest

## 6. Explainable AI
Implemented SHAP for:
- Global feature importance
- Waterfall plots
- Dependence plots
- Plain-English fraud explanations

## 7. Risk Segmentation
Transactions were categorized into:
- Critical Risk
- Suspicious
- Clear

## 8. Dashboard Development
Built a multi-page Streamlit dashboard with:
- Fraud overview
- Transaction explorer
- SHAP explainability
- Interactive charts

---

# Model Evaluation Metrics

Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- PR-AUC

PR-AUC was prioritized because fraud detection datasets are highly imbalanced.

---

# Key Insights

## Top Fraud Signals Identified by SHAP
- High transaction amounts
- Suspicious transaction timing
- Device-related behavioral anomalies

## Critical Risk Transaction Patterns
- High fraud probability
- Unusual transaction timing
- Suspicious device behavior
- Large transaction amounts

---

# Dashboard Features

## Overview Page
Displays:
- Total transactions
- Fraud count
- Detection rate
- Average fraud amount

## Transaction Explorer
Provides:
- Searchable transaction table
- Risk filtering
- Live fraud probability display

## SHAP Explainer
Shows:
- Transaction-specific SHAP explanations
- Waterfall plots
- Plain-English interpretations

---

# Visualizations Included

- SHAP Global Summary Plot
- Fraud Rate by Hour of Day
- Transaction Amount Distribution
- Risk Tier Donut Chart
- Precision-Recall Curve
- Interactive Plotly Scatter Plot

---

# Streamlit Dashboard

Run locally using:

```bash
streamlit run app.py
```

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
FraudDetection_ManyaSharma/
│
├── analysis.ipynb
├── data/
├── dashboard/
├── charts/
├── README.md
├── requirements.txt
├── summary.docx
└── model files
```

---

# Business Recommendations

- Deploy real-time fraud alert systems
- Use behavioral monitoring for suspicious activity
- Continuously retrain fraud models
- Integrate additional behavioral and geolocation data

---

# Model Limitations

- Fraud patterns evolve continuously
- False positives may affect customer experience
- SHAP explanations are computationally expensive
- Performance depends heavily on feature quality

---

# Future Improvements

Potential enhancements:
- Real-time streaming fraud detection
- Deep learning models
- Graph-based fraud analytics
- Cloud deployment pipelines
- Real-time API integration

---

# Conclusion

This project demonstrates a complete fraud analytics pipeline integrating:
- Machine Learning
- Explainable AI
- Data Visualization
- Interactive Dashboard Deployment

The system not only predicts fraudulent transactions effectively but also provides interpretable insights that improve transparency and analyst trust.

---

# Author

Manya Sharma

AI & Data Analytics Internship Capstone Project
