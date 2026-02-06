import pandas as pd

# 1. Read CSV
df = pd.read_csv("raw_data.csv")

print("Original Data")
print(df.head())

# 2. Clean column names (safe practice)
df.columns = df.columns.str.strip().str.lower()

# 3. Convert date columns
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
df['dob'] = pd.to_datetime(df['dob'], dayfirst=True, errors='coerce')

# 4. Remove duplicate rows
df = df.drop_duplicates()

# 5. Handle missing values
df['gender'] = df['gender'].fillna('Unknown')
df['price'] = df['price'].fillna(df['price'].mean())
df['quantity'] = df['quantity'].fillna(1)

# 6. Clean text columns
text_cols = ['customer_name', 'product', 'category', 'city']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# 7. Create total_amount column
df['total_amount'] = df['price'] * df['quantity']

print("\nCleaned Data")
print(df.head())

# 8. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\n cleaned_data.csv file created successfully")