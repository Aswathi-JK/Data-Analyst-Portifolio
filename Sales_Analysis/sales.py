import pandas as pd

data = pd.read_csv("C:/Dev/Python_projects/sales_data.csv", encoding = "latin1")

print(data.head())
print(data.columns)
print(data.info())

print("Total Sales =", data["Sales"].sum())
print("Total Profit =", data["Profit"].sum())

region_sales = data.groupby("Region")["Sales"].sum()
region_sales.to_csv("region_sales.csv")
top_region = region_sales.idxmax()
top_region_sales = region_sales.max()
print("Top Region:", top_region)
print("Sales:", top_region_sales)

category_sales = data.groupby("Product Category")["Sales"].sum()
category_sales.to_csv("category_sales.csv")
top_category = category_sales.idxmax()
top_category_sales = category_sales.max()
print("Top Category:", top_category)
print("Sales:", top_category_sales)

loss = data[data["Profit"] < 0]
loss.to_csv("loss_products.csv", index=False)

print(loss[["Product Name", "Profit"]].head())
print(loss[["Product Category", "Profit"]].head())
