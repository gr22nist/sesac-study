-- .mode csv
-- .headers on

-- .import users.csv users
-- .import orders.csv orders
-- .import orderitems.csv orderitems
-- .import items.csv items
-- .import stores.csv stores

-- CREATE TABLE IF NOT EXISTS "users"(
--     "Id" TEXT,
--     "Name" TEXT,
--     "Gender" TEXT,
--     "Age" INTEGER,

--     "Birthdate" DATE,
--     "Address" TEXT);

-- CREATE TABLE IF NOT EXISTS "items"(
--     "Id" TEXT,
--     "Name" TEXT,
--     "Type" TEXT,
--     "UnitPrice" INTEGER);


-- CREATE TABLE IF NOT EXISTS "orders"(
--     "Id" TEXT,
--     "OrderAt" DATETIME,
--     "StoreId" TEXT,
--     "UserId" TEXT);

-- CREATE TABLE IF NOT EXISTS "orderitems"(
--     "Id" TEXT,
--     "OrderId" TEXT,
--     "ItemId" TEXT);

-- CREATE TABLE IF NOT EXISTS "stores"(
--     "Id" TEXT,
--     "Name" TEXT,
--     "Type" TEXT,
--     "Address" TEXT);

-- DELETE FROM users where id='Id';
-- DELETE FROM orders where id='Id';
-- DELETE FROM orderitems where id='Id';
-- DELETE FROM items where id='Id';
-- DELETE FROM stores where id='Id';


select * from users where Birthdate <= '2001-01-01';
select * from users where Birthdate between '2001-01-01' and '2001-01-31';
select * from users where strftime('%Y', Birthdate) = '1999';
