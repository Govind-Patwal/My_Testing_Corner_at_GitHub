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