\! echo ===================================================================
\! echo "create Regions table (Регионы)"
\! echo ===================================================================
CREATE TABLE "regions" (
  id serial PRIMARY KEY,
  name varchar
);

\! echo ===================================================================
\! echo "create Locations table (Расположения)"
\! echo ===================================================================
CREATE TABLE "locations" (
  id serial PRIMARY KEY,
  address varchar,
  region_id int
);

\! echo ===================================================================
\! echo "create Departments table (Подразделения)"
\! echo ===================================================================
CREATE TABLE "departments" (
  id serial PRIMARY KEY,
  name varchar,
  location_id int,
  manager_id int
);

\! echo ===================================================================
\! echo "create Employees table (работники, включая менеджеров)"
\! echo ===================================================================
CREATE TABLE "employees" (
  id serial PRIMARY KEY,
  name varchar,
  last_name varchar,
  hire_date date,
  salary int,
  email varchar,
  manager_id int,
  department_id int
);

\! echo ===================================================================
\! echo "insert data to Regions table"
\! echo ===================================================================
INSERT INTO regions (name) VALUES ('Eastern Europe');

\! echo ===================================================================
\! echo "insert data to Locations table"
\! echo ===================================================================
INSERT INTO locations (address, region_id) VALUES ('Turkey', 1);
INSERT INTO locations (address, region_id) VALUES ('Russia', 1);
INSERT INTO locations (address, region_id) VALUES ('Kazakhstan', 1);

\! echo ===================================================================
\! echo "insert data to Departments table"
\! echo ===================================================================
INSERT INTO employees (name, last_name, hire_date, salary, email, department_id) VALUES ('Turkey', 'Manager', date '2021-01-01', 5000, 'turkey.manager@dualbootpartners.com', 1);
INSERT INTO departments (name, location_id, manager_id) VALUES ('Turkey', 1, 1);
INSERT INTO employees (name, last_name, hire_date, salary, email, department_id) VALUES ('Russia', 'Manager', date '2021-01-01', 5000, 'russia.manager@dualbootpartners.com', 2);
INSERT INTO departments (name, location_id, manager_id) VALUES ('Russia', 2, 2);
INSERT INTO employees (name, last_name, hire_date, salary, email, department_id) VALUES ('Kazakhstan', 'Manager', date '2021-01-01', 5000, 'kazakhstan.manager@dualbootpartners.com', 3);
INSERT INTO departments (name, location_id, manager_id) VALUES ('Kazakhstan', 3, 3);

\! echo ===================================================================
\! echo "insert data to Employees table"
\! echo ===================================================================
INSERT INTO employees (name, last_name, hire_date, salary, email, manager_id, department_id) VALUES ('Turkey', 'Employee1', date(now()), 100, 'turkey.employee1@dualbootpartners.com', 1, 1);
INSERT INTO employees (name, last_name, hire_date, salary, email, manager_id, department_id) VALUES ('Turkey', 'Employee2', date('2022-01-01'), 1000, 'turkey.employee2@mail.com', 1, 1);
INSERT INTO employees (name, last_name, hire_date, salary, manager_id, department_id) VALUES ('Turkey', 'Employee3LastNameLongerThanTenSymbols', date('2023-01-01'), 3000, 1, 1);
INSERT INTO employees (name, last_name, hire_date, salary, email, manager_id, department_id) VALUES ('Russia', 'Employee1', date(now()), 100, 'russia.employee1@dualbootpartners.com', 2, 2);
INSERT INTO employees (name, last_name, hire_date, salary, email, manager_id, department_id) VALUES ('Russia', 'Employee2', date('2022-01-01'), 1000, 'russia.employee2@mail.com', 2, 2);
INSERT INTO employees (name, last_name, hire_date, salary, manager_id, department_id) VALUES ('Russia', 'Employee3', date('2023-01-01'), 3000, 2, 2);
INSERT INTO employees (name, last_name, hire_date, salary, email, manager_id, department_id) VALUES ('Kazakhstan', 'Employee1', date(now()), 100, 'kazakhstan.employee@dualbootpartners.com', 3, 3);
INSERT INTO employees (name, last_name, hire_date, salary, email, manager_id, department_id) VALUES ('Kazakhstan', 'Employee2', date('2022-01-01'), 1000, 'kazakhstan.employee@mail.com', 3, 3);
INSERT INTO employees (name, last_name, hire_date, salary, manager_id, department_id) VALUES ('Kazakhstan', 'Employee3', date('2023-01-01'), 3000, 3, 3);







