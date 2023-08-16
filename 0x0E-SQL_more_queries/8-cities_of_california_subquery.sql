-- This Query for lists all the cities of California in the database hbtn_0d_usa
   -- for states table  only one record where name = California
   -- for Results must be sorted order by cities.id
   -- for The database name will be passed as an argument of the mysql command

SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
