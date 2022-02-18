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
# refining selection

## distinct
it will give us unique items when we have duplicates

```sql
SELECT DISTINCT column_name FROM table_name
```
you can use distinct on multiple columns at same time 

```sql
SELECT DISTINCT column_name1,column_name2 FROM table_name
-- OR
SELECT DISTINCT CANCAT(column_name1,column_name2) FROM table_name
```

## order by 
### order ascending
```sql 
SELECT column_name FROM table_name ORDER BY column_name
-- OR
SELECT column_name FROM table_name ORDER BY column_name ASC

```
### order descending
```sql 
SELECT column_name FROM table_name ORDER BY column_name DESC

```
- you can order by nth column you call with select for example :
```SELECT column_name1,column_name2 FROM table_name ORDER BY 1``` it will ordered by column_name1
- you can order by 2 diffrent columns : ```SELECT column_name1,column_name2 FROM table_name ORDER BY 1,2```

## limit
this command will limit results to n 
 ```sql 
SELECT column_name FROM table_name LIMIT n;
```
you can give range to LIMIT command:
```sql 
SELECT column_name FROM table_name LIMIT start_point lenght;
```
example: ```SELECT title FROM books LIMIT 0 3;```
- for selecting to end of table you sould use big number as length
  
## like
you can search with this command
```sql 
SELECT column_name FROM table_name WHERE column_name LIKE '%string%'
```
- ```%``` means anything for example :```'%s``` will search for all words ends with s
- ```_``` means exactly one char : ```1_1``` will search for all words has 1 at fisrt then any char again 1 , `171` is accepted but `1781` is not accepted

--------------------------------------------------
# Aggregate Functions
## count
for counting the rows of a sample or the whole table, use COUNT function.
```sql
SELECT COUNT(*) FROM table_name;
```
## sumation
for sumation of numeric values in a column, use SUM function:
```sql
SELECT SUM(column_name) FROM table_name;
```
## min, max
for get minimum or maximum values in a special column, use MIN/MAX function:
```sql
SELECT MIN(column_name) FROM table_name;
SELECT MAX(column_name) FROM table_name;
```
## average
you can use AVG function for calculate average for numeric value in a column:
```sql
SELECT AVG(column_name) FROM table_name;
```
## group by
one of the aggregate tools in SQL is GROUP BY. with that you can categorized or grouping based on a special category or mark or something.
in below we can see a grouping base on column X:
```sql
SELECT column_name01, column_name02, ... FROM table_name
GROUP BY column_nameX;
```
- grouping by more than one column is possible. for example you can grouping by first name column and last name column.

- now you can combine previous function with GROUP BY:
```sql
# COUNT and GROUP BY
SELECT column_name01, column_name02, ... , COUNT(*) FROM table_name
GROUP BY column_nameX;

# MAX/MIN and GROUP BY
SELECT column_name01, column_name02, ..., Max(column_name03)
FROM table_name
GROUP BY column_name04, column_name05 , ...;

#and etc...
```
- for get a subset that sorted in MAX or MIN value you can try two way:
```sql
SELECT * FROM table_name
WHERE column_name = (SELECT Min(column_name) FROM tablename);
```
or
```sql
SELECT * FROM table_name  
ORDER BY column_name ASC LIMIT 1;
```
but in first way, using two selecting is not a good choice(it's not efficient and even slow to process)

--------------------------------------------------
# Data Type
### char vs varchar
char is fixed lenght
### int
### decimal
```decimal(total_digits,digit_after_decimal)```
### float and double
float and double are not fix point
### date 
'YYYY-MM-DD'
### time 
'HH:MM:SS'
### datetime
date + time 
### time funcs
![image](Users/ali79/Desktop/Screenshot.png)
# logical operators
## NOT
get all rows that is not equal to 'string':
```sql
SELECT column_name FROM table_name WHERE column_name != 'string'
```
## NOT LIKE 
it is uposite of ```LIKE```
```sql
SELECT column_name FROM table_name WHERE column_name NOT LIKE '%string%'
```
## Comparison

```sql
SELECT column_name FROM table_name WHERE column_name > n 
```
```sql
    >  -- Greater
    >= -- Greater equal
    <  -- Smaller
    <= -- Smaller and equal
```
## logical AND
```sql
-- this will select rows that both column1 = n and column2 = n is correct in them
SELECT column1,column2 FROM table_name WHERE column1 = n AND column2 = n 
-- onother way :
SELECT column1,column2 FROM table_name WHERE column1 = n && column2 = n 
```
## logical OR
```sql
-- this will select rows that column1 = n OR column2 = n is correct in them
SELECT column1,column2 FROM table_name WHERE column1 = n OR column2 = n 
-- onother way :
SELECT column1,column2 FROM table_name WHERE column1 = n || column2 = n 
```
## IN and NOT IN
we can use list for selection
```sql
-- this will select rows that column1 = str1 OR column1 = str2 is correct in them
SELECT * FROM table_name WHERE column1 IN ('str1','str2')
```
## BETWEEN and NOT BETWEEN
we can use a number range for selection
```sql
-- this will select rows that  n <= column1 <= m
SELECT * FROM table_name WHERE column1 BETWEEN n AND m
```
## case statment
you  can use conditions in selecting data
```sql
select * ,
        case
            when condition then "str1"
            else "str2"
        END  AS "column title"
    FROM table_name;
```


# join
## one to many
### foreign key
foreign key is a key that refers to another table`s primary key

you should set foreign key in creating table time like this
```sql
FOREIGN KEY (column_name) references table_name (othertable_column_name) 
-- this will conncect column_name column to other table column (othertable_column_name)
```
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
