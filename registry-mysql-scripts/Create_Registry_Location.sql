CREATE TABLE `registry`.`location` (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(30),
    va_host VARCHAR(30),
    va_node VARCHAR(30),
    va_ports VARCHAR(50),
    cloud_address VARCHAR(10)
)
COMMENT = 'Location where the assistant can be found; academy, work or home';