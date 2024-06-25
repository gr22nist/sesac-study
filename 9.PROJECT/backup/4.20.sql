select * from users
where cast(age as integer) between 20 and 29
limit 10;

-- sqlite3 db명 < sql파일명