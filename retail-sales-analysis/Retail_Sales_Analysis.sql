USE RetailSalesDB;
GO
-- ============================================
-- Retail Sales Analysis Project
-- Author: Niranjana Arasu
-- Database: RetailSalesDB
-- Dataset: Sample Superstore
-- ============================================

USE RetailSalesDB;
GO
-- Query 1: Total Sales - Business Question - What is the total revenue generated?
SELECT SUM(Sales) AS Total_Sales
From dbo.SampleSuperstore;
GO
-- Query 2: Total Profit - What is the overall profit?
Select Sum(Profit) AS Total_Profit
FROM dbo.SampleSuperstore;
GO
-- Query 3: Total Orders - How many orders were placed?
SELECT COUNT(*) AS Total_Orders
FROM dbo.SampleSuperstore;
GO
-- Query 4: Orders by Category - Which product category generates the highest sales and profit?
SELECT 
   Category,
   ROUND(SUM(Sales),2) AS Total_Sales,
   ROUND(SUM(Profit),2) AS Total_Profit
FROM dbo.SampleSuperstore
GROUP BY Category
ORDER BY Total_Sales DESC;
GO
--Query 5: Sales by Region - Which region performs the best?
SELECT 
   Region,
   ROUND(SUM(Sales),2) AS Total_Sales,
   ROUND(SUM(Profit),2) AS Total_Profit
FROM dbo.SampleSuperstore
GROUP BY Region
ORDER BY Total_Sales DESC;
GO
