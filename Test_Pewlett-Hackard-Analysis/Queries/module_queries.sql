-- Creating tables for PH-EmployeeDB

-- creating tables departments
CREATE TABLE departments (
     dept_no VARCHAR(4) NOT NULL,
     dept_name VARCHAR(40) NOT NULL,
     PRIMARY KEY (dept_no),
     UNIQUE (dept_name)
);

-- creating tables employees
CREATE TABLE employees (
	emp_no INT NOT NULL,
	birth_date DATE NOT NULL,
	first_name VARCHAR NOT NULL,
	last_name VARCHAR NOT NULL,
	gender VARCHAR NOT NULL,
	hire_date DATE NOT NULL,
	PRIMARY KEY (emp_no)
);

-- creating tables dept_manager
CREATE TABLE dept_manager (
	dept_no VARCHAR(4) NOT NULL,
    emp_no INT NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
	PRIMARY KEY (emp_no, dept_no),
	FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
	FOREIGN KEY (dept_no) REFERENCES departments (dept_no)    
);

-- creating tables salaries
CREATE TABLE salaries (
  	emp_no INT NOT NULL,
  	salary INT NOT NULL,
  	from_date DATE NOT NULL,
  	to_date DATE NOT NULL,
	PRIMARY KEY (emp_no),
  	FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
);

-- creating dept_employee
CREATE TABLE dept_employee (
	emp_no INT NOT NULL,
	dept_no VARCHAR NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL,
	PRIMARY KEY (emp_no, dept_no),
	FOREIGN KEY (dept_no) REFERENCES departments (dept_no)
);

-- creating titles
CREATE TABLE titles (
	emp_no INT NOT NULL,
	title VARCHAR NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL,
	PRIMARY KEY (emp_no, title, from_date),
	FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
);

--------------------------------------------------
select *
from departments;

select *
from employees;

select *
from dept_employee;

select *
from dept_manager;

select *
from salaries;

select *
from dept_manager;

--------------------------------------------------
-- query to retreive the first_name and last_name from the employees table where DOB is between 1952/1/1 and 1955/12/31
select first_name, last_name
from employees
where birth_date between '1952-01-01' and '1955-12-31';

-- query to retrieve first_name and last_name from employees table where DOB is in the year 1952
SELECT first_name, last_name
FROM employees
WHERE birth_date BETWEEN '1952-01-01' AND '1952-12-31';

-- query to retrieve first_name and last_name from employees table where DOB is in the year 1953
SELECT first_name, last_name
FROM employees
WHERE birth_date BETWEEN '1953-01-01' AND '1953-12-31';

-- query to retrieve first_name and last_name from employees table where DOB is in the year 1954
SELECT first_name, last_name
FROM employees
WHERE birth_date BETWEEN '1954-01-01' AND '1954-12-31';

-- query to retrieve first_name and last_name from employees table where DOB is in the year 1955
SELECT first_name, last_name
FROM employees
WHERE birth_date BETWEEN '1955-01-01' AND '1955-12-31';

-- Retirement eligibility
select first_name, last_name
into retirement_info
from employees
where (birth_date between '1952-01-01' and '1955-12-31')
AND (hire_date between '1985-01-01' and '1988-12-31');

select first_name, last_name, title
from employees
left join titles on employees.emp_no = titles.emp_no;

-- creating retirement info with f/name, l/name and emp_no
select first_name, last_name, emp_no
into retirement_info
from employees
where (birth_date between '1952-01-01' and '1955-12-31')
and (hire_date between '1985-01-01'and '1988-12-31')

-- check the table 
select * from retirement_info;

---------------------------------------------------
-- inner join example
select departments.dept_name, 
	dept_manager.emp_no, 
	dept_manager.from_date, 
	dept_manager.to_date
from departments
inner join dept_manager 
on departments.dept_no = dept_manager.dept_no;

-- USING ALIASES - above inner join example
select de.dept_name, 
	dm.emp_no, 
	dm.from_date, 
	dm.to_date
from departments as de
inner join dept_manager as dm
on de.dept_no = dm.dept_no;

---------------------------------------------------
-- joining retirement_info and dept_emp tables
select retirement_info.emp_no,
	retirement_info.first_name, 
	retirement_info.last_name, 
	dept_employee.to_date	
from retirement_info
left join dept_employee 
on retirement_info.emp_no = dept_employee.emp_no;

-- USING ALIASES - above joining retirement_info and dept_emp tables ()
select ri.emp_no,
	ri.first_name, 
	ri.last_name, 
	de.to_date	
from retirement_info as ri
left join dept_employee as de
on ri.emp_no = de.emp_no;

-- creating a new table - exisitng employees to retire 
select ri.emp_no,
	ri.first_name, 
	ri.last_name, 
	de.to_date
into current_emp	
from retirement_info as ri
left join dept_employee as de
on ri.emp_no = de.emp_no
WHERE de.to_date = '9999-01-01';

select * from current_emp;

--- joining the current_emp and department number
select count(ce.emp_no), de.dept_no
into number_of_employees_retiring_per_department
from current_emp as ce
left join dept_employee as de
on ce.emp_no = de.emp_no
group by de.dept_no
order by de.dept_no;

select * from number_of_employees_retiring_per_department;

---------------------------------------------------
SELECT emp_no, 
	first_name, 
	last_name, 
	gender
INTO emp_info
FROM employees
WHERE (birth_date BETWEEN '1952-01-01' AND '1955-12-31')
AND (hire_date BETWEEN '1985-01-01' AND '1988-12-31');

SELECT * FROM emp_info;

DROP TABLE emp_info:

------- Employee Information: A list of employees containing their unique 
------- employee number, their last name, first name, gender, and salary
SELECT e.emp_no, 
	e.first_name, 
	e.last_name, 
	e.gender,
	s.salary,
	de.to_date
INTO emp_info
FROM employees as e
INNER JOIN salaries as s
ON e.emp_no = s.emp_no
INNER JOIN dept_employee as de
ON e.emp_no = de.emp_no
WHERE (e.birth_date BETWEEN '1952-01-01' AND '1955-12-31')
AND (e.hire_date BETWEEN '1985-01-01' AND '1988-12-31')
AND (de.to_date = '9999-01-01');
---view the table
SELECT * FROM emp_info;


-- List of managers per department
SELECT  dm.dept_no,
        d.dept_name,
        dm.emp_no,
        ce.last_name,
        ce.first_name,
        dm.from_date,
        dm.to_date
INTO manager_info
FROM dept_manager AS dm
    INNER JOIN departments AS d
        ON (dm.dept_no = d.dept_no)
    INNER JOIN current_emp AS ce
        ON (dm.emp_no = ce.emp_no);
---view the table
SELECT * FROM manager_info;

----- list of retirees per department
SELECT ce.emp_no,
	ce.first_name,
	ce.last_name,
	d.dept_name
INTO dept_info
FROM current_emp as ce
INNER JOIN dept_employee AS de
ON (ce.emp_no = de.emp_no)
INNER JOIN departments AS d
ON (de.dept_no = d.dept_no);
---view the table
SELECT * from dept_info; 


---- tailored list for ONLY the sales team
SELECT emp_no, first_name, last_name, dept_name
FROM dept_info
WHERE (dept_info.dept_name = 'Sales');

---- tailored list for the sales and dev team
SELECT emp_no, first_name, last_name, dept_name
FROM dept_info
WHERE (dept_info.dept_name = 'Sales')
OR (dept_info.dept_name = 'Development');




































