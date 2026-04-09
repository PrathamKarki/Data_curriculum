/* Aggregation (GROUP BY) */

/** Find the average price per neighbourhood **/
SELECT * 
FROM properties;

SELECT name, AVG(price) as avg_property_price
FROM properties
GROUP BY name
ORDER BY avg_property_price DESC;


/** Count total properties in each room type **/
SELECT room_type, Count(1) as "Total_properties"
FROM properties
GROUP BY room_type
ORDER BY Count(1) DESC;

/** Find maximum price in each neighbourhood **/
SELECT neighbourhood, price
FROM properties;

SELECT neighbourhood, MAX(price) as "Costly_neighbourhood"
FROM properties
GROUP BY neighbourhood;

/** Find minimum price in each room type **/
SELECT room_type, min(price) as "Lower_room_price"
FROM properties
GROUP BY room_type
ORDER BY min(price) ASC;

/** Show total number of listings per host_name **/
SELECT host_name, COUNT(*) as "Total_listings" 
FROM properties
GROUP BY host_name;