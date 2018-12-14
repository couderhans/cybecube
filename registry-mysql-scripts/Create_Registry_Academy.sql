CREATE TABLE `registry`.`academy` (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(10),
	courses INT,
		FOREIGN KEY (id)
        REFERENCES course(id)
)
COMMENT = 'Courses followed in the Academy';
