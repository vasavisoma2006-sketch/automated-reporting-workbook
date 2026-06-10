import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Total Sales:", df["Sales"].sum())
print("Total Orders:", len(df))

print("\nSales by Region")
print(df.groupby("Region")["Sales"].sum())

print("\nSales by Product")
print(df.groupby("Product")["Sales"].sum())
