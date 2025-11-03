-- Questions - 
------------------------------------------------------------------------------------------
-- 1. Write SELECT statements with filtering (WHERE)
-- 2. Use ORDER BY and LIMIT clauses
-- 3. Insert, update, and delete data
-- 4. Use DISTINCT and aggregate functions (COUNT, SUM, AVG)
-- 5. Basic string and date/time functions
 
 
-- 1. Create tables with appropriate data types
-- 2. Use constraints: NOT NULL, UNIQUE, PRIMARY KEY
-- 3. Define default values and check constraints
-- 4. Understand and use SERIAL and UUID types
-- 5. Alter tables to add/drop columns and constraints
 
 
-- 1. Implement INNER JOIN, LEFT JOIN, RIGHT JOIN
-- 2. Write simple correlated and non-correlated subqueries
-- 3. Use EXISTS and IN predicates
-- 4. UNION and UNION ALL 
----------------------------------------------------------------------------------------------------

-- Answer-

-- 1. Write SELECT statements with filtering (WHERE)
-- Get employees from Surat
SELECT * FROM employeedb
WHERE city = 'Surat';

-- 2. Use ORDER BY and LIMIT clauses
SELECT * FROM employeedb
ORDER BY id DESC
LIMIT 2;

-- 3. Insert, update, and delete data
-- Insert a new employee
INSERT INTO employeedb (id, name, city)
VALUES (12345, 'Ravi', 'Pune');

-- Update an employee’s city
UPDATE employeedb
SET city = 'Mumbai'
WHERE name = 'Uday';

-- Delete an employee by ID
DELETE FROM employeedb
WHERE id = 11234;

-- 4. Use DISTINCT and aggregate functions (COUNT, SUM, AVG)
-- Get unique city names
SELECT DISTINCT city FROM employeedb;

-- Count number of employees
SELECT COUNT(*) AS total_employees FROM employeedb;


-- 5. Basic string and date/time functions
-- Convert name to uppercase
SELECT UPPER(name) AS upper_name FROM employeedb;

-- Show current date and time
SELECT NOW();

----------------------------------------------------------------------------------------------
-- 1. Create tables with appropriate data types
create table AIML_employee (emp_id varchar(8), Name varchar(20), city varchar(20))

alter table AIML_employee
add column Age int

insert into AIML_employee
values ('ESET0144', 'Uday', 'Surat', 26)

insert into AIML_employee
values ('ESET0135', 'Shubham', 'Pune', 24),
('ESET0123', 'Milan', 'Jaipur', 22),
('ESET0112', 'Gaurav', 'Mumbai', 25),
('ESET0096', 'Saurabh', 'Vaishali', 25),
('ESET0176', 'Abhishek', 'Panna', 23)

insert into AIML_employee
values ('ESET0034', 'Reet', 'Bihar', 22),
('ESET0035', 'Gopalbhai', 'Bihar', 25),
('ESET0036', 'Gauravi', 'Mumbai', 28),
('ESET0037', 'Saurabhi', 'Vaishali', 25),
('ESET045', 'Abhisheki', 'Panna', 23)

-- 2. Use constraints: NOT NULL, UNIQUE, PRIMARY KEY
alter table AIML_employee
add constraint ap primary key (emp_id)

alter table AIML_employee
alter column Name set not null

alter table AIML_employee
add constraint au unique(Name)


-- 3. Define default values and check constraints
alter table AIML_employee
alter column city set default 'Not known'

alter table AIML_employee
add constraint age_check check (Age > 0)

-- 4. Understand and use SERIAL and UUID types
-- Serial
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT
);

-- UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";  -- enable UUID generation
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    email TEXT
);
-- 5. Alter tables to add/drop columns and constraints

alter table AIML_employee
add column dummy int

alter table AIML_employee
drop column dummy

alter table AIML_employee
drop constraint au

------------------------------------------------------------------------------------------------------
-- 1. Implement INNER JOIN, LEFT JOIN, RIGHT JOIN

create table emp_desgination (id varchar(10), designation varchar(20))

alter table emp_desgination
rename to emp_designation

insert into emp_designation values
('ESET0108', 'AIML Engineer'),
('ESET0112', 'Software'),
('ESET0096', 'Backend'),
('ESET0001', 'Frontend')

select * from emp_designation

select a.emp_id, a.Name, b.designation from AIML_employee as a
inner join emp_designation as b on a.emp_id = b.id

select a.emp_id, a.Name, b.designation from AIML_employee as a
left join emp_designation as b on a.emp_id = b.id

select a.emp_id, a.Name, b.designation from AIML_employee as a
right join emp_designation as b on a.emp_id = b.id

-- 2. Write simple correlated and non-correlated subqueries


-- Non correlated query
SELECT name, Age
FROM AIML_employee
WHERE Age >= (
    SELECT AVG(Age)
    FROM AIML_employee
);

-- Correlated query
SELECT e.name, e.Age, e.city
FROM AIML_employee as e
WHERE e.Age >= (
    SELECT AVG(e2.Age)
    FROM AIML_employee e2
	where e2.city = e.city
)
order by e.city;

-- 3. Use EXISTS and IN predicates
-- use exists and in predicates
-- IN
SELECT name
FROM AIML_employee
WHERE emp_id IN (
    SELECT id
    FROM emp_designation
    WHERE id = 'ESET0108'
);

-- EXISTS - Find employees who belong to at least one designation is 'AIML Engineer'
SELECT e.name, e.city
FROM AIML_employee e
WHERE exists (
    SELECT 1
    FROM emp_designation d
    WHERE d.id = e.emp_id
	and d.designation = 'AIML Engineer'
);

-- 4. UNION and UNION ALL 

select emp_id from AIML_employee
union all
select id from emp_designation