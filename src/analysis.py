import pandas as pd

df = pd.read_csv("data/OnlineRetail.csv", encoding="latin1")

print(df.head())
print(df.info())

df.isnull().sum()
df = df.dropna(subset=["CustomerID"])

df = df[df["Quantity"] > 0]

df = df[df["UnitPrice"] > 0]

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print(df["Revenue"].sum())

print(df["InvoiceNo"].nunique())

print(df["CustomerID"].nunique())

top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

print(top_products)

top_revenue = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)

print(top_revenue)

country = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False)

print(country)

import matplotlib.pyplot as plt

top_products.plot(kind="bar", figsize=(10,5))
plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=90)
plt.show()

country.head(5).plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Top 5 Countries Revenue")
plt.show()

duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

df = df.drop_duplicates()

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Revenue"].sum()

print(monthly_sales)

monthly_sales.plot(figsize=(10,5), marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)

plt.show()

top_country = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)

top_country.plot(kind="bar", figsize=(10,5))

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.show()

plt.savefig("images/top_products.png")

plt.savefig("images/country_revenue.png")
plt.savefig("images/monthly_sales.png")