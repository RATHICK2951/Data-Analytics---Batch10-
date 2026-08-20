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
    Path(__file__).with_name('Telco_Customer_Churn_with_LTV_Added-1.xlsx')
)

print("Dataset loaded successfully.")
print("Dataset shape:", data_frame.shape)


# -------------------- Separate Features and Target --------------------

X = data_frame.drop(
    columns=[
        'LTV',
        'customerID',
        'TotalCharges',
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


# -------------------- Identify Columns --------------------

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

# transform:
# Uses the categories learned from training data

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


# -------------------- Prediction on Test Data --------------------

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
print('rmse:',rmse)
print('mae:',mae)
print('r2:',r2)
#-------------------- Save Model and Preprocessor --------------------

model_data = {
    "model": model,
    "preprocessor": preprocessor
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