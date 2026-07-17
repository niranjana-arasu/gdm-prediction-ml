Retail Sales Analysis using SQL & Power BI

📌 Overview

This project analyzes retail sales data using SQL Server and Power BI to uncover key business insights. SQL was used to import, clean, and query the dataset, while Power BI was used to build an interactive dashboard for visualizing trends across sales, profit, and customer behavior.

🧩 Problem Statement

The Superstore dataset shows strong topline sales, but profitability is inconsistent across product categories and regions — with nearly 1 in 5 orders operating at a loss. This project uses SQL to quantify where the sales-to-profit relationship breaks down (by category, sub-category, region, and discount level) and Power BI to surface those patterns visually, so leadership can identify which segments need pricing or discount corrections.

🎯 Objectives

Import and structure raw retail sales data in SQL Server
Write queries to calculate core business metrics
Identify patterns in sales, profit, and shipping performance
Build an interactive Power BI dashboard for stakeholders

🛠️ Skills Used

SQL Server
SQL Server Management Studio (SSMS)
Power BI
Data Analysis
Data Visualization
Business Insights

📊 Key Metrics Analysed

Total Sales
Total Profit
Order Count
Sales by Category
Profit by Region
Sales by Shipping Mode

Insights Found

Overall business profit margin stands at 12.49% across 9,994 orders, with total sales of $2.29M and total profit of $286.8K.
Furniture generates nearly as much in sales as Technology (~$742K vs ~$836K) but converts it into only a 2.54% profit margin, compared to 17.4% for Technology and 17.04% for Office Supplies — Furniture is the clear underperformer.
Within Furniture, Tables (-8.36% margin) and Bookcases (-3.02% margin) are actively losing money on every sale, dragging down the whole category.
18.71% of all orders (1,870 of 9,994) are loss-making, indicating a meaningful chunk of transactions where cost exceeds revenue.
Central region posts the lowest total profit (~$39.7K) despite mid-range sales (~$501K), underperforming West (~$108.4K profit) and East (~$91.5K profit) on a profit-per-sale basis.
Furniture's average discount (17.39%) is only slightly above Office Supplies (15.73%) and Technology (13.23%), suggesting the losses come more from product-level pricing/cost issues in Tables and Bookcases than from blanket over-discounting.
