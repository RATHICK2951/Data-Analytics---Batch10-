# API Reference

## Base URL

Local:

http://127.0.0.1:8000

Docker:

http://127.0.0.1:8001

---

## GET /

Returns the API status message.

### Expected Response

```json
{
  "message": "Customer Churn & LTV API is running",
  "status": "success"
}

GET /health

Checks whether the API is healthy.

Expected Response
{
  "status": "healthy"
}
### POST /predict

Predicts customer churn for a single customer.

Request Body
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
### POST /batch_predict

Predicts churn for multiple customers.

Request Body
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
### Response

The API returns:

Total number of customers processed
Input customer details
Churn prediction
Churn probability