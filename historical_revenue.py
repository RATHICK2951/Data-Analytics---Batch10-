import pandas as pd

# -------------------- Load Excel File --------------------
df = pd.read_excel(
    r"C:\customer\Telco_Customer_Churn_with_LTV_Added-1.xlsx"
)
print("Dataset loaded successfully.")
print("Original shape:", df.shape)

# -------------------- Convert TotalCharges to Numeric --------------------

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# -------------------- Calculate Historical Revenue --------------------

# Use actual TotalCharges when available

df["Historical_Revenue"] = df["TotalCharges"]

# If TotalCharges is missing,
# estimate using MonthlyCharges × tenure

missing = df["Historical_Revenue"].isna()

df.loc[missing, "Historical_Revenue"] = (
    df.loc[missing, "MonthlyCharges"]
    * df.loc[missing, "tenure"]
)

# -------------------- Create Final DataFrame --------------------

historical_revenue_df = df[
    [
        "customerID",
        "Historical_Revenue"
    ]
].copy()

# -------------------- Check Missing Values --------------------

missing_count = historical_revenue_df[
    "Historical_Revenue"
].isna().sum()

print("\nMissing Historical Revenue:", missing_count)


# -------------------- Display Results --------------------

print("\nHistorical Revenue Results")
print("--------------------------")

print(
    historical_revenue_df.head(10)
)


# -------------------- Save Excel File --------------------

output_file = (
    r"C:\customer\Historical_Revenue_Per_Customer.xlsx"
)

historical_revenue_df.to_excel(
    output_file,
    index=False
)

print("\nHistorical revenue calculated successfully.")
print("Output file:", output_file)