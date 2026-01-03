# data_engine/validator.py
def validate_dataset(df):
    issues = []

    if df.empty:
        issues.append("Dataset is empty")

    if df.shape[1] < 2:
        issues.append("Dataset must have at least 2 columns")

    if df.isnull().sum().sum() > 0:
        issues.append("Missing values detected")

    return issues
