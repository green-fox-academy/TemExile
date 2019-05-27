SELECT * FROM users 
    WHERE (date_of_registration between '2018-01-01' and '2018-12-31') 
        and (email LIKE '%.com') 
        and (country = 'China');

SELECT count(distinct username) FROM users;

SELECT count(username) FROM users
    WHERE date_of_registration between '2019-01-10' and '2019-12-31';

SELECT count(username) FROM users
    WHERE EXTRACT(month from date_of_registration) = 1;

SELECT country, COUNT(username) as count  FROM users
    GROUP BY country ORDER BY count desc limit 1;

SELECT sum(case when gender = 'Male' then 1 else 0 end)::decimal/
        sum(case when gender = 'Female' then 1 else 0 end)::decimal 
    FROM users;

SELECT count(*) FROM users 
    WHERE (id is NULL) 
    or (username is NULL) 
    or (email is NULL) 
    or (date_of_registration is NULL) 
    or (first_name is NULL) 
    or (last_name is NULL) 
    or (country is NULL) 
    or (gender is NULL);

SELECT name, price FROM products ORDER BY price desc limit 3;

SELECT name, price FROM products ORDER BY price asc limit 2 offset 3;

SELECT category, avg(price) FROM products WHERE category = 'Electronics' GROUP BY category;

SELECT category, sum(price) FROM products WHERE category = 'Toys' GROUP BY category;

SELECT avg(rating) FROM reviews;

SELECT a.product_id, b.name, avg(a.rating) as rate 
    FROM reviews a left join products b on a.product_id = b.id 
    GROUP BY a.product_id, b.name 
    ORDER BY avg(a.rating) DESC limit 1;

SELECT a.product_id, b.name, avg(a.rating) as rate 
    FROM reviews a left join products b on a.product_id = b.id 
    GROUP BY a.product_id, b.name 
    ORDER BY avg(a.rating) ASC limit 1;

SELECT c.name 
    FROM (SELECT a.*, b.* 
        FROM reviews a right join products b on a.product_id = b.id) as c 
    WHERE c.rating is NULL;

SELECT count(*) FROM reviews WHERE (rating <= 3 and comment is NULL);

SELECT a.username, count(a.username) 
    FROM users a full join reviews b on a.id = b.user_id 
    GROUP BY a.username 
    ORDER BY count(a.username) DESC limit 1;

SELECT a.name, avg(b.rating) as AvgRating 
    FROM products a left join reviews b on a.id = b.product_id 
    GROUP BY a.name;

SELECT current_date - max(date) FROM reviews;