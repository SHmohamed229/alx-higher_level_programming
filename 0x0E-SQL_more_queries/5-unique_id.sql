-- this query for creates the table unique_id on your MySQL server.
   -- unique_id (description):
      -- for id INT - default value 1, must be unique
      -- for name VARCHAR(256)
   -- This  database name will be passed as an argument of the mysql command
   -- this If the table unique_id already exists, script should not fail

CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
