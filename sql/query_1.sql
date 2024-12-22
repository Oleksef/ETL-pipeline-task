SELECT signup_date, count(1)
FROM users
GROUP BY signup_date
--ORDER BY count DESC;