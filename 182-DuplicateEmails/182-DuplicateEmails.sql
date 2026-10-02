-- Last updated: 02/10/2026, 16:03:53
# Write your MySQL query statement below
select email from Person
group by email
having COUNT(email) > 1;