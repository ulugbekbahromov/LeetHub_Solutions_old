# Write your MySQL query statement below
select customer_number
from Orders
group by customer_number
having count(order_number) = (
            select count(*)
            from Orders
            group by customer_number
            order by count(*) desc
            limit 1
);