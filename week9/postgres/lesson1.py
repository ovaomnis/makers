"""
introducing to database.. Creating DB, tables
"""

# PostgreSQL - system to manage db (DBMS) Kit of application, which helps manage db and manipulate with data
# (CRUD)

# MySQL, Firebase, MongoDB, PostgreSQL, SQLite ...

# DB - data storage (managing, organization, structuring, processing and changing relation of information)

# \c <database> -> connect to database
# \d <database> -> show information about database
# \dt <database> -> show database tables
# \q -> quit from database
# \l -> list databases
# \du -> show users

"""
Filed Types in PostgreSql
"""

# Numeric Types\
# a. smallint(2 bytes) -> -32768 to 32768
# b. integer(4 bytes) -> -2,147,483,648 to 2,147,483,647
# c. bigint(8 bytes) -> -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 to 9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

# d. smallserial
# e. serial
# f. bigserial

# Character Types
# a. varchar(symbol amount) -> light in weight then other chart types max char 255
# b. char(symbol amount) ->  if say that char takes 50 and give 20 chars then other unfilled characters will replaces by space, max char 255
# c. text() -> takes unlimited amount of characters

# Boolean type
# a. boolean(1 byte) -> True/False, 1/0

# Data types
# a. date -> calendar date (year, month, day)

# Location types
# a. location -> coordinates -> {243, -23}

# alter role <user> with superuser createrole createdb; -> createing db
# create database <db_name>; -> creating db
# create database <db_name> with owner <user>; -> creating db with user
# grand all privileges on database <db_name> to user <user>; -> give all privileges
# create table <table_name>(column names);
# drop role <user>
# drop database <db_name>
# drop table <table_name>


'''ALTER TABLE'''

# alter table <table_name> rename to <new_table_name>;
# alter table <table_name> add column <column_name> <type> <constraint>;
# alter table <table_name> drop column <column_name>;
# alter table <table_name> rename column <column_name> to <new_column_name>;
# alter table <table_name> alter column <column> set/drop <constraint>;

'''
Relations
'''

# One to one
# one person has one id
# one author has one autobiography

# One to many
# One curator has many students

# Many to many
# one mentor many students, one student many mentors

# Foreign key -> outer key (with this key we create relations)
# Primary key -> (on primary key relations are created)


"""
JOIN -> instruction to join data from two tables
"""

"""
aggregation functions
"""
# SUM()
# MIN(), MAX()
# COUNT() -
# AVG() - find average


