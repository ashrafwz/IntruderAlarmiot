CREATE USER 'amir'@'localhost' IDENTIFIED BY 'MYPASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'amir'@'localhost'
WITH GRANT OPTION;
CREATE USER 'amir'@'%' IDENTIFIED BY 'MYPASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'amir'@'%'
WITH GRANT OPTION