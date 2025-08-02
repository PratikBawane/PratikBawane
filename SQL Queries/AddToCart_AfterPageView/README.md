📌 If you're exploring SQL or preparing for interviews, this kind of question is a must-practice! 

🛒 SQL Challenge: Identify Users Who Added to Cart After Viewing a Page 
• This SQL challenge tackles a common e-commerce analytics use-case: finding users who performed an 'Add_to_Cart' action strictly after a 'Page_View' on the same day. Perfect for practicing temporal event analysis and preparing for SQL interviews! 


😎 #Scenario: 
Given a table UserActivity(screenshot below) with: 
• UserID: unique identifier of the user
• ActionType: type of action performed (Page_View, Add_to_Cart, etc.)
• ActionTimestamp: timestamp of the action 


📖 #Problem_Statement:
• Write a SQL query to find the UserIDs of all customers who have performed an 'Add_to_Cart' action on the same day as, and strictly after, a 'Page_View' action. Each UserID should appear only once in the result. 


✅ The goal is to identify UserIDs of customers who performed an Add_to_Cart action on the same calendar day as a Page_View, but only if the add-to-cart happened strictly after the page view. Each qualifying UserID should appear only once in the result. 


💻 #SQL_Query_Solution:

```
with Page_View_Events as (
select UserID, ActionType, ActionTimestamp from UserActivity where ActionType = 'Page_View' 
),  

Add_to_Cart as(
select UserID, ActionType, ActionTimestamp from UserActivity where ActionType = 'Add_to_Cart'
)

select distinct p.UserID from Page_View_Events p join Add_to_Cart a on p.UserID = a.UserID and date_format(p.ActionTimestamp, '%d-%m-%y') = date_format(a.ActionTimestamp, '%d-%m-%y')
where a.ActionTimestamp > p.ActionTimestamp; 
```



🧠 #Key_Takeaways: 
✅ Mastering window functions and date manipulation is crucial in real-world SQL analytics. 
✅ Challenges like these teach temporal event analysis, a critical skill for BI, data science, and engineering roles. 
✅ This logic can directly power features like funnel analysis in e-commerce! 

🔗 Please connect with me here on LinkedIn: <a href="https://www.linkedin.com/in/pratik-bawane-5529901b9/" target="_blank">Click to connect<a/> <br> 

😊 Would love to hear your take on this, if you've an alternative approach please share it with the connections! 
