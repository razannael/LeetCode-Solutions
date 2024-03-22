# Write your MySQL query statement below
SELECT person.firstName, person.lastName, address.city, address.state 
FROM person 
LEFT JOIN address 
on person.personId = address.personId;