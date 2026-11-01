-- Last updated: 01/11/2026, 23:21:15
SELECT player_id, min(event_date)
AS first_login
FROM Activity
GROUP BY player_id