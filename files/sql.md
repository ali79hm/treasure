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
## insert data intp table
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

## prevent null columns
for example we have students table and every student must have a name so name fields cant be empty , what should we do?
the answer is NOT NULL.
we can set a column to NOT NULL to prevent this problems
```sql
CREATe TABLE tablename
(
    column_name1 data_type NOT NULL,
    column_name2 data_type
);
```
in above code **column_name1** cant be NULL

## set default value for columns
if user doesnt set a value for a column it will set to NULL
one way to prevent that is setting a default value 
```sql
CREATe TABLE tablename
(
    column_name1 data_type DEFAULT default_value,
    column_name2 data_type
);
```
in above code if user doesnt set **column_name1** it will set to **default_value**


# warnings
## see warnings
```sql
SHOW WARNINGS;
```
