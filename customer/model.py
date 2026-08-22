# -------------------- Import Libraries --------------------

import pandas as pd
import numpy as np
import pickle
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)


# -------------------- Load Dataset --------------------

data_frame = pd.read_excel(
    Path(__file__).with_name(
        'Telco_Customer_Churn_with_LTV_Added-1.xlsx'
    )
)

print("Dataset loaded successfully.")
print("Dataset shape:", data_frame.shape)


# -------------------- Create LTV Segmentation --------------------
# Thresholds are calculated from the actual LTV values

low_threshold = data_frame['LTV'].quantile(0.33)
high_threshold = data_frame['LTV'].quantile(0.66)

print("\nLTV Segmentation Thresholds:")
print("Low    :", low_threshold)
print("Medium :", high_threshold)


def segment_ltv(ltv):
    if ltv <= low_threshold:
        return "Low"
    elif ltv <= high_threshold:
        return "Medium"
    else:
        return "High"


# Add segmentation to original dataset
data_frame['LTV_Segment'] = data_frame['LTV'].apply(segment_ltv)

print("\nActual LTV Segment Distribution:")
print(data_frame['LTV_Segment'].value_counts())


# -------------------- Separate Features and Target --------------------

# LTV_Segment is NOT used as a feature because
# it is created directly from LTV.

X = data_frame.drop(
    columns=[
        'LTV',
        'LTV_Segment',
        'customerID',
        'TotalCharges'
    ]
)

y = data_frame['LTV']


# -------------------- Train-Test Split --------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape :", X_test.shape)


# -------------------- Identify Categorical Columns --------------------

categorical_columns = X_train.select_dtypes(
    include='object'
).columns


# -------------------- Create Preprocessor --------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            'categorical',
            OneHotEncoder(
                handle_unknown='ignore',
                sparse_output=False
            ),
            categorical_columns
        )
    ],
    remainder='passthrough'
)


# -------------------- Transform Training Data --------------------

X_train_transformed = preprocessor.fit_transform(
    X_train
)


# -------------------- Transform Testing Data --------------------

X_test_transformed = preprocessor.transform(
    X_test
)


# -------------------- Create Model --------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# -------------------- Train Model --------------------

model.fit(
    X_train_transformed,
    y_train
)

print("\nModel training completed.")


# -------------------- Prediction --------------------

y_pred = model.predict(
    X_test_transformed
)


# -------------------- Model Evaluation --------------------

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

mae = mean_absolute_error(
    y_test,
    y_pred
)

r2 = r2_score(
    y_test,
    y_pred
)

print("\nModel Evaluation")
print("-------------------------")
print("RMSE:", rmse)
print("MAE :", mae)
print("R2  :", r2)


# -------------------- Predicted LTV Segmentation --------------------

predicted_segments = [
    segment_ltv(ltv)
    for ltv in y_pred
]


# -------------------- Create Prediction Results --------------------

results = X_test.copy()

results['Actual_LTV'] = y_test.values
results['Predicted_LTV'] = y_pred
results['LTV_Segment'] = predicted_segments


# -------------------- Display Results --------------------

print("\nCustomer LTV Predictions and Segmentation")
print("------------------------------------------")

print(
    results[
        [
            'Actual_LTV',
            'Predicted_LTV',
            'LTV_Segment'
        ]
    ].head(20)
)


# -------------------- Segment Distribution --------------------

print("\nPredicted LTV Segment Distribution:")
print(
    results['LTV_Segment'].value_counts()
)


# -------------------- Save Prediction Results --------------------

results.to_excel(
    'LTV_Customer_Segmentation_Results.xlsx',
    index=False
)

print(
    "\nPrediction results saved as: "
    "LTV_Customer_Segmentation_Results.xlsx"
)


# -------------------- Save Model and Preprocessor --------------------

model_data = {
    "model": model,
    "preprocessor": preprocessor,
    "low_threshold": low_threshold,
    "high_threshold": high_threshold
}


with open(
    "ltv_random_forest.pkl",
    "wb"
) as file:

    pickle.dump(
        model_data,
        file
    )


print("\nModel and preprocessor saved successfully.")
print("File name: ltv_random_forest.pkl")