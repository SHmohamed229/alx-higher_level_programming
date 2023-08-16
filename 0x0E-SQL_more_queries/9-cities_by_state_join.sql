-- this query for lists all cities contained in the database hbtn_0d_usa
   -- Each record should display: for cities.id - cities.name - states.name
   -- for Results must be have a sorted in ascending order by cities.id
   -- This  database name will be passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
