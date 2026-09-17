# Customer Churn Prediction & Lifetime Value (LTV) Engine
## Project Overview

Customer churn is an important problem for businesses because losing existing customers can affect revenue and long-term growth.
This project focuses on analyzing customer data to identify customers who are likely to churn and estimate their Customer Lifetime Value (LTV).
The project covers the complete data analytics workflow, starting from data collection and preprocessing, followed by exploratory data analysis, machine learning-based churn prediction, LTV estimation, SHAP-based model interpretation, and retention analysis.
The main goal of the project is to identify high-risk customers and understand their potential value so that businesses can make better customer retention decisions.
##  Problem Statement

Customer churn can lead to loss of revenue and increased costs for businesses.
The objective of this project is to analyze customer information and identify the factors associated with customer churn. The project also aims to predict the probability of a customer churning and estimate the customer's lifetime value based on historical revenue.
By combining churn prediction with customer value and retention analysis, the project helps identify customers who may need greater retention attention.
##  Objectives

- Clean and preprocess the customer churn dataset.
- Store and manage customer data using PostgreSQL.
- Perform Exploratory Data Analysis (EDA).
- Identify important factors associated with customer churn.
- Build machine learning models for churn prediction.
- Compare different classification models.
- Estimate Customer Lifetime Value using historical revenue.
- Use SHAP for model explainability.
- Identify high-risk and high-value customers.
- Generate retention priorities and recommended actions.
- Prepare the processed data for visualization and further use.
##  Dataset

The project uses a Telco Customer Churn dataset containing **7,043 customers**.
The dataset contains information about:

- Customer demographics
- Customer tenure
- Services subscribed
- Contract type
- Payment method
- Monthly charges
- Total charges
- Churn information
- Customer Lifetime Value (CLTV)

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- PostgreSQL
- Jupyter Notebook
- Git & GitHub
- IBM Cognos Analytics

## Dashboard Overview

The project includes interactive dashboards developed using **IBM Cognos Analytics** to present the key findings from the customer churn and LTV analysis.

The dashboards provide a visual overview of **customer churn patterns, churn risk, customer lifetime value (LTV), and retention insights**. They bring together the results from the data analysis and machine learning stages into an easy-to-understand business analytics view.

### Dashboard Pages

- **Customer Churn Overview** – Provides an overall view of the customer base and highlights major churn patterns across different customer characteristics.
- **Churn Risk Analysis** – Focuses on customer churn risk and the factors associated with higher churn, helping identify customer groups that may require attention.
- **LTV & Retention Analysis** – Presents customer lifetime value, LTV segments, retention priority, and recommended retention actions to support customer retention analysis.

The dashboard uses the processed customer data along with the churn-risk, LTV, and retention datasets generated during the project.

> **Tool used:** IBM Cognos Analytics
  

##  Project Workflow

Customer Churn Dataset
        ↓
Data Collection
        ↓
PostgreSQL Database
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Churn Prediction
        ↓
Model Evaluation
        ↓
LTV Prediction
        ↓
SHAP Explainability
        ↓
Retention Analysis
        ↓
Visualization
