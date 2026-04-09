/* HAVING IN SQL */

/** Show neighbourhood where average price is greater than 80 **/
SELECT neighbourhood, AVG(price) as "Average_price"
from properties
GROUP BY neighbourhood
HAVING AVG(price) > 80;

/** Show room types that have more than 5 listings **/
SELECT room_type, COUNT(*) as total_listings
FROM properties
GROUP BY room_type
HAVING COUNT(*) > 5;