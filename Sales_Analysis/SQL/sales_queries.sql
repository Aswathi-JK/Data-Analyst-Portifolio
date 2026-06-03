-- Total sales
SELECT SUM(SALES) AS Total_sales FROM sales;

-- Total Profit
SELECT SUM(PROFIT) AS Total_Profits FROM sales;

-- Total Orders
SELECT COUNT(*) AS Total_Orders
FROM sales;

-- Sales by Region
SELECT REGION, ROUND(SUM(SALES), 0) AS Total_sales
FROM sales
GROUP BY REGION
ORDER BY Total_sales DESC;

-- Profit by Region
SELECT Region, ROUND(SUM(PROFIT)) AS Total_profit
FROM sales
GROUP BY REGION 
ORDER BY Total_profit DESC;

-- Sales by Category
SELECT PRODUCT_CATEGORY, ROUND(SUM(SALES), 0) AS Total_sales
FROM sales
GROUP BY PRODUCT_CATEGORY
ORDER BY Total_sales DESC;
 
-- Top 10 Products by Sales
SELECT PRODUCT_NAME, ROUND(SUM(SALES), 0) AS Total_sales
FROM sales
GROUP BY PRODUCT_NAME
ORDER BY Total_sales DESC
LIMIT 10;

-- Loss-Making Products
SELECT PRODUCT_NAME, PROFIT
FROM sales
WHERE PROFIT < 0;

-- Average Sales by Category
SELECT PRODUCT_CATEGORY, ROUND(AVG(SALES), 0) AS Average_Sale
FROM sales
GROUP BY PRODUCT_CATEGORY
ORDER BY Average_Sale DESC;

