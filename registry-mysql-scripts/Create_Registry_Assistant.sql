CREATE TABLE `registry`.`assistant` (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    assistant_name VARCHAR(30),
    title VARCHAR(10),
	state INT,
		FOREIGN KEY (state)
        REFERENCES state(id)
        ON DELETE CASCADE,
    location INT,
		FOREIGN KEY (location)
        REFERENCES location(id)
        ON DELETE CASCADE,
    date_of_birth VARCHAR(12),
    gender VARCHAR(1),
    class VARCHAR(7),
	alive BOOLEAN
)
COMMENT = 'Virtual assistant identity card';