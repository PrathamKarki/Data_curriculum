/* Display  all the columns from properties table */
USE metro_stay;
SELECT *
FROM properties;

/* Show only name, host_name and price */
SELECT name, host_name, price
FROM properties;

/* Find all the properteis where price is greater than 100 */
SELECT *
FROM properties
WHERE price > 100;

/* List all the properties located in "Thamel" */
SELECT id, host_name, name, neighbourhood
FROM properties
WHERE neighbourhood LIKE 'Tha%l';

/* Show all "Private room" listings */
SELECT id, host_name, name, room_type
FROM properties
WHERE room_type = 'Private room';

/* Find Properties where price is between 20 and 80 */
SELECT id, host_name, name, price
FROM properties
WHERE price BETWEEN 20 AND 80;

/* Display properties where host_name is not NULL */
SELECT name, host_name
FROM properties
WHERE host_name IS NOT NULL;

