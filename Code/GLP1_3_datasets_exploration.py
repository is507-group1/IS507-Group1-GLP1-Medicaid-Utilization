import pandas as pd

# ---------------------------------------------------------
# 1. Load datasets
# ---------------------------------------------------------

# Medicaid Drug Utilization
medicaid_drug = pd.read_csv("sdud2025_updatedjuly2026.csv")

# BRFSS 2025
brfss = pd.read_sas("LLCP2025.XPT", format="xport")

# Medicaid Enrollment
medicaid_enrollment = pd.read_csv("pi-dataset-september-2026-release.csv")


# ---------------------------------------------------------
# 2. Medicaid Drug Utilization Dataset
# ---------------------------------------------------------

print("\n===== Medicaid Drug Utilization =====")

print("Shape:", medicaid_drug.shape)

print("\nData types:")
print(medicaid_drug.dtypes)

print("\nMissing values:")
print(medicaid_drug.isna().sum())

drug_columns = [
    "State",
    "NDC",
    "Year",
    "Quarter",
    "Product Name",
    "Number of Prescriptions",
    "Suppression Used"
]

print("\nRelevant variables:")
print(medicaid_drug[drug_columns].head())

print("\nSuppression Used values:")
print(medicaid_drug["Suppression Used"].value_counts(dropna=False))


# ---------------------------------------------------------
# 3. BRFSS 2025 Dataset
# ---------------------------------------------------------

print("\n===== BRFSS 2025 =====")

print("Shape:", brfss.shape)

print("\nData types:")
print(brfss.dtypes)

print("\nMissing values:")
print(brfss.isna().sum())

brfss_columns = [
    "_STATE",
    "_BMI5CAT",
    "DIABETE4",
    "_LLCPWT"
]

print("\nRelevant variables:")
print(brfss[brfss_columns].head())


# ---------------------------------------------------------
# 4. Medicaid Enrollment Dataset
# ---------------------------------------------------------

print("\n===== Medicaid Enrollment =====")

print("Shape:", medicaid_enrollment.shape)

print("\nData types:")
print(medicaid_enrollment.dtypes)

print("\nMissing values:")
print(medicaid_enrollment.isna().sum())

enrollment_columns = [
    "State Abbreviation",
    "State Name",
    "Reporting Period",
    "Preliminary or Updated",
    "Final Report",
    "Total Medicaid Enrollment"
]

print("\nRelevant variables:")
print(medicaid_enrollment[enrollment_columns].head())
