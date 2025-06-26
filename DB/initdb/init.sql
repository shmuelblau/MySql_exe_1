USE eagleEyeDB;

CREATE TABLE IF NOT EXISTS agents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codeName VARCHAR(255),
    realName VARCHAR(255),
    location VARCHAR(255),
    status VARCHAR(50),
    missionsCompleted INT
);

INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES
('ShadowFox', 'David Cohen', 'Tel Aviv', 'Active', 12),
('IronWolf', 'Lior Levi', 'Jerusalem', 'Inactive', 8),
('BlackHawk', 'Yael Mizrahi', 'Haifa', 'Active', 15),
('Ghost', 'Avi Peretz', 'Eilat', 'Missing', 3),
('NightOwl', 'Dana Azulai', 'Beersheba', 'Active', 22),
('Viper', 'Nadav Segal', 'Netanya', 'Retired', 30),
('Falcon', 'Noa Shalom', 'Ashdod', 'Active', 18),
('Scorpion', 'Eli Harari', 'Nazareth', 'Captured', 6),
('WolfEye', 'Rina Bar-On', 'Hadera', 'Active', 11),
('Storm', 'Moshe Azulai', 'Tiberias', 'On Leave', 9);