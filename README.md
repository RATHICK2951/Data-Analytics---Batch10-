I need you to completely update the README.md section/documentation for my contribution to this project.

IMPORTANT:
- This is my Role 4 contribution: CHURN PREDICTION MODEL DEVELOPMENT.
- Write it professionally for company review, internship evaluation, GitHub review, presentation, and viva.
- Keep the information technically accurate and consistent with the actual project files.
- Do NOT invent work that I did not perform.
- Do NOT claim that I used a technique unless it is actually supported by the project.
- Do NOT modify source code, datasets, model files, dashboard files, backend files, or other team members' work.
- ONLY update the README.md documentation.
- Keep the existing project README information outside my Role 4 section intact unless it needs minor formatting adjustment.
- Replace/expand my current short Role 4 list with a detailed professional explanation.
- Explain WHAT I DID, HOW I DID IT, and WHY I DID IT for every major step.
- Make the documentation understandable to both technical and non-technical reviewers.
- Use proper Markdown headings, tables, bullet points, code blocks, and workflow diagrams.
- Do not make the README unnecessarily repetitive.
- After editing, verify the Markdown formatting and make sure there are no broken sections.

PROJECT:
Customer Churn Prediction & Lifetime Value (LTV) Engine

MY ROLE:
Role 4 – Churn Prediction Model Development

MY MAIN RESPONSIBILITY:
Develop, evaluate, validate, document, and prepare the machine learning component responsible for predicting customer churn.

DATASET:
IBM Telco Customer Churn dataset.

TARGET:
Churn

IDENTIFIER:
customerID

The customerID field is an identifier and should not be treated as a predictive feature.

MAIN INPUT FEATURES:
- gender
- SeniorCitizen
- Partner
- Dependents
- tenure
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

MACHINE LEARNING TECHNOLOGIES:
- Python
- pandas
- NumPy
- scikit-learn
- XGBoost
- Joblib
- Matplotlib / visualization tools used for model analysis

ROLE 4 WORKFLOW:
Dataset
→ Feature Selection
→ Data Preparation
→ Numerical/Categorical Feature Handling
→ Preprocessing Pipeline
→ Model Training
→ Model Evaluation
→ Model Comparison
→ Final Model
→ Churn Probability Generation
→ Churn Risk Classification
→ Prediction Output
→ Model Validation
→ Model Saving
→ Documentation
→ Deployment Preparation

NOW WRITE THE README DOCUMENTATION USING THE FOLLOWING CONTENT AND STRUCTURE:

# My Role – Role 4: Churn Prediction Model Development

Start with a professional overview explaining that I was responsible for the machine learning component of the Customer Churn Prediction & LTV Engine.

Explain that the objective was to build a binary classification model capable of identifying customers who are likely to leave the service and generate churn probabilities that can support downstream retention, LTV, backend, and dashboard components.

Explain that my responsibility covered the complete ML lifecycle from feature selection and data preparation through model training, evaluation, prediction generation, validation, model saving, reporting, and deployment preparation.

---

## 1. Feature Selection

Explain:

- I identified the customer attributes relevant to churn prediction.
- The dataset contains demographic, service, contract, tenure, and billing information.
- The target variable is Churn.
- customerID is an identifier and was not used as a predictive feature.
- Numerical features include tenure, MonthlyCharges, and TotalCharges.
- Categorical features include gender, Partner, Dependents, Contract, InternetService, PaymentMethod, etc.

Explain WHY feature selection was required:

- Machine learning should use meaningful customer attributes rather than identifiers.
- customerID identifies a record but does not represent customer behaviour.
- Selecting the appropriate input and target columns creates a clean ML problem.

Include the feature list in a professional table with:
Feature / Type / Purpose

Do not claim causal relationships unless supported by the actual analysis.

---

## 2. Data Preparation for Machine Learning

Explain how I prepared the customer dataset for machine learning.

Explain that the raw dataset contains both numerical and categorical variables.

Explain that machine learning models require appropriately formatted numerical inputs.

Describe the preparation as:

Raw Customer Dataset
→ Select Relevant Columns
→ Separate Features and Target
→ Identify Numerical Features
→ Identify Categorical Features
→ Apply Preprocessing
→ Generate Model-Ready Data

Explain WHY:

- Models cannot directly process ordinary text categories.
- Data preparation creates a consistent input format.
- It makes the model pipeline reusable for future predictions.

