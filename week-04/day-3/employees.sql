-- Most common first name
SELECT first_name, count(first_name)as time 
FROM employee_day_3 
GROUP BY first_name 
HAVING count(first_name) >= (SELECT count(first_name) as time 
                                FROM employee_day_3 
                                GROUP BY first_name 
                                ORDER BY time DESC limit 1);

-- Most common first name among the young(<30)
SELECT first_name, count(first_name)as time 
FROM employee_day_3
WHERE age < 30
GROUP BY first_name 
HAVING count(first_name) >= (SELECT count(first_name) as time 
                                FROM employee_day_3 
                                WHERE age < 30
                                GROUP BY first_name 
                                ORDER BY time DESC limit 1);

-- Median salary
SELECT avg(salary) as median_salary 
FROM (SELECT salary 
        FROM employee_day_3
        ORDER BY salary ASC limit 2 offset 149) as table1;

-- earn more than salary
SELECT count(first_name)
FROM employee_day_3
WHERE salary > (SELECT avg(salary) FROM employee_day_3);

-- increase salary
UPDATE employee_day_3
SET salary = salary + 1200
WHERE salary < (SELECT avg(salary) as median_salary 
FROM (SELECT salary 
        FROM employee_day_3
        ORDER BY salary ASC limit 2 offset 149) as table1);