WITH PositiveDates AS
(SELECT patient_id, MIN(test_date) AS positive_date
FROM covid_tests 
WHERE result LIKE 'Positive'
GROUP BY patient_id),
NegativeAfterPositiveDates AS 
(SELECT pd.*, MIN(ct.test_date) AS negative_date
FROM PositiveDates AS pd
LEFT JOIN covid_tests AS ct
ON(pd.patient_id = ct.patient_id AND pd.positive_date < ct.test_date )
WHERE ct.result LIKE 'Negative'
GROUP BY patient_id)

SELECT p.patient_id, patient_name, age, DATEDIFF(negative_date, positive_date) AS recovery_time
FROM NegativeAfterPositiveDates
JOIN patients AS p 
USING(patient_id)
ORDER BY recovery_time ASC, patient_name ASC