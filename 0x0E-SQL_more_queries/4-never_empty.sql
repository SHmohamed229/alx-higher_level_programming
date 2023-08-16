-- This Query for creates the table id_not_null on your MySQL server.
   -- id_not_null description:
      -- id INT - for default value 1
      -- for name VARCHAR(256)
   -- this for  database name will be passed as an argument of the mysql command
   -- this If the table id_not_null already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
