WITH three_unique_subject_2_times AS (
    SELECT student_id FROM study_sessions GROUP BY student_id HAVING COUNT(DISTINCT(subject))>2
    AND student_id 
    NOT IN (SELECT DISTINCT(student_id) FROM study_sessions GROUP BY student_id,subject HAVING COUNT(*)<2)
),
consecutive_dates AS (
    SELECT student_id
    FROM (
        SELECT student_id,subject,
        DATEDIFF(session_date,LAG(session_date,1) OVER (PARTITION BY student_id ORDER BY session_date)) AS gaps
        FROM study_sessions
    ) AS consecutive_dates
    GROUP BY student_id
    HAVING MAX(gaps) <3
),
study_spiral_pattern AS (
    SELECT s.student_id,
    s.student_name,
    s.major, 
    COUNT(DISTINCT(ss.subject)) AS cycle_length,
    SUM(ss.hours_studied) AS total_study_hours,
    COUNT(s.student_id) OVER() AS unique_students
    FROM students AS s
    JOIN study_sessions AS ss
    ON s.student_id = ss.student_id
    GROUP BY s.student_id
    HAVING s.student_id IN (SELECT * FROM three_unique_subject_2_times)
    AND s.student_id IN (SELECT * FROM consecutive_dates)
    ORDER BY cycle_length DESC,total_study_hours DESC
)
SELECT student_id,student_name,major,cycle_length,total_study_hours
FROM study_spiral_pattern
WHERE unique_students>1;