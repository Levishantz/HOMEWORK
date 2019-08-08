--question 1

SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary FROM employees 
LEFT JOIN salaries ON employees.Emp_no = salaries.Emp_no

-- question 2

SELECT employees.hire_date FROM employees
WHERE hire_date LIKE '%1986%'


-- question 3

SELECT 
dept_manager.emp_no,
departments.dept_name,
employees.first_name,
employees.last_name,
dept_manager.from_date,
dept_manager.to_date
FROM 
employees
INNER JOIN dept_manager ON dept_manager.emp_no = employees.emp_no
INNER JOIN departments ON dept_manager.dept_no = departments.dept_no;

-- question 4

SELECT 
dept_emp.dept_no,
dept_emp.emp_no,
departments.dept_name,
employees.first_name,
employees.last_name
FROM 
dept_emp
INNER JOIN employees ON employees.emp_no = dept_emp.emp_no

INNER JOIN departments ON dept_emp.dept_no = departments.dept_no;


-- question 5
SELECT * FROM employees
WHERE first_name = 'Hercules' and last_name LIKE '%B%'

-- question 6 
-- sales dept = d007

SELECT * FROM departments

SELECT 
dept_emp.dept_no,
dept_emp.emp_no,
departments.dept_name,
employees.first_name,
employees.last_name
FROM 
dept_emp
INNER JOIN employees ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE dept_emp.dept_no = 'd007'

-- question 7
-- development = d005

SELECT 
dept_emp.dept_no,
dept_emp.emp_no,
departments.dept_name,
employees.first_name,
employees.last_name
FROM 
dept_emp
INNER JOIN employees ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE dept_emp.dept_no = 'd007' OR dept_emp.dept_no = 'd005'

-- question 8

SELECT last_name, COUNT(last_name) AS Num FROM employees
GROUP BY last_name
ORDER BY num DESC
