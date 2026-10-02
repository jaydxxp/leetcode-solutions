-- Last updated: 02/10/2026, 16:03:50
# Write your MySQL query statement be
SELECT Customers.name as Customers FROM Customers
WHERE id not in (select customerId from Orders)