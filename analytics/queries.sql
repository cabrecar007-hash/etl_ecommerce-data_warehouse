-- Total sales per store per day
SELECT store_id, DATE(datetime) as day, SUM(amount) as total_sales
FROM dw_user_logs
WHERE action_type = 'buy'
GROUP BY store_id, day
ORDER BY day;

-- Active users per day
SELECT store_id, DATE(datetime) as day, COUNT(DISTINCT user_id) as active_users
FROM dw_user_logs
GROUP BY store_id, day;
