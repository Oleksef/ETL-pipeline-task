SELECT *
FROM users
WHERE signup_date BETWEEN current_date - 7 AND current_date;


-- SELECT *
-- FROM users
-- WHERE signup_date > current_date - INTERVAL '7 day';