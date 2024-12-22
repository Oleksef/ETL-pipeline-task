WITH common_domain AS (SELECT
    domain, COUNT(domain)
FROM users
GROUP BY domain
ORDER BY count DESC
LIMIT 1)

SELECT users.*
FROM users
JOIN common_domain USING(domain);