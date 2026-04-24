/* SORTING (ORDER BY) IN SQL */

/* Show all properties ordered by price (highest to lowest) */
SELECT *
from properties
ORDER BY price DESC;

/* Show the 5 chepest properties */
SELECT TOP 5 host_name, name, price
from properties
ORDER BY price ASC;

/* Show properties sorted by neighbourhood alphabetically */
SELECT host_name, name, price, neighbourhood
from properties
ORDER by neighbourhood asc;