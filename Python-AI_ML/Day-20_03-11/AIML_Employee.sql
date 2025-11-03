
insert into employeedb
values (11234, 'Saurabh', 'Vaishali')

insert into employeedb
values (11235, 'Abhishek', 'Panna')

select * from employeedb

update employeedb
set city= 'Bangalore'
where name='Abhishek'

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

select * from AIML_employee


alter table AIML_employee
add constraint ap primary key (emp_id)

alter table AIML_employee
alter column Name set not null

alter table AIML_employee
add constraint au unique(Name)

alter table AIML_employee
alter column city set default 'Not known'

alter table AIML_employee
add constraint age_check check (Age > 0)

alter table AIML_employee
add column dummy int

alter table AIML_employee
drop column dummy

alter table AIML_employee
drop constraint au

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

-- UNION and UNION ALL
select emp_id from AIML_employee
union all
select id from emp_designation
















