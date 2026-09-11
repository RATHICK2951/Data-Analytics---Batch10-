# Customer Churn Prediction & Lifetime Value (LTV) Engine

# My Role – Role 4: Churn Prediction Model Development

I was responsible for the machine learning component of the Customer Churn Prediction & LTV Engine. My objective was to build a binary classification model capable of identifying customers who are likely to leave the service, and to generate churn probabilities that could support downstream retention, LTV, backend, and dashboard components of the wider project.

My responsibility covered the complete machine learning lifecycle — from feature selection and data preparation through model training, evaluation, prediction generation, validation, model saving, reporting, and deployment preparation.

---

## 1. Feature Selection

I identified the customer attributes relevant to churn prediction. The dataset contains demographic, service, contract, tenure, and billing information, with **Churn** as the target variable. `customerID` is an identifier field and was not used as a predictive feature.

- **Numerical features:** `tenure`, `MonthlyCharges`, `TotalCharges`
- **Categorical features:** `gender`, `Partner`, `Dependents`, `Contract`, `InternetService`, `PaymentMethod`, and other related service/account attributes

**Why this was required:** Machine learning models should be trained on meaningful customer attributes rather than identifiers. `customerID` identifies a record but does not represent customer behaviour, so selecting the appropriate input and target columns was necessary to create a clean, well-defined ML problem.

| Feature | Type | Purpose |
|---|---|---|
| gender | Categorical | Demographic attribute |
| SeniorCitizen | Categorical | Demographic attribute |
| Partner | Categorical | Household/demographic attribute |
| Dependents | Categorical | Household/demographic attribute |
| tenure | Numerical | Length of customer relationship |
| PhoneService | Categorical | Service subscription attribute |
| MultipleLines | Categorical | Service subscription attribute |
| InternetService | Categorical | Service subscription attribute |
| OnlineSecurity | Categorical | Service subscription attribute |
| OnlineBackup | Categorical | Service subscription attribute |
| DeviceProtection | Categorical | Service subscription attribute |
| TechSupport | Categorical | Service subscription attribute |
| StreamingTV | Categorical | Service subscription attribute |
| StreamingMovies | Categorical | Service subscription attribute |
| Contract | Categorical | Contract/billing attribute |
| PaperlessBilling | Categorical | Billing attribute |
| PaymentMethod | Categorical | Billing attribute |
| MonthlyCharges | Numerical | Billing attribute |
| TotalCharges | Numerical | Billing attribute |
| customerID | Identifier (excluded) | Record identification only, not predictive |

*Note: This table reflects the intended relationships between features and the churn problem based on their role in the dataset; it does not represent confirmed causal relationships between any feature and churn.*