IMPORTANT:
Do not invent specific cleaning operations such as removing an exact number of duplicate rows or filling a specific number of missing values unless the actual project files confirm those operations.

---

## 3. Categorical and Numerical Feature Handling

Explain that the project uses a scikit-learn preprocessing pipeline and ColumnTransformer.

Explain that numerical and categorical columns are handled through separate preprocessing branches.

Explain the concept:

Numerical Features
→ Numerical preprocessing

Categorical Features
→ Categorical encoding

Both
→ ColumnTransformer
→ Machine Learning Model

Explain WHY:

- Different data types require different processing.
- Categorical text must be converted into machine-readable numerical representation.
- Using a pipeline keeps preprocessing consistent between model training and prediction.
- It reduces the risk of training and prediction data being processed differently.

Do not claim a specific scaler or encoder unless the actual source code confirms it. If the code confirms the encoder/scaler, mention the exact implementation.

---

## 4. Model Training

Explain that churn prediction is a binary classification problem:

No → Customer does not churn
Yes → Customer churns

Explain that multiple candidate machine learning approaches were considered:

- Logistic Regression
- Random Forest
- XGBoost

Explain WHY multiple algorithms were considered:

- Different algorithms learn patterns differently.
- Comparing multiple approaches gives a stronger basis for selecting the final model.
- Churn behaviour may involve both straightforward and nonlinear relationships.

---

## 5. Logistic Regression

Explain:

- Logistic Regression was used for binary churn classification.
- It produces a probability-based churn prediction.
- The final saved churn model is Logistic Regression.
- The model configuration includes max_iter=1000 and random_state=42.
- The preprocessing component and trained model were saved together in the model artifact.

Explain WHY Logistic Regression was useful:

- Suitable for binary classification.
- Efficient and interpretable.
- Provides probability estimates.
- Probability estimates are useful for churn risk classification.

Do not claim it was selected solely because it had the highest metric unless the actual model comparison confirms that.

---

## 6. Random Forest

Explain:

- Random Forest was considered/evaluated as a candidate churn classification model.
- It uses multiple decision trees and combines their predictions.
- It can capture nonlinear relationships and interactions between customer attributes.

Explain WHY it was considered:

- Customer churn can depend on combinations of multiple customer characteristics.
- Tree-based models can capture patterns that may not be represented by a simple linear relationship.

---

## 7. XGBoost

Explain:

- XGBoost was considered/evaluated as another candidate model.
- It is a gradient boosting algorithm based on decision trees.
- It builds trees sequentially to improve prediction performance.

Explain WHY it was considered:

- It can model nonlinear relationships.
- It is widely used for structured/tabular data.
- It provides a useful comparison against Logistic Regression and Random Forest.

Do not invent exact XGBoost hyperparameters unless they are present in the actual code.

---

## 8. Model Evaluation

Explain that model evaluation was performed using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Explain each metric clearly:

Accuracy:
Overall percentage of correct predictions.

Precision:
Among customers predicted to churn, how many actually churned.

Recall:
Among customers who actually churned, how many were successfully identified.

F1 Score:
Balance between precision and recall.

ROC-AUC:
Measures how effectively the model distinguishes churn customers from non-churn customers across classification thresholds.

Explain WHY multiple metrics were required instead of relying only on accuracy.

Mention that churn is a business problem where missing actual churn customers can be important, so recall and other classification metrics are also relevant.

---

## 9. Churn Probability Generation

Explain that the model produces not only a binary prediction but also a churn probability.

Example concept:

Customer
→ Trained Churn Model
→ Churn Probability
→ Churn Prediction

Explain WHY probability is useful:

- A binary Yes/No result alone does not show the level of risk.
- Probability allows customers to be ranked according to estimated churn likelihood.
- Higher-risk customers can be prioritized for retention analysis.
- Probability can be used by downstream project components.

Do not present probability values as business certainty. Clearly describe them as model estimates.

---

## 10. Churn Risk Classification

Explain that churn probabilities were converted into practical risk categories:

- Low Risk
- Medium Risk
- High Risk

Final risk distribution:

| Risk Category | Customers |
| Low Risk | 4,489 |
| Medium Risk | 1,344 |
| High Risk | 1,210 |

Explain WHY risk categories were created:

- Business users can understand risk categories more easily than thousands of raw probability values.
- Risk categories support customer prioritization.
- High-risk customers can be considered for retention-focused analysis.

If the actual source code contains exact thresholds, include them. Otherwise do not invent thresholds.

