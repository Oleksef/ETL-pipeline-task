DELETE FROM users
WHERE domain NOT IN ('google.com', 'yahoo.com', 'hotmail.com');

SELECT *
FROM users;