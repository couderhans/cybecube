CREATE TABLE `registry`.`course` (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    initDate VARCHAR(10),
    title VARCHAR(10),
	course_status VARCHAR(30),
    subscriptions INT,
		FOREIGN KEY (id)
        REFERENCES assistant(id),
	complete BOOLEAN
)
COMMENT = 'Courses followed in the Academy';