---

## 11. Confusion Matrix Analysis

Explain the final confusion matrix using these values:

True Negatives = 4,797
False Positives = 377
False Negatives = 622
True Positives = 1,247

Create a table:

| | Predicted No Churn | Predicted Churn |
| Actual No Churn | 4,797 | 377 |
| Actual Churn | 622 | 1,247 |

Explain:

True Negative:
Actual non-churn customer correctly predicted as non-churn.

False Positive:
Actual non-churn customer predicted as churn.

False Negative:
Actual churn customer predicted as non-churn.

True Positive:
Actual churn customer correctly predicted as churn.

Explain WHY confusion matrix analysis is important, especially for understanding false negatives because missed churn customers can represent missed retention opportunities.

---

## 12. ROC Curve Analysis

Explain that an ROC curve was generated to evaluate model discrimination across different probability thresholds.

Final ROC-AUC:

90.92%

Explain that ROC-AUC measures how well the model separates churn customers from non-churn customers.

Do not describe ROC-AUC as "90.92% of predictions are correct." Explain it correctly as a discrimination metric.

---

## 13. Model Performance Reporting

Document the final model metrics:

| Metric | Result |
| Accuracy | 85.82% |
| Precision | 76.79% |
| Recall | 66.72% |
| F1 Score | 71.40% |
| ROC-AUC | 90.92% |

Mention the model reporting files:

reports/model_metrics_long.csv
reports/model_performance.csv
reports/final_dashboard_kpis.csv

Explain WHY structured reports were created:

- Easier review
- Model comparison
- Dashboard integration
- Presentation
- Documentation
- Future maintenance

---

## 14. Churn Prediction Output Generation

Explain that after finalizing the model, customer-level prediction outputs were generated.

The output contains relevant customer-level prediction information such as:

- Customer ID
- Churn probability
- Churn prediction
- Churn risk

Explain WHY:

- The model must generate usable predictions rather than only evaluation scores.
- Customer-level outputs allow downstream components to use the churn results.
- Outputs can support retention, LTV, backend, and dashboard analysis.

Do not claim additional columns unless they actually exist in the project output.

---

## 15. Saving the Final Trained Model

Explain that the trained model was saved using Joblib.

Model path:

models/churn_model.joblib

Explain that the saved model contains the trained preprocessing/model components required for prediction.

The final saved model uses:

Logistic Regression
max_iter=1000
random_state=42

Explain WHY saving the model is important:

- The model does not need to be retrained for every prediction.
- The saved model can be loaded later.
- It provides a reusable artifact for integration with backend/deployment workflows.
- Keeping preprocessing with the model helps maintain consistent prediction behaviour.

---

## 16. Model Validation

Explain that the final model and generated outputs were reviewed and validated.

Validation included checking:

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

Explain WHY:

- To verify that the final outputs are internally consistent.
- To ensure the saved model and generated reports are ready for integration.
- To identify issues before deployment or project review.

Do not claim external production validation unless it actually happened.

---

## 17. Documentation

Explain that I documented the work throughout the development process.

Mention these Role 4 documentation files where applicable:

reports/day8_progress.txt
reports/day9_progress.txt
reports/day9_model_analysis.txt
reports/day10_progress.txt
reports/day10_model_validation.txt

Explain that documentation covers:

- Development progress
- Churn model analysis
- Model validation
- Churn insights
- Deployment preparation

Explain WHY:

- Makes the work traceable.
- Helps teammates understand the work.
- Supports company/internship review.
- Makes future maintenance easier.
- Provides evidence of the development process.

---

## 18. Deployment Preparation

Explain that after model development and validation, the churn model was prepared for integration with the wider project.

Mention:

models/churn_model.joblib

Explain that the wider project contains:

- FastAPI backend
- Power BI dashboard
- LTV component
- Churn prediction component

Explain that my Role 4 contribution supplies the trained churn model and prediction outputs that can be consumed by other project components.

IMPORTANT:
Do NOT claim that I personally deployed the entire application if that was not my responsibility.
Use wording such as:
"deployment preparation and integration readiness."

---

# FINAL MODEL RESULTS

Include this table:

| Metric | Result |
| Accuracy | 85.82% |
| Precision | 76.79% |
| Recall | 66.72% |
| F1 Score | 71.40% |
| ROC-AUC | 90.92% |

Add a short professional interpretation:

