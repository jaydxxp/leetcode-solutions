-- Last updated: 01/10/2026, 01:54:30
# Write your MySQL query statement below
select firstName,lastName,city,state from Person left join Address
on Person.PersonId = Address.PersonId;