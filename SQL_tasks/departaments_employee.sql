-- task #1
SELECT * 
FROM employee 
WHERE salary > 50000;

-- task #2
SELECT department_id
FROM employee
GROUP BY department_id
HAVING COUNT (*) = 0;

-- task #3
SELECT 
    head.name as head,
    department.name as department,
    GROUP_CONCAT(employee.name) as employess
FROM
    employee  
INNER JOIN
    employee AS head ON employee.chief_id = head.id
INNER JOIN
    department ON department.id = employee.department_id 
GROUP BY head.name,department.name;

-- task #4 
SELECT department_id,
CASE
    WHEN department_id IN (SELECT department_id FROM employee GROUP BY department_id HAVING COUNT (*) > 0) THEN AVG (salary)
    ELSE 0
END AS avg_salary
FROM employee
GROUP BY department_id;


-- task #5
SELECT department_id, AVG (salary) AS avg_salary
FROM employee
WHERE avg_salary > 50000
GROUP BY department_id;

-- task #6
SELECT dep.name, ch.name 
FROM employee AS emp, Employee AS ch, department AS dep
WHERE ch.id = emp.chief_id AND ch.salary > (SELECT MAX(salary) 
											FROM Employee AS max 
											WHERE max.department_id = ch.department_id)
AND dep.ID = ch.department_id;

-- task #7
SELECT * 
FROM Employee AS emp
LEFT JOIN Employee AS ch ON (emp.chief_id = ch.Id AND emp.department_id = ch.department_id)
WHERE ch.id IS NULL;