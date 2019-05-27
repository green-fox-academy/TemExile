-- create a table
create table employees(first_name VARCHAR(50), last_name VARCHAR(50), 
                        username VARCHAR(50), date_of_employment date, 
                        date_of_exit date, Role VARCHAR(50), Salary INT);

-- Inserted a row to table
INSERT into employees(first_name, last_name, username, 
                        date_of_employment, date_of_exit, Role, Salary) 
        values ('haoxiang','weng','haoxiangweng','2019-05-06', NULL, 'junior',111);

-- Added a column to table 
ALTER TABLE employees ADD department VARCHAR(50);

-- removed a column from table
ALTER TABLE employees DROP username;

-- renamed a column in the table
ALTER TABLE employees RENAME Role TO Level;