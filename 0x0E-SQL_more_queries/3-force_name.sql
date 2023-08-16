-- This Query for creates the table force_name on your MySQL server.
   -- This for force_name description:
      -- for id INT
      -- for name VARCHAR(256) can’t be null
   -- This for  database name will be passed as an argument of the mysql command
   -- for If the table force_name already exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
