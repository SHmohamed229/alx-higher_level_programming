-- this query for creates the database hbtn_0d_usa and the table states on your MySQL server.
   -- states (descriptio)n:
      -- for id INT unique - auto generated, cant be null, is a primary key
      -- for name VARCHAR(256) - can't be null
   -- this for If the table hbtn_0d_usa already exists, script should not fail
   -- this for If the table states already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
