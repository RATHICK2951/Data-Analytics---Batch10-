# API Request and Response Examples

This document contains example requests and responses for the Customer Churn & LTV Prediction API.

---

## 1. Health Check

### Endpoint

GET /health

### Expected Response

```json
{
  "status": "healthy"
}
2. Single Customer Prediction
Endpoint

POST /predict

Request
{
  "tenure": 10,
  "monthly_charges": 80,
  "total_charges": 800
}
Response
{
  "churn_prediction": "Yes",
  "churn_probability": 0.8
}
3. Low Churn Prediction
Endpoint

POST /predict

Request
{
  "tenure": 30,
  "monthly_charges": 50,
  "total_charges": 1500
}
Response
{
  "churn_prediction": "No",
  "churn_probability": 0.2
}
4. Batch Prediction
Endpoint

POST /batch_predict

Request
[
  {
    "tenure": 10,
    "monthly_charges": 80,
    "total_charges": 800
  },
  {
    "tenure": 30,
    "monthly_charges": 50,
    "total_charges": 1500
  }
]
Expected Response Structure
{
  "total_customers": 2,
  "predictions": [
    {
      "customer": {},
      "prediction": {}
    }
  ]
}
5. Invalid Request Example
Endpoint

POST /predict

Invalid Request
{
  "tenure": "invalid",
  "monthly_charges": 80,
  "total_charges": 800
}
Expected Result

The API should return:

Status code: 422
Validation error message
