SQL Treasure
---
# introduction 
first of all what is data base:
a structured set of data with accessible inteface 

second thing we should know is diffrent between data base and data base management systems usally people call both of them as data base
data base is your tables but DBMS(data base management systems) is a system that do thing such as adding tables ,removing them and etc
so sql is database language but mySQL is DBSM.
we have several DBSMs that use sql as language, like postgre SQL,mySQL,oracle,SQlite .
their diffrence is in speed , security , size , user premitions and ...

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

- before making tables you sould be familier with sql data types if you are not! , [click here](https://www.w3schools.com/sql/sql_datatypes.asp)
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
