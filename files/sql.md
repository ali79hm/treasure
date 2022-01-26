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
## select a database for working
```sql
USE <databases name>;
```
## show currently  selected database
```sql
SELECT database();
```
## delete a databases
```sql
DROP DATABASE <name>;
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
## Deleteing tables
```sql
DROP TABLE <table_name>;
```
## Prevent null columns
for example we have students table and every student must have a name so name fields cant be empty , what should we do?
the answer is NOT NULL.
we can set a column to NOT NULL to prevent this problems
### while creating table:
```sql
CREATE TABLE tablename
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
## Set default value for columns

### while creating table:

if user doesnt set a value for a column it will set to NULL
one way to prevent that is setting a default value 
```sql
CREATE TABLE tablename
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
## Primary key

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
 ### after creating table:
```sql
ALTER TABLE table_name MODIFY column_name data_type PRIMARY KEY NOT NULL AUTO_INCREMENT;
```
## cloning a table
Step 1: Creating an Empty Table
First use the following statement to create an empty table based on the definition of original table. It also includes the column attributes and indexes defined in the original table:
```sql
CREATE TABLE new_table LIKE original_table;
```

Step 2: Inserting Data into Table
Now, use the following statement to populate the empty table with data from original table:
```sql
INSERT INTO new_table SELECT * FROM original_table;
```


--------------------------------------------------

# work with data in tables
## Insert data
### Insert data into table
```sql
INSERT INTO table_name =(column_name,column_name)
VALUES ('data','data');
```
### Insert multiple data
```sql
INSERT INTO table_name =(column_name,column_name)
VALUES  ('data1','data1'),
        ('data2','data2'),
        ('data3','data3');
```
## Read tables

### Read all columns:
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
we want to get name of people who`s age is grather than 18 :```SELECT name FROM people WHERE age>18 ```

#### select list of special rows
say that you want to select people with age 20 and 18 you can do this :
```sql
SELECT column_name1 FROM table_name WHERE age IN (2,4);
```
#### select range of special rows
say that you want to select people with age 20 and 18 you can do this :
```sql
SELECT column_name1 FROM table_name WHERE age BETWEEN 2 AND 4;
```

### using aliases
we cant show a column with special title
```sql
SELECT column_name AS special_name FROM table_name;
```
## Update
```sql
UPDATE table_name SET <list_of_changes> WHERE <condition>;
```
## delete
```sql
DELETE FROM table_name WHERE <condition>;
```
becuse ther isn`t any undo button you can select data before updating or deleting to make sure that you are targeting what you mean to target
### clear all table data
```sql
DELETE FROM table_name;
```
## how to undo table changes
as i mensioned before there is no way to undo changes that commited 
but we can do 2 thing when we work with sensetinve data then if we messed up we can undo changes
### first method
you can set autocommit off with this command:
```sql
SET SESSION autocommit = 0;
```
Now you may enter a series of SQL statements that collectively will make up the transaction. At any point, you may undo all of the statements for the transaction by entering the following SQL statements:
```sql
ROLLBACK;
```
If you don’t want to reverse a transaction and decide to commit the SQL statements executed, enter the following SQL statement:
```sql
COMMIT;
```
This ends the transaction. Note that some statements are not transactional and may not be rolled back, such as data definition statements CREATE TABLE, CREATE DATABASE, ALTER TABLE, DROP TABLE, and DROP DATABASE, for example. Some of these statements, in fact, implicitly commit the current transaction.

auto commit will turn again after you end session but also you can turn back on autocommit by this command:
```sql
SET SESSION autocommit = 1;
```
### second method
you can use this command before your sql statments:
```sql
START TRANSACTION;
```
Now you may enter a series of SQL statements that collectively will make up the transaction. At any point, you may undo all of the statements for the transaction by entering the following SQL statements:
```sql
ROLLBACK;
```
If you don’t want to reverse a transaction and decide to commit the SQL statements executed, enter the following SQL statement:
```sql
COMMIT;
```
This ends the transaction and for new transaction you sould do this methed again . Note that some statements are not transactional and may not be rolled back, such as data definition statements CREATE TABLE, CREATE DATABASE, ALTER TABLE, DROP TABLE, and DROP DATABASE, for example. Some of these statements, in fact, implicitly commit the current 

--------------------------------------------------

# string functions
[string functions DOCUMENTATION](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)

first of all you should know how to use string functions:
```sql
SELECT <string_function> FROM table_name;
```
 now we move on functions

 ## concat
 ```sql
 SELECT CONCAT(string1,string2) FROM table_name;
```
there is way to concat with separator
```sql
 SELECT CONCAT_WS(separator,string1,string2) FROM table_name;
```
## substring
```sql
 SELECT SUBSTRING(string,start_index,lenght) FROM table_name;
```
there is other way
```sql
 SELECT SUBSTRING(string,start_index) FROM table_name;
```
we can use minus indexes as well (with minus index count will start from end)

we can use ```substr()``` instead of ```SUBSTRING()```.

##replace
```sql
 SELECT REPLACE(string,replace_part,alternative) FROM table_name;
```

## reverse
```sql
 SELECT REVERSE(string) FROM table_name;
```

## upper and lower case
```sql
SELECT UPPER(string) FROM table_name;
SELECT LOWER(string) FROM table_name;
```

## string lenght
```sql
SELECT CHAR_LENGTH(string) FROM table_name;
```


--------------------------------------------------


# part 8 to 10 is here
blah blah blah

# part 11 to 13 is here
again blah blah blah

# run sql file
```sql
SOURCE file.sql;
```


--------------------------------------------------

# warnings
## see warning
```sql
SHOW WARNINGS;
```
