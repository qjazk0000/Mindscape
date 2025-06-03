CREATE DATABASE mindscape_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'mindscape_user'@'localhost' IDENTIFIED BY '1111';

GRANT ALL PRIVILEGES ON mindscape_db.* TO 'mindscape_user'@'localhost';

FLUSH PRIVILEGES;


REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'mindscape_user'@'localhost';
DROP USER 'mindscape_user'@'localhost';
FLUSH PRIVILEGES;