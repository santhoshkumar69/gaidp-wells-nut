import pandas as pd
import os
import openai

# Load dataset
df = pd.read_csv("allowable_values_full_112.csv")  # Replace with your dataset

# Generate basic profile
def generate_data_profile(df):
    profile = {
        "Columns": list(df.columns),
        "Data Types": df.dtypes.to_dict(),
        "Missing Values": df.isnull().sum().to_dict(),
        "Summary Statistics": df.describe(include='all').to_dict()
    }
    return profile

profile = generate_data_profile(df)

# Convert profile to a readable string
profile_str = "\n".join([f"{k}: {v}" for k, v in profile.items()])
print(profile_str)
# Use LLM to analyze profile (Updated for OpenAI v1.0.0+)
# Set API key securely


openai_client = openai.OpenAI(api_key="test_key")  # Set in system environment
models = openai_client.models.list()
for model in models.data:
    print(model.id)
response = openai_client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{"role": "user", "content": "Summarize this dataset."}],
    max_tokens=500  # Lower this value to reduce cost
)

# Print AI-generated insights
print(response.choices[0].message.content)