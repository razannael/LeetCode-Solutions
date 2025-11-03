WITH CTE AS(
	SELECT content_id, content_text,  unnest(string_to_array(REPLACE(content_text,'-','  '), ' ')) AS new_text
	FROM user_content 
)
SELECT content_id, content_text AS original_text , REPLACE( STRING_AGG(UPPER(SUBSTR(new_text,1,1)) || LOWER(SUBSTR(new_text,2, LENGTH(new_text) - 1)), ' ') , ' - ', '-')  AS converted_text
FROM (
	SELECT content_id, content_text, CASE WHEN new_text = '' THEN '-' ELSE new_text END 
	FROM CTE
)sub
GROUP BY content_id, content_text
ORDER BY content_id