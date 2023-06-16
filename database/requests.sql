\! echo ===================================================================
\! echo "Показать работников у которых нет почты или почта не в корпоративном домене"
\! echo "(домен dualbootpartners.com)"
\! echo ===================================================================

SELECT * FROM employees
WHERE email NOT LIKE '%@dualbootpartners.com'
OR email IS NULL;

\! echo ===================================================================
\! echo "Получить список работников нанятых в последние 30 дней"
\! echo ===================================================================

SELECT * FROM employees
WHERE hire_date >= now() - interval '30 day';

\! echo ===================================================================
\! echo "Найти максимальную и минимальную зарплату по каждому департаменту"
\! echo "авторский комментарий: первый вариант человекочитаемый, второй без лишних джойнов"
\! echo ===================================================================

SELECT d.name, MAX(salary), MIN(salary) 
FROM employees
JOIN departments d ON d.id = employees.department_id
GROUP BY d.name;

SELECT department_id, MAX(salary), MIN(salary) 
FROM employees
GROUP BY department_id;


\! echo ===================================================================
\! echo "Посчитать количество работников в каждом регионе"
\! echo "авторский комментарий: первый вариант человекочитаемый, второй без лишних джойнов"
\! echo ===================================================================

SELECT region.name, COUNT(region_id)
FROM employees
JOIN departments department ON department.id = employees.department_id
JOIN locations location ON location.id = department.location_id
JOIN regions region ON region.id = location.region_id
GROUP BY region.name;

SELECT region_id, COUNT(region_id)
FROM employees
JOIN departments department ON department.id = employees.department_id
JOIN locations location ON location.id = department.location_id
GROUP BY region_id;

\! echo ===================================================================
\! echo "Показать сотрудников у которых фамилия длиннее 10 символов"
\! echo ===================================================================

SELECT * FROM employees
WHERE char_length(last_name) > 10;

\! echo ===================================================================
\! echo "Показать сотрудников с зарплатой выше средней по всей компании"
\! echo ===================================================================

SELECT * FROM employees
WHERE salary > (
  SELECT AVG(salary)
  FROM employees
);