"The final model demonstrated strong overall classification performance, with an ROC-AUC of 90.92%, indicating strong ability to distinguish between churn and non-churn customers. Accuracy was 85.82%, while precision and recall provide additional insight into the model's ability to correctly identify predicted and actual churn customers."

Do not overstate the model as production-ready solely based on these metrics.

---

# FINAL CUSTOMER CHURN RESULTS

Include:

| KPI | Value |
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

Explain that these values summarize the final prediction and customer-risk output.

---

# KEY ROLE 4 DELIVERABLES

Organize them into sections:

## Machine Learning
- Feature selection
- Data preparation
- Numerical/categorical feature handling
- Preprocessing pipeline
- Logistic Regression
- Random Forest
- XGBoost
- Model evaluation
- Model validation

## Prediction
- Churn prediction
- Churn probability generation
- Churn risk classification
- Customer-level prediction output

## Evaluation
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

## Saved Model

models/churn_model.joblib

## Reports

reports/model_metrics_long.csv
reports/model_performance.csv
reports/final_dashboard_kpis.csv

## Development Documentation

reports/day8_progress.txt
reports/day9_progress.txt
reports/day9_model_analysis.txt
reports/day10_progress.txt
reports/day10_model_validation.txt

---

# END-TO-END ROLE 4 WORKFLOW

Create a clean Markdown workflow diagram:

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

Make this visually clean in Markdown.

---

# BUSINESS VALUE OF ROLE 4

Write a professional section explaining that the churn model allows the project to move beyond historical reporting toward predictive customer-risk analysis.

Explain that the model can help answer:

- Which customers are likely to churn?
- What is the estimated churn probability?
- Which customers fall into high-risk categories?
- Which customers may require retention attention?
- How can churn probability be combined with customer value/LTV?
- How can customer-level churn predictions support business decision-making?

Explain that the churn prediction component provides the machine learning foundation for the broader Customer Churn Prediction & LTV Engine.

Do not claim that the model guarantees customer retention.

---

# WHAT I LEARNED / TECHNICAL CONTRIBUTION

Add a professional section describing the technical skills gained through this work:

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

Do not exaggerate the level of expertise. Present these as technologies/concepts applied during the project.

---

# VIVA / INTERVIEW EXPLANATION

Add a section titled:

## How I Explain My Role in a Viva

Use this professional paragraph:

"I worked on Role 4, which was the churn prediction model. I selected the relevant customer features, prepared the data for machine learning, handled numerical and categorical features using a preprocessing pipeline, and evaluated Logistic Regression, Random Forest, and XGBoost approaches. I evaluated the model using Accuracy, Precision, Recall, F1 Score, and ROC-AUC, and analysed the confusion matrix and ROC curve. I then generated customer-level churn probabilities and risk classifications, saved the final trained model as churn_model.joblib, validated the outputs and reports, documented the development process, and prepared the model for integration with the wider project's backend, LTV, and dashboard components."

---

# IMPORTANT ACCURACY RULES

Before saving README.md, inspect the actual project files if necessary and make sure the documentation does not contradict them.

Specifically verify:

1. Actual model saved in models/churn_model.joblib.
2. Actual model type.
3. Actual preprocessing pipeline.
4. Actual prediction output columns.
5. Actual report filenames.
6. Actual documentation filenames.
7. Actual metrics.
8. Actual dataset feature names.

If an implementation detail is not confirmed by the source files, describe it generically rather than inventing it.

Do not claim:
- exact scaler settings unless verified
- exact encoder settings unless verified
- exact train/test split unless verified
- exact XGBoost hyperparameters unless verified
- exact Random Forest hyperparameters unless verified
- data cleaning counts unless verified
- production deployment unless verified
- causal relationships between features and churn unless verified

Keep all verified numerical results exactly as provided above.

---

# FINAL README QUALITY REQUIREMENTS

Make the final README:

- Professional
- Human-written
- Clear
- Technically accurate
- Suitable for GitHub
- Suitable for internship/company review
- Suitable for viva preparation
- Easy to scan
- Not overly repetitive
- Properly formatted
- Consistent terminology
- Consistent metric values
- Free of spelling/grammar errors

Do not remove important existing project documentation.

Only expand/update the Role 4 contribution documentation.

After making the changes, review the entire README once and ensure the Role 4 section clearly explains:

WHAT I DID
+
HOW I DID IT
+
WHY I DID IT
+
WHAT THE RESULT WAS
+
HOW IT FITS INTO THE OVERALL PROJECT.
