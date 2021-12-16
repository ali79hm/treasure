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

# manage Databases

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

--------------------------------------------------

# manage tables

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
## prevent null columns
for example we have students table and every student must have a name so name fields cant be empty , what should we do?
the answer is NOT NULL.
we can set a column to NOT NULL to prevent this problems
### while creating table:
```sql
CREATe TABLE tablename
(
    column_name1 data_type NOT NULL,
    column_name2 data_type
);
```
in above code **column_name1** cant be NULL
 ### after creating tabel:
```sql
ALTER TABLE table_name MODIFY column_name data_type NOT NULL;
```
## set default value for columns

### while creating table:

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

 ### after creating tabel:
```sql
ALTER TABLE table_name ALTER column_name SET DEFAULT default_value;
```
## primary key

we need unique id to destiguish between datas.
in sql we can set a column to primary key and it will be unique for every row 
### while creating table:
```sql
CREATE TABLE tablename
(
    column_name1 data_type NOT NULL,
    column_name2 data_type,
    PRIMARY KEY (column_name1)
);
```
it is hard to set primary key manually so we cant make it automatic by using ```AUTO_INCREMENT```
```sql
CREATE TABLE tablename
(
    column_name1 data_type NOT NULL AUTO_INCREMENT,
    column_name2 data_type,
    PRIMARY KEY (column_name1)
);
```
 ### after creating tabel:
```sql
ALTER TABLE table_name MODIFY column_name data_type PRIMARY KEY NOT NULL AUTO_INCREMENT;
```

--------------------------------------------------


# work with data in tables

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





## read tables

### read all columns:
```sql
SELECT * FROM table_name
```
### read a column
```sql
SELECT column_name FROM table_name
```

### read multiple columns
```sql
SELECT column_name1,column_name2 FROM table_name
```

### use condition for selecting special rows
```sql
SELECT column_name1 FROM table_name WHERE condidion
```
here a example from conditions:
suppose we have two columns: 1.name 2.age
we want to get name of people who`s age is grather than 18 :
```SELECT name FROM people WHERE age>18 ```

### using aliases
we cant show a column with special title
```sql
SELECT column_name AS special_name FROM table_name
```



# warnings
## see warnings
```sql
SHOW WARNINGS;
```
