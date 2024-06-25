select distinct i.name
from users u
join orders od on u.id = od.userid
join stores st on od.storeid = st.id
join orderitems odi on od.id = odi.orderid
join items i on odi.itemid = i.id
where u.id = '0a497257-2b1a-4836-940f-7b95db952e61'

-- sqlite3 db명 < sql파일명