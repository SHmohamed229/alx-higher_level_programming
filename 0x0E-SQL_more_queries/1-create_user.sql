-- This Query for creates the MySQL server user user_0d_1.
   -- user_0d_1 This should have all privileges on your MySQL server
   -- password Has set to user_0d_1_pwd
   -- This for If the user user_0d_1 already exists, script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
