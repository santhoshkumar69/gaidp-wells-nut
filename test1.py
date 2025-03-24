import pandas as pd
import re

dff = pd.read_csv("loan_data_fields_filtered.csv")


def detect_pattern(value):
    """Identify common patterns using regular expressions."""

    for field_Name, regex in dff.items():
        if re.match(field_Name, str(value)):
            return field_Name
    return "Unknown"


def generate_data_profile(df):
    """Generate a data profile with RegEx pattern detection."""
    profile = {}

    for column in df.columns:
        sample_values = df[column].dropna().astype(str).tolist()[:20]  # Sample data for detection

        detected_patterns = [detect_pattern(val) for val in sample_values]
        print('detected patterns:', detected_patterns)
        most_common_pattern = max(set(detected_patterns), key=detected_patterns.count)

        profile[column] = {
            "Data Type": str(df[column].dtype),
            # "Missing Values": df[column].isnull().sum(),
            # "Unique Values": df[column].nunique(),
            "Detected Pattern": most_common_pattern
        }

    return pd.DataFrame.from_dict(profile, orient="index")


# Load dataset
df = pd.read_csv("bank_patterns_sample_matching_regex.csv")

# Generate profile
profile_df = generate_data_profile(df)
print(profile_df)

