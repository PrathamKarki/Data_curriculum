USE metro_stay;
GO;

/* Learning about DDL CREATE DROP AND ALTER */
CREATE TABLE properties(
	id BIGINT PRIMARY KEY,
	name NVARCHAR(500) NULL,
	host_id BIGINT NULL, 
	host_name NVARCHAR(255) NULL,
	neighbourhood NVARCHAR(100) NULL,
	latitude FLOAT NULL,
	longitude FLOAT NULL,
	room_type NVARCHAR(100) NULL,
	price FLOAT NULL
	);

/* Inserting of values into the table */

INSERT INTO properties VALUES
(1, 'Cozy Apartment', 101, 'John Doe', 'Thamel', 27.7172, 85.3240, 'Entire home/apt', 45),
(2, 'Budget Room', 102, 'Alice Smith', 'Lakeside', 28.2096, 83.9856, 'Private room', 20),
(3, 'Luxury Villa', 103, 'Robert Brown', 'Thamel', 27.7160, 85.3245, 'Entire home/apt', 200),
(4, 'City Studio', 104, 'Emma Wilson', 'Baneshwor', 27.6890, 85.3420, 'Entire home/apt', 60),
(5, 'Hostel Bed', 105, 'David Lee', 'Thamel', 27.7175, 85.3230, 'Shared room', 10),
(6, 'Modern Flat', 106, 'Sophia Kim', 'Patan', 27.6720, 85.3240, 'Entire home/apt', 80),
(7, 'Quiet Room', 107, 'Michael Chen', 'Lakeside', 28.2100, 83.9860, 'Private room', 25),
(8, 'Penthouse', 108, 'Olivia Johnson', 'Baneshwor', 27.6900, 85.3430, 'Entire home/apt', 300),
(9, 'Guest House', 109, 'James Miller', 'Patan', 27.6730, 85.3250, 'Private room', 35),
(10, 'Cozy Nest', 110, 'Liam Davis', 'Thamel', 27.7180, 85.3250, 'Entire home/apt', 55),
(11, 'Backpacker Spot', 111, 'Noah Wilson', 'Lakeside', 28.2110, 83.9870, 'Shared room', 15),
(12, 'Family Home', 112, 'Ava Martinez', 'Patan', 27.6740, 85.3260, 'Entire home/apt', 90),
(13, 'Budget Stay', 113, 'Ethan Clark', 'Thamel', 27.7190, 85.3260, 'Private room', 18),
(14, 'River View Flat', 114, 'Isabella Moore', 'Baneshwor', 27.6910, 85.3440, 'Entire home/apt', 120),
(15, 'Small Room', 115, 'William Taylor', 'Lakeside', 28.2120, 83.9880, 'Private room', 22);