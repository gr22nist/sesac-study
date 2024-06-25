-- select o.userid, sum(cast(i.UnitPrice as integer))
-- from orders od
-- join orderitems odi on od.id = odi.orderid
-- join items i on odi.itemid = i.id
-- where od.userid = '0a497257-2b1a-4836-940f-7b95db952e61'

.headers on

select od.userid, sum(cast(i.UnitPrice as integer)) AS revenue
from users u
join orders od on u.id = od.userid
join orderitems odi on od.id = odi.orderid
join items i on odi.itemid = i.id
group by od.userid
order by revenue desc
limit 10;

-- sqlite3 db명 < sql파일명