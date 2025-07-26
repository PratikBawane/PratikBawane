🔍 SQL Challenge: **Find Users Who Logged In for at least 3 Consecutive Days**

 💻 Querying with MySQL | Window Functions | Date Logic
Recently, I worked on an interesting SQL scenario where I needed to identify users who logged in for 3 consecutive days. Here's how I tackled it using MySQL window functions and some smart logic. 👇 

🧩 Problem: 
Given a **UserLogins** table (📸 see Screenshot 1), identify users who have logged in for at least 3 consecutive days. 
 
🧠 Approach:
I used a common SQL trick: if you subtract the row number from the login date (converted to day), consecutive logins will form groups with the same difference. Here's a breakdown: 

📌 Query Logic: 
```
WITH logins AS (
 SELECT 
 UserID, 
 LoginDate, 
 ROW_NUMBER() OVER(PARTITION BY UserID ORDER BY LoginDate) AS rn,
 DATE_FORMAT(LoginDate, '%d') - ROW_NUMBER() OVER(PARTITION BY UserID ORDER BY LoginDate) AS date_diff
),
consecutive_days AS (
 SELECT * FROM logins
)
SELECT UserID 
FROM consecutive_days 
GROUP BY UserID, date_diff 
HAVING COUNT(date_diff) >= 3; 
```

🔍 Breakdown: 
• CTE logins: Assigns a row number to each login per user based on date.
• date_diff logic: If logins are consecutive, the difference between date and row number remains the same.
• Grouping by UserID and date_diff, and filtering those with count >= 3 gives us users with 3+ consecutive logins. 

✅ Result: User 1001 logged in for at least 3 consecutive days! (📸 Screenshot 3) 

📷 Screenshots: 
🖼️ Screenshot 1: Sample Data (UserLogins table)
🖼️ Screenshot 2: Intermediate step showing row_number and date_diff
🖼️ Screenshot 3: Final result – user(s) who met the condition 

💡This small yet powerful use-case shows how SQL window functions can be leveraged to solve temporal data challenges efficiently! 

🔗 Let me know your thoughts, or if you'd solve it differently! 
You can connect with me on LinkedIn: <a href="https://www.linkedin.com/in/pratik-bawane-5529901b9/" target="_blank">LinkedIn profile</a> <br> 
hashtag#SQL hashtag#MySQL hashtag#WindowFunctions hashtag#DataEngineering hashtag#ConsecutiveLogins hashtag#SQLChallenge hashtag#LearningByDoing hashtag#DataAnalytics hashtag#CodeWithMe hashtag#LinkedInLearning
