/*
DELIMITER //
CREATE PROCEDURE show_databases()
BEGIN
SHOW DATABASES;
END //
DELIMITER ;
*/
/*
DELIMITER //
CREATE PROCEDURE get_customers_where_name( IN n varchar(255))
BEGIN
SELECT * FROM customers WHERE name = n;
END //
DELIMITER ;
*/
/*
DELIMITER //
CREATE PROCEDURE insert_into_customers(IN n varchar(255), IN a varchar(255))
BEGIN
INSERT INTO customers (name, address) VALUES (n, a);
END //
DELIMITER ;
*/
/*
DELIMITER //
CREATE PROCEDURE create_database(IN n varchar(255))
BEGIN
CREATE DATABASE n;
END //
DELIMITER ;
*/
/*
DELIMITER //
CREATE PROCEDURE create_database(IN n varchar(255))
BEGIN
CREATE DATABASE n;
END //
DELIMITER ;
*/
/*
DELIMITER //
CREATE PROCEDURE multiply(IN x INT, IN y INT, OUT z INT)
BEGIN
	SET z = x * y;
END //
DELIMITER ;
*/
/*
DELIMITER //
CREATE PROCEDURE multiply2(IN x INT, INOUT y INT)
BEGIN
	SET y = x * y;
END //
DELIMITER ;
*/
/*
DELIMITER //
CREATE FUNCTION moja_funkcija()
returns varchar(30) deterministic
BEGIN
return "zdravo";
END //
DELIMITER ;
*/
/*
DROP TRIGGER IF EXISTS my_trigger;
CREATE TRIGGER my_trigger AFTER INSERT ON customers FOR EACH ROW
INSERT INTO history (name) VALUES (NOW())
*/