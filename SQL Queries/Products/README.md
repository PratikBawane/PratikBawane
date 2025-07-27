
📌 If you're exploring SQL or preparing for interviews, this kind of question is a must-practice! 

🧾 SQL Case Challenge: **Monthly Sales Breakdown by Product**  
📊 Querying using CASE, SUM, and GROUP BY logic in SQL

Today I tackled a classic yet fundamental SQL scenario — converting rows into columns to summarize monthly product sales. Here’s a quick walk-through of the problem, approach, and solution. 👇

**Scenario: 
You have a table ProductSales(Screenshot1) with columns: ProductID (INT), SaleAmount (DECIMAL), and SaleMonth (VARCHAR, e.g., 'Jan', 'Feb', 'Mar', 'Apr'). 

**Problem Statement: 
Write a SQL query to display the total SaleAmount for each ProductID, with separate columns for the sales of 'Jan', 'Feb', and 'Mar'. Your output should have one row per ProductID and columns for each month(refer Screenshot2).  

**SQL Query: 

```

select ProductID, 

sum(case SaleMonth when 'Jan' then SaleAmount else 0 end) as 'Jan_Sales', 

sum(case SaleMonth when 'Feb' then SaleAmount else 0 end) as 'Feb_Sales', 

sum(case SaleMonth when 'Mar' then SaleAmount else 0 end) as 'Mar_Sales' 

from ProductSales 

group by ProductID;

``` 

🧠 Key Concepts Used: 
🎯 CASE WHEN: Helps transform row values into conditional aggregates.
📦 SUM aggregation: Calculates total sales per month per product.
🧮 GROUP BY: Ensures one row per product with month-wise totals. 

This style of query is often referred to as a pivot in SQL — super useful for dashboarding, reporting, and analytics. 

💡 Why It Matters:
Being able to reshape your data like this is a key skill for:
📈 BI tools like Tableau or Power BI
📊 Monthly trend analysis and reporting
🔄 Data transformation without needing Excel! 

Would love to hear how you would handle it with dynamic SQL or across more months! 
Plz connect with me on LinkedIn: <a href="https://www.linkedin.com/in/pratik-bawane-5529901b9/" target="_blank">Click to connect</a> <br> 

#SQL #SQLQuery #DataAnalytics #Pivot #CaseWhen #SQLAggregation #LearningByDoing #DataEngineering #SQLChallenge #LinkedInLearning
