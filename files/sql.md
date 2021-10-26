SQL Treasure
---

# work with Databases

## show all databases
```sql
show databases;
```

## create a new databases
```sql
CREATE DATABASE <name>;
```

## delete a databases
```sql
DROP DATABASE <name>;
```

## select a database for working
```sql
USE <databases name>;
```
## show currently  selected database
```sql
SELECT database();
```

# work with tables
## create a table
```sql
CREATe TABLE tablename
(
    column_name data_type,
    column_name data_type
);
```
## show all tables
```sql
SHOW TABLES;
```
## print a table 
```sql
SHOW columns FROM <table_name>;
```
or we can use 
```sql
DESC <table_name>;
```
## deleteing tables
```sql
DROP TABLE <table_name>;
```
## insert data
```sql
INSERT INTO table_name =(column_name,column_name)
VALUES ('data','data');
```
## insert multiple data
```sql
INSERT INTO table_name =(column_name,column_name)
VALUES  ('data1','data1'),
        ('data2','data2'),
        ('data3','data3');
```
