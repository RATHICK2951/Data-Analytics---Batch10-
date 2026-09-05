# Known Issues and Testing Findings

This document records issues identified during testing of the Customer Churn & LTV Prediction API.

## Issue 1: Negative Input Values Are Accepted

### Description

During API testing, negative values were provided for customer data fields.

Example request:

```json
{
  "tenure": -5,
  "monthly_charges": -70,
  "total_charges": -500
}
Expected Behavior

The API should reject negative values because negative tenure, monthly charges, and total charges are not valid customer data.

A validation error with status code 422 would be expected.

Actual Behavior

The API accepted the negative values and returned:

Status code: 200 OK
Churn prediction: No
Churn probability: 0.2
Impact

Invalid customer data can be processed by the prediction logic, which may produce unreliable results.

Suggested Improvement

Add validation constraints to the Pydantic model.

Example:

from pydantic import BaseModel, Field

class CustomerData(BaseModel):
    tenure: float = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    total_charges: float = Field(ge=0)

The ge=0 constraint ensures that values must be greater than or equal to zero.

Testing Status

The issue was identified during functional testing and documented for future improvement.

The API continues to function correctly for valid input data.
