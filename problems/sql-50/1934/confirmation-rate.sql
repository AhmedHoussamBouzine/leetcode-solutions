
SELECT s.user_id , IFNULL(ROUND(AVG(c.action = 'confirmed'), 2), 0) AS confirmation_rate
FROM Signups s 
LEFT JOIN Confirmations c ON s.user_id = c.user_id 
GROUP BY 1;
