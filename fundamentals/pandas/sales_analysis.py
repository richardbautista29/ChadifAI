import pandas as pd

# Load data
df = pd.read_csv("sales.csv")

# Create total column
df["Total"] = df["Price"] * df["Quantity"]

# Basic outputs
print("=== DATA ===")
print(df)

print("\n=== TOTAL SALES ===")
print(f"₱{df['Total'].sum():,}")

print("\n=== SALES PER PRODUCT ===")
sales_per_product = df.groupby("Product")["Total"].sum()
print(sales_per_product.sort_values(ascending=False))

print("\n=== BEST SELLING PRODUCT ===")
print(df.groupby("Product")["Quantity"].sum().idxmax())

print("\n=== BEST SALES DAY ===")
print(df.groupby("Date")["Total"].sum().idxmax())

print("\n=== SALES PER DAY ===")
print(df.groupby("Date")["Total"].sum())