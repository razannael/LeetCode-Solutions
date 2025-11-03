WITH meetingStats AS (
    SELECT employee_id, SUM(duration_hours) AS total_hour, YEARWEEK(meeting_date, 3) AS weeks
    FROM meetings
    GROUP BY employee_id, weeks
),
heavyMeetings AS (
    SELECT *, COUNT(*) AS meeting_heavy_weeks
    FROM meetingStats
    WHERE total_hour > 20 
    GROUP BY employee_id 
    HAVING COUNT(*) >= 2
)
SELECT employee_id, employee_name, department, meeting_heavy_weeks
FROM heavyMeetings
LEFT JOIN employees 
USING( employee_id)
ORDER BY meeting_heavy_weeks DESC, employee_name