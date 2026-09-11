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

---

## 2. Data Preparation for Machine Learning

I prepared the customer dataset for machine learning by working with the raw dataset, which contains both numerical and categorical variables. Since models require appropriately formatted numerical inputs, the data needed to be structured before it could be used for training.

**Preparation flow:**

```
Raw Customer Dataset
        ↓
Select Relevant Columns
        ↓
Separate Features and Target
        ↓
Identify Numerical Features
        ↓
Identify Categorical Features
        ↓
Apply Preprocessing
        ↓
Generate Model-Ready Data
```

**Why this was necessary:**
- Models cannot directly process ordinary text categories.
- Data preparation creates a consistent input format for training and inference.
- It makes the model pipeline reusable for future predictions.

*(Specific cleaning operations, such as exact counts of duplicate rows removed or missing values filled, are not detailed here as they were not independently verified against the project's source files.)*

---

## 3. Categorical and Numerical Feature Handling

The project uses a scikit-learn preprocessing pipeline built around a `ColumnTransformer`, with numerical and categorical columns handled through separate preprocessing branches.

```
Numerical Features → Numerical preprocessing
Categorical Features → Categorical encoding
                ↓
        ColumnTransformer
                ↓
     Machine Learning Model
```

**Why this approach was used:**
- Different data types require different processing methods.
- Categorical text must be converted into a machine-readable numerical representation.
- Using a pipeline keeps preprocessing consistent between model training and prediction.
- It reduces the risk of training and prediction data being processed differently.

*(The exact scaler and encoder implementations are not specified here, as they were not independently confirmed against the source code.)*

---

## 4. Model Training

Churn prediction is a binary classification problem:

- **No** → Customer does not churn
- **Yes** → Customer churns

Multiple candidate machine learning approaches were considered:

- Logistic Regression
- Random Forest
- XGBoost

**Why multiple algorithms were considered:**
- Different algorithms learn patterns differently.
- Comparing multiple approaches provides a stronger basis for selecting the final model.
- Churn behaviour may involve both straightforward and nonlinear relationships between features.

---

## 5. Logistic Regression

Logistic Regression was used for binary churn classification and produces a probability-based churn prediction. **The final saved churn model is Logistic Regression**, configured with `max_iter=1000` and `random_state=42`. The preprocessing component and trained model were saved together in the model artifact.

**Why Logistic Regression was useful:**
- Suitable for binary classification problems.
- Efficient and interpretable.
- Provides probability estimates.
- Probability estimates are useful for churn risk classification.

*(Logistic Regression was selected as the final model based on the overall evaluation process; this documentation does not claim it was selected solely due to a single highest metric.)*

---

## 6. Random Forest

Random Forest was considered and evaluated as a candidate churn classification model. It uses multiple decision trees and combines their predictions, and can capture nonlinear relationships and interactions between customer attributes.

**Why it was considered:**
- Customer churn can depend on combinations of multiple customer characteristics.
- Tree-based models can capture patterns that may not be represented by a simple linear relationship.

---

## 7. XGBoost

XGBoost was considered and evaluated as another candidate model. It is a gradient boosting algorithm based on decision trees, building trees sequentially to improve prediction performance.

**Why it was considered:**
- It can model nonlinear relationships.
- It is widely used for structured/tabular data.
- It provided a useful comparison against Logistic Regression and Random Forest.

*(Specific XGBoost hyperparameters are not listed here, as they were not independently confirmed against the source code.)*

---

## 8. Model Evaluation

Model evaluation was performed using the following metrics:

- **Accuracy** – Overall percentage of correct predictions.
- **Precision** – Among customers predicted to churn, how many actually churned.
- **Recall** – Among customers who actually churned, how many were successfully identified.
- **F1 Score** – Balance between precision and recall.
- **ROC-AUC** – Measures how effectively the model distinguishes churn customers from non-churn customers across classification thresholds.

**Why multiple metrics were required:** Accuracy alone can be misleading, especially on imbalanced datasets like churn, where the majority of customers do not churn. Churn is a business problem where missing actual churn customers can be costly, so recall and other classification metrics are also directly relevant to evaluating model usefulness.

---

## 9. Churn Probability Generation

The model produces not only a binary prediction but also a churn probability.

```
Customer → Trained Churn Model → Churn Probability → Churn Prediction
```

**Why probability is useful:**
- A binary Yes/No result alone does not show the level of risk.
- Probability allows customers to be ranked according to estimated churn likelihood.
- Higher-risk customers can be prioritized for retention analysis.
- Probability can be consumed by downstream project components.

Churn probability values are model-based estimates and should not be interpreted as business certainty.

---

## 10. Churn Risk Classification

Churn probabilities were converted into practical risk categories to support business interpretation:

- Low Risk
- Medium Risk
- High Risk

**Final risk distribution:**

| Risk Category | Customers |
|---|---|
| Low Risk | 4,489 |
| Medium Risk | 1,344 |
| High Risk | 1,210 |

**Why risk categories were created:**
- Business users can understand risk categories more easily than thousands of raw probability values.
- Risk categories support customer prioritization.
- High-risk customers can be considered for retention-focused analysis.

---

## 11. Confusion Matrix Analysis

| | Predicted No Churn | Predicted Churn |
|---|---|---|
| **Actual No Churn** | 4,797 | 377 |
| **Actual Churn** | 622 | 1,247 |

- **True Negative (4,797):** Actual non-churn customer correctly predicted as non-churn.
- **False Positive (377):** Actual non-churn customer predicted as churn.
- **False Negative (622):** Actual churn customer predicted as non-churn.
- **True Positive (1,247):** Actual churn customer correctly predicted as churn.

**Why this analysis is important:** The confusion matrix breaks down model performance beyond a single accuracy figure. False negatives are particularly important to understand, since missed churn customers represent missed retention opportunities for the business.

---

## 12. ROC Curve Analysis

An ROC curve was generated to evaluate model discrimination across different probability thresholds.

**Final ROC-AUC: 90.92%**

ROC-AUC measures how well the model separates churn customers from non-churn customers across all thresholds — it does not mean that 90.92% of predictions are correct. It is a discrimination metric, not an accuracy metric.

---

## 13. Model Performance Reporting

| Metric | Result |
|---|---|
| Accuracy | 85.82% |
| Precision | 76.79% |
| Recall | 66.72% |
| F1 Score | 71.40% |
| ROC-AUC | 90.92% |

**Reporting files:**
- `reports/model_metrics_long.csv`
- `reports/model_performance.csv`
- `reports/final_dashboard_kpis.csv`

**Why structured reports were created:**
- Easier review
- Model comparison
- Dashboard integration
- Presentation
- Documentation
- Future maintenance

---

## 14. Churn Prediction Output Generation

After finalizing the model, customer-level prediction outputs were generated, containing customer-level prediction information such as:

- Customer ID
- Churn probability
- Churn prediction
- Churn risk

**Why this was necessary:**
- The model must generate usable predictions rather than only evaluation scores.
- Customer-level outputs allow downstream components to use the churn results.
- Outputs can support retention, LTV, backend, and dashboard analysis.

---

## 15. Saving the Final Trained Model

The trained model was saved using Joblib.

**Model path:** `models/churn_model.joblib`

The saved model contains the trained preprocessing and model components required for prediction. The final saved model is:

**Logistic Regression** — `max_iter=1000`, `random_state=42`

**Why saving the model is important:**
- The model does not need to be retrained for every prediction.
- The saved model can be loaded later for inference.
- It provides a reusable artifact for integration with backend/deployment workflows.
- Keeping preprocessing bundled with the model helps maintain consistent prediction behaviour.

---

## 16. Model Validation

The final model and generated outputs were reviewed and validated. Validation included checking:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion matrix
- ROC curve
- Churn predictions
- Churn probabilities
- Risk classifications
- Generated reports
- Saved model artifact

**Why this was necessary:**
- To verify that the final outputs are internally consistent.
- To ensure the saved model and generated reports are ready for integration.
- To identify issues before deployment or project review.

*(This validation was conducted internally as part of model development and review; it does not represent external production validation.)*

---

## 17. Documentation

I documented the work throughout the development process. Relevant Role 4 documentation files include:

- `reports/day8_progress.txt`
- `reports/day9_progress.txt`
- `reports/day9_model_analysis.txt`
- `reports/day10_progress.txt`
- `reports/day10_model_validation.txt`

This documentation covers development progress, churn model analysis, model validation, churn insights, and deployment preparation.

**Why this was necessary:**
- Makes the work traceable.
- Helps teammates understand the work.
- Supports company/internship review.
- Makes future maintenance easier.
- Provides evidence of the development process.

---

## 18. Deployment Preparation

After model development and validation, the churn model was prepared for integration with the wider project via `models/churn_model.joblib`.

The wider project consists of:

- FastAPI backend
- Power BI dashboard
- LTV component
- Churn prediction component

My Role 4 contribution supplies the trained churn model and prediction outputs that can be consumed by other project components — this reflects **deployment preparation and integration readiness**, not deployment of the full application.

---

# FINAL MODEL RESULTS

| Metric | Result |
|---|---|
| Accuracy | 85.82% |
| Precision | 76.79% |
| Recall | 66.72% |
| F1 Score | 71.40% |
| ROC-AUC | 90.92% |

The final model demonstrated strong overall classification performance, with an ROC-AUC of 90.92%, indicating strong ability to distinguish between churn and non-churn customers. Accuracy was 85.82%, while precision and recall provide additional insight into the model's ability to correctly identify predicted and actual churn customers. These metrics reflect development and validation performance and are not, on their own, a claim of production readiness.

---

# FINAL CUSTOMER CHURN RESULTS

| KPI | Value |
|---|---|
| Total Customers | 7,043 |
| Actual Churn Customers | 1,869 |
| Predicted Churn Customers | 1,624 |
| Actual Churn Rate | 26.54% |
| Predicted Churn Rate | 23.06% |
| Low Risk Customers | 4,489 |
| Medium Risk Customers | 1,344 |
| High Risk Customers | 1,210 |
| Average Monthly Charges | 64.76 |
| Average Tenure | 32.37 |

These values summarize the final prediction and customer-risk output generated by the model.

---

# KEY ROLE 4 DELIVERABLES

**Machine Learning**
- Feature selection
- Data preparation
- Numerical/categorical feature handling
- Preprocessing pipeline
- Logistic Regression
- Random Forest
- XGBoost
- Model evaluation
- Model validation

**Prediction**
- Churn prediction
- Churn probability generation
- Churn risk classification
- Customer-level prediction output

**Evaluation**
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

**Saved Model**
- `models/churn_model.joblib`

**Reports**
- `reports/model_metrics_long.csv`
- `reports/model_performance.csv`
- `reports/final_dashboard_kpis.csv`

**Development Documentation**
- `reports/day8_progress.txt`
- `reports/day9_progress.txt`
- `reports/day9_model_analysis.txt`
- `reports/day10_progress.txt`
- `reports/day10_model_validation.txt`

---

# END-TO-END ROLE 4 WORKFLOW

```
IBM Telco Customer Churn Dataset
        ↓
Feature Selection
        ↓
Data Preparation
        ↓
Numerical + Categorical Feature Handling
        ↓
Preprocessing Pipeline
        ↓
Model Training
        ↓
Logistic Regression / Random Forest / XGBoost
        ↓
Model Evaluation
        ↓
Accuracy / Precision / Recall / F1 / ROC-AUC
        ↓
Final Model
        ↓
Churn Probability
        ↓
Churn Prediction
        ↓
Risk Classification
        ↓
Customer-Level Output
        ↓
Model Saving
        ↓
Validation
        ↓
Documentation
        ↓
Deployment Preparation
```

---

# BUSINESS VALUE OF ROLE 4

The churn model allows the project to move beyond historical reporting toward predictive customer-risk analysis. It helps answer key business questions:

- Which customers are likely to churn?
- What is the estimated churn probability for a given customer?
- Which customers fall into high-risk categories?
- Which customers may require retention attention?
- How can churn probability be combined with customer value/LTV?
- How can customer-level churn predictions support business decision-making?

The churn prediction component provides the machine learning foundation for the broader Customer Churn Prediction & LTV Engine. It does not, on its own, guarantee customer retention — it provides a data-driven basis for prioritizing retention efforts.

---

# WHAT I LEARNED / TECHNICAL CONTRIBUTION

Through this work, I applied the following technologies and concepts:

- Binary classification
- Feature selection
- Data preprocessing
- Categorical feature handling
- Numerical feature handling
- scikit-learn pipelines
- ColumnTransformer
- Logistic Regression
- Random Forest
- XGBoost
- Classification metrics
- Confusion matrix interpretation
- ROC curve and ROC-AUC
- Probability-based prediction
- Risk classification
- Model serialization with Joblib
- Model validation
- Machine learning reporting
- Git/GitHub-based project workflow
- Deployment preparation
