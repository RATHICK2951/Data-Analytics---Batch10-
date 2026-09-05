# API Testing Checklist

This checklist was used to verify the functionality of the Customer Churn & LTV Prediction API.

## API Availability

- [x] FastAPI server starts successfully
- [x] Swagger UI is accessible
- [x] Root endpoint responds successfully
- [x] Health endpoint returns healthy status

## Single Prediction Testing

- [x] Valid customer data tested
- [x] Empty request tested
- [x] Missing required fields tested
- [x] Invalid data types tested
- [x] Negative input values tested
- [x] Boundary values tested
- [x] High churn prediction logic tested
- [x] Medium churn prediction logic tested
- [x] Low churn prediction logic tested

## Batch Prediction Testing

- [x] Single customer batch tested
- [x] Multiple customer batch tested
- [x] Empty batch tested
- [x] Invalid customer data tested
- [x] Output count validation tested
- [x] Repeated identical inputs tested

## Docker Deployment Testing

- [x] Docker image built successfully
- [x] Docker container started successfully
- [x] Port mapping verified
- [x] Swagger UI accessed from Docker container
- [x] API endpoints tested after containerization

## Issue Verification

- [x] Input validation issue identified
- [x] Negative values accepted by API
- [x] Issue documented in testing documentation

## Final Verification

- [x] Functional testing completed
- [x] Deployment testing completed
- [x] Testing results documented
- [x] PASS and FAIL results recorded