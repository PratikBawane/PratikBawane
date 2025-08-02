📌 If you're exploring SQL or preparing for interviews, this kind of question is a must-practice! 

# 🛒 SQL Challenge: Identify Users Who Added to Cart After Viewing a Page 
This SQL challenge tackles a common e-commerce analytics use-case: **finding users who performed an 'Add_to_Cart' action strictly after a 'Page_View' on the same day**. Perfect for practicing temporal event analysis and preparing for SQL interviews!

---
## Scenario: 
Given a table `UserActivity` with:
- **UserID**: unique identifier of the user
- **ActionType**: type of action performed (`Page_View`, `Add_to_Cart`, etc.)
- **ActionTimestamp**: timestamp of the action 

## 📘 Problem Statement: 
Write a SQL query to find the UserIDs of all customers who have performed an 'Add_to_Cart' action on the same day as, and strictly after, a 'Page_View' action. Each UserID should appear only once in the result. 

✅ The goal is to identify **UserIDs of customers who performed an `Add_to_Cart` action on the same calendar day as a `Page_View`, but only if the add-to-cart happened strictly *after* the page view**. Each qualifying UserID should appear **only once** in the result.

---

## 💻 SQL Query Solution: 

```
WITH Page_View_Events AS (
  SELECT UserID, ActionType, ActionTimestamp
  FROM UserActivity
  WHERE ActionType = 'Page_View'
),

Add_to_Cart AS (
  SELECT UserID, ActionType, ActionTimestamp
  FROM UserActivity
  WHERE ActionType = 'Add_to_Cart'
)

SELECT DISTINCT UserID
FROM Page_View_Events p
JOIN Add_to_Cart a
  ON p.UserID = a.UserID
  AND TO_VARCHAR(p.ActionTimestamp, 'DD-MM-YYYY') = TO_VARCHAR(a.ActionTimestamp, 'DD-MM-YYYY')
WHERE a.ActionTimestamp > p.ActionTimestamp;
```

🧠 Key Takeaways:
✅ Mastering window functions and date manipulation is crucial in real-world SQL analytics.
✅ Challenges like these teach temporal event analysis, a critical skill for BI, data science, and engineering roles.
✅ This logic can directly power features like funnel analysis in e-commerce!

Here's the LinkedIn link to connect with me: <a href="https://www.linkedin.com/in/pratik-bawane-5529901b9/">Click to connect<a/> <br> 

💬 Have you faced similar SQL challenges? Share your approach below!
#SQL #SQLQueries #DataAnalytics #Ecommerce #PageView #AddToCart #LearningByDoing #SQLInterview #DataEngineering #PratikBawane #LinkedInLearning 
