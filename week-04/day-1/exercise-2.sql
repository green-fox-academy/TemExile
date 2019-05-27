-- List the users who registered in 2018 with a .com email address and living in China
SELECT * FROM users 
    WHERE (date_of_registration between '2018-01-01' and '2018-12-31') 
        and (email LIKE '%.com') 
        and (country = 'China');

-- How many users are there?
SELECT count(distinct username) FROM users;

-- How many users registered in 2019?
SELECT count(username) FROM users
    WHERE date_of_registration between '2019-01-10' and '2019-12-31';

-- How many users registered in January?
SELECT count(username) FROM users
    WHERE EXTRACT(month from date_of_registration) = 1;

-- Which country has the most users?
SELECT country, COUNT(username) as count  FROM users
    GROUP BY country ORDER BY count desc limit 1;

-- What is the gender ratio? Male:Female
SELECT sum(case when gender = 'Male' then 1 else 0 end)::decimal/
        sum(case when gender = 'Female' then 1 else 0 end)::decimal 
    FROM users;

-- How many users left at least one field blank?
SELECT count(*) FROM users 
    WHERE (id is NULL) 
    or (username is NULL) 
    or (email is NULL) 
    or (date_of_registration is NULL) 
    or (first_name is NULL) 
    or (last_name is NULL) 
    or (country is NULL) 
    or (gender is NULL);

-- Which are the 3 most expensive products?
SELECT name, price FROM products ORDER BY price desc limit 3;

-- Which are the 4th and 5th cheapest products?
SELECT name, price FROM products ORDER BY price asc limit 2 offset 3;

-- What is the average price for an electric product?
SELECT category, avg(price) FROM products WHERE category = 'Electronics' GROUP BY category;

-- How much would it cost me to buy all the toys?
SELECT category, sum(price) FROM products WHERE category = 'Toys' GROUP BY category;

-- What is the average rating?
SELECT avg(rating) FROM reviews;

-- Which product has the best average rating?
SELECT product_id, name, rate
FROM(SELECT a.product_id, b.name, avg(a.rating) as rate 
    FROM reviews a left join products b on a.product_id = b.id 
    GROUP BY a.product_id, b.name) as table1
WHERE rate = (SELECT max(rate) FROM (SELECT a.product_id, b.name, avg(a.rating) as rate 
    FROM reviews a left join products b on a.product_id = b.id 
    GROUP BY a.product_id, b.name) as table2);

-- Which product has the worst rating?
SELECT product_id, name, rate
FROM(SELECT a.product_id, b.name, avg(a.rating) as rate 
        FROM reviews a left join products b on a.product_id = b.id 
        GROUP BY a.product_id, b.name ) as table1
WHERE rate = (SELECT min(rate) FROM (SELECT a.product_id, b.name, avg(a.rating) as rate 
        FROM reviews a left join products b on a.product_id = b.id 
        GROUP BY a.product_id, b.name)as table2);

-- Which products have no review?
SELECT c.name 
    FROM (SELECT a.*, b.* 
        FROM reviews a right join products b on a.product_id = b.id) as c 
    WHERE c.rating is NULL;

-- How many reviews are 3 or below without comment?
SELECT count(*) FROM reviews WHERE (rating <= 3 and comment is NULL);

-- Which user reviewed the most?
SELECT username, reviews
FROM(SELECT a.username, count(a.username) as reviews
        FROM users a full join reviews b on a.id = b.user_id 
        GROUP BY a.username 
        ORDER BY count(a.username)) as table1
WHERE reviews = (SELECT max(reviews) FROM (SELECT a.username, count(a.username) as reviews
        FROM users a full join reviews b on a.id = b.user_id 
        GROUP BY a.username 
        ORDER BY count(a.username)) as table2);

-- List the average rating for each product
SELECT a.name, avg(b.rating) as AvgRating 
    FROM products a left join reviews b on a.id = b.product_id 
    GROUP BY a.name;

-- How many days passed since the last review?
SELECT current_date - max(date) FROM reviews;