import pandas as pd

data = pd.read_csv("C:/Dev/Python_projects/sales_data.csv", encoding = "latin1")

print(data.head())
print(data.columns)
print(data.info())

print("Total Sales =", data["Sales"].sum())
print("Total Profit =", data["Profit"].sum())

print(data.groupby("Region")["Sales"].sum())
print(data.groupby("Product Category")["Sales"].sum())

loss = data[data["Profit"]<0]
print(loss[["Product Name", "Profit"]].head())
print(loss[["Product Category", "Profit"]].head())
print(data)