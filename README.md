# Project datafun-05-sql
## Author
*    [Jordan](httpls://github.com/JfromNWMS)

## Overview

This project integrates Python and SQL, focusing on database interactions using SQLite.
The project involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

This project contains three modules that utilize four directories within the root directory fo the project.  Description of the modules and their working directories is as follows:

### db01_setup.py

Contained in this module are four functions.  create_database() opens and closes a connection to the database in the data directory to ensure the databases existence.  insert_data_from_csv() utilizes pandas to read author.csv and book.csv in the data directory located within the project root directory and inserts the records from the CSV files into the database.  execute_sql() takes in a mandatory pathlib.Path object, reads the SQL file from the given path, and then executes the script in the database.  query_sql() takes in a mandatory pathlib.Path object, reads the SQL file from the given path, executes the the SQL script from the SQL file in the database, and then returns a pandas.DataFrame with the results of the SQL script execution. 

The main() function of db01_setup calls execute_sql() on all files in the sql_create directory.  Contained within the sql_create directory are three SQL script files whose descriptions are as follows:  

01_drop_tables.sql drops the authors and books tables from the database.  

02_create_tables.sql creates the authors and books tables in the database following the schema:

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

02_insert_records.sql inserts 10 records into each of the authors and books tables of the database following the schema above.

After installing dependencies from requiredments.txt execute "PS> py db01_setup.py" in a powershell terminal to run the file which will create the database if it doesn't exist, drop existing authors and books tables, create tables for authors and books, and then insert records for the authors and books tables.  See requirements.txt for instructions on how to set up a virtual environment for the project and how to install dependencies in the virtual environment.

### db02_features.py

This module contains only the main function which itterates through all the SQL script files in the sql_features directory and utilizes the execute_sql() function from db01_setup.py to execute the SQL script files.

Contained in the sql_features directory are two SQL script files whose descriptions are as follows:

delete_records.sql deletes the record(s) from the authors table where the first_name column is equal to 'Harper'.

update_records.sql updates the books table by changing the fields under the year_published column to '1950' where the title column is equal to '1984'.

After installing dependencies from requiredments.txt execute "PS> py db02_features.py" in a powershell terminal to run main().  See requirements.txt for instructions on how to set up a virtual environment for the project and how to install dependencies in the virtual environment.

### db03_queries.py

This module contains only the main function which itterates through all the SQL script files in the sql_queries directory and utilizes the query_sql() function from db01_setup.py to execute the SQL script files.

Contained in the sql_features directory are two SQL script files whose descriptions are as follows:

query_aggregation.sql checks within the books table whether or not the sum of all year_published fields divided by the average of all year_published fields is equal to the number of distinct fields under year_published and returns a string denoting the distinctness of all the year_published fields.

query_filter.sql selects last_name from the authors table and title from the books table joined corresponding to author_id and filters the result set rows on the occurence of a '2' in fields under author_id in the authors table.

query_group_by.sql selects the authors last name from the authors table and the title column in the books table where they are joined corresponding to author_id.  The result set is then filtered to show only records where the authors table last_name field starts with a vowel and then rows are grouped on the combinations of last_name in the authors table and title in the books table.

query_join.sql selects all distinct combinations of authors and their respective books, inner joins them corresponding to author_id, and then orders the result set by the title of their books in ascending order.

query_sorting.sql selects fields under last_name in the authors table and the last year the author published a book from year_published in the books table.  The result set is then grouped by last_name from the authors table and ordered by the last year they published a book.

After installing dependencies from requiredments.txt execute "PS> py db03_queries.py" in a powershell terminal to run main().  See requirements.txt for instructions on how to set up a virtual environment for the project and how to install dependencies in the virtual environment.

---
## Specifications for Project datafun-05-sql
---

## Step 1: Start Project, Open in VS Code

Start a project as usual. 
1. Create a repo in GitHub with a default README.md. Name the repo **datafun-05-sql**. 
2. Clone your new repo down to the Projects folder on your machine. 
3. Open your new project repository folder in VS Code.

---

## Step 2: Add/Update Critical Files

With your new project repo folder open in VS Code, add/update critical project files at the start of every project. 

### Add/Add .gitignore

- The .gitignore file tells Git files to ignore when committing changes.
- Review/copy the example .gitignore file, you might be able to use it without modification.

### Add/Update requirements.txt

- The requirements.txt file lists the packages used in the project.
- Review/copy the example requirements.txt file, you might be able to use it without modification.
- You may not need all the listed packages - and may want to add others. Modify the requirements.txt as needed.

### Update README.md

- Edit and customize your README.md to provide an overview of the project and instructions for running it.
 
### Git add-commit-push

After adding .gitignore (or any other key file), run git add, commit, and push to commit your changes to GitHub. 

```shell
git add .
git commit -m "Add .gitignore and requirements.txt"
git push -u origin main
```

---

## Step 3: Set up Virtual Environment

Next, create and activate a virtual environment for this project. 
Also install additional dependencies required for this project.
See [requirements.txt](requirements.txt) for detailed instructions. 

A. Create .venv
B. Activate .venv
C. Install dependencies into .venv
D. Select VS Code interpreter to use .venv

## Step 4: Schema Design and Database Initialization

Design a schema with at least two related tables, including foreign key constraints.
Document the schema design in your README.md.

sql_create folder:

- 01_drop_tables.sql - drop tables to restart
- 02_create_tables.sql - create your database schema using sql 
- 03_insert_records.sql - insert at least 10 additional records into each table.

db01_setup.py:

Create a Python script that demonstrates the ability to create a database, define a schema, and insert records. 
Make it easy to re-run by dropping the tables first.




## Step 5. Cleaning and Feature Engineering

Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements.
You might create an additional table, insert new records,
and perform data querying (with filters, sorting, and joining tables),
data aggregation, and record update and deletion.

sql_features folder:

1. update_records.sql - update 1 or more records in a table.
2. delete_records.sql - delete 1 or more records from a table.

db02_features.py

Create a Python script that demonstrates the ability to run sql scripts 
to interact with fields, update records, delete records, and maybe add additional columns. 



## Step 6. Perform Aggregations and queries

Implement SQL statements and queries to perform aggregations and queries.

sql_queries folder: 

1. query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
2. query_filter.sql - use WHERE to filter data based on conditions.
3. query_sorting.sql - use ORDER BY to sort data.
4. query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
5. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

Use Python to execute the SQL queries and maybe chart, illustrate, and/or summarize your findings:

db03_queries.py
