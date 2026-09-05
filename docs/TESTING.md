# API Testing Documentation

## Project
Customer Churn & LTV Prediction API

## Testing Objective
The objective of testing was to verify that all API endpoints function correctly, handle requests appropriately, and return expected responses.

## Testing Environment

- Framework: FastAPI
- API Documentation: Swagger UI
- Testing Method: Manual API Testing
- Local URL: http://127.0.0.1:8000/docs
- Container URL: http://127.0.0.1:8001/docs
- Containerization: Docker



# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API root endpoint |
| GET | `/health` | API health check |
| POST | `/predict` | Predict churn for one customer |
| POST | `/batch_predict` | Predict churn for multiple customers |


## Functional Testing

| Test ID | Endpoint | Test Scenario | Expected Result | Actual Result | Status |
|--------|----------|---------------|-----------------|---------------|--------|
| TC001 | GET `/` | Normal request | Successful API response | API returned 200 OK successfully | PASS |
| TC002 | GET `/health` | Health check | API returns `healthy` status | API returned 200 OK with `{"status":"healthy"}` | PASS |
| TC003 | POST `/predict` | Valid customer data | Prediction generated successfully | API returned prediction successfully with status 200 | PASS |
| TC004 | POST `/predict` | Empty request | Validation error returned | API returned 422 Unprocessable Entity | PASS |
| TC005 | POST `/predict` | Missing required field | Validation error returned | API returned 422 Unprocessable Entity | PASS |
| TC006 | POST `/predict` | Invalid data type | Validation error returned | API returned 422 Unprocessable Entity | PASS |
| TC007 | POST `/predict` | Negative input values | API should reject invalid negative values | API accepted negative values and returned a prediction with status 200 | FAIL |
| TC008 | POST `/predict` | Boundary values (zero values) | API handles boundary values without crashing | API returned a prediction successfully | PASS |
| TC009 | POST `/predict` | Prediction logic branch 1 | Returns `Yes` with probability `0.8` | API returned `Yes` with probability `0.8` and status 200 | PASS |
| TC010 | POST `/predict` | Prediction logic branch 2 | Returns `Yes` with probability `0.6` | API returned `Yes` with probability `0.6` and status 200 | PASS |
| TC011 | POST `/predict` | Prediction logic else branch | Returns `No` with probability `0.2` | API returned `No` with probability `0.2` and status 200 | PASS |
| TC012 | POST `/batch_predict` | Single customer | One prediction generated successfully | API returned 200 OK with `total_customers: 1` and one prediction | PASS |
| TC013 | POST `/batch_predict` | Multiple customers | Predictions generated for all customers | API returned 200 OK and predictions for all input customers | PASS |
| TC014 | POST `/batch_predict` | Empty batch | API handles empty list gracefully | API returned 200 OK with `total_customers: 0` and an empty predictions list | PASS |
| TC015 | POST `/batch_predict` | Invalid customer data in batch | Validation error returned | API returned 422 Unprocessable Entity for invalid data | PASS |
| TC016 | POST `/batch_predict` | Output count validation | Number of outputs equals number of inputs | 3 inputs produced 3 predictions | PASS |
| TC017 | POST `/batch_predict` | Same input repeated | Same input should produce consistent predictions | API returned identical predictions for identical customer inputs | PASS |

# Prediction Logic Testing

The prediction endpoint was tested with different customer values to verify all branches of the prediction logic.

## High Churn Risk

Input:

```json
{
  "tenure": 10,
  "monthly_charges": 80,
  "total_charges": 800
}
```

Expected Result:

```json
{
  "churn_prediction": "Yes",
  "churn_probability": 0.8
}
```

Actual Result: API returned the expected prediction with status 200.

Status: PASS

## Medium Churn Risk

Input:

```json
{
  "tenure": 18,
  "monthly_charges": 65,
  "total_charges": 1170
}
```

Expected Result:

```json
{
  "churn_prediction": "Yes",
  "churn_probability": 0.6
}
```

Actual Result: API returned the expected prediction with status 200.

Status: PASS

## Low Churn Risk

Input:

```json
{
  "tenure": 30,
  "monthly_charges": 50,
  "total_charges": 1500
}
```

Expected Result:

```json
{
  "churn_prediction": "No",
  "churn_probability": 0.2
}
```

Actual Result: API returned the expected prediction with status 200.

Status: PASS

---

# Docker Deployment Testing

The FastAPI application was containerized and tested using Docker to verify that the application works correctly in a containerized environment.

## Docker Image Build

Command Used:

```bash
docker build -t churn-api .
```

Expected Result:
Docker image should build successfully without errors.

Actual Result:
The Docker image churn-api:latest was built successfully.

Status: PASS

## Docker Container Execution

Command Used:

docker run -p 8001:8000 churn-api

Expected Result:
The FastAPI application should start successfully inside the Docker container.

Actual Result:
The container started successfully and Uvicorn was running on port 8000 inside the container.

Status: PASS

## Port Mapping Verification

The Docker container was configured with the following port mapping:

Host Machine Port 8001 → Docker Container Port 8000

The containerized API was successfully accessed at:

http://127.0.0.1:8001/docs

Expected Result:
Swagger UI should be accessible through the mapped host port.

Actual Result:
Swagger UI was successfully accessible through http://127.0.0.1:8001/docs.

Status: PASS

## Container API Testing

After containerization, the following API endpoints were tested again:

| Endpoint | Result |
|----------|--------|
| GET `/` | PASS |
| GET `/health` | PASS |
| POST `/predict` | PASS |
| POST `/batch_predict` | PASS |

All tested endpoints returned expected responses while running inside the Docker container.

Status: PASS


# Testing Summary

| Testing Category | Result |
|-----------------|--------|
| Root Endpoint Testing | PASS |
| Health Endpoint Testing | PASS |
| Valid Input Testing | PASS |
| Empty Input Testing | PASS |
| Missing Field Testing | PASS |
| Invalid Data Type Testing | PASS |
| Negative Input Validation | FAIL |
| Boundary Value Testing | PASS |
| Prediction Logic Testing | PASS |
| Batch Prediction Testing | PASS |
| Docker Image Build | PASS |
| Docker Container Execution | PASS |
| Container API Testing | PASS |

## Issues Identified

The API returned a successful prediction instead of rejecting the invalid input.

This indicates that input constraints for non-negative values are currently not implemented.

### Negative Input Validation

During testing, the API accepted negative values for `tenure`, `monthly_charges`, and `total_charges`.

Example:

```json
{
  "tenure": -5,
  "monthly_charges": -70,
  "total_charges": -500
}
```

# Conclusion

The Customer Churn & LTV Prediction API was successfully tested using Swagger UI.

Functional testing was performed for API endpoints, valid and invalid inputs, prediction logic branches, batch predictions, and output consistency.

The application was also successfully containerized using Docker. The Docker image was built successfully, the container executed successfully, and all API endpoints were verified after containerization.

One input validation issue was identified: the API currently accepts negative values for customer data fields without validation.