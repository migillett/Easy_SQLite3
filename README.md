# Easy SQLite3

## Introduction
This script is basically a way to speed up the importing and use of a SQLite3 database for python projects. All you have to do is import this python script into your python project and use it as if it were a class.

## Use
To get started, save the `easy_sqlite3.py` file in your project folder next to your other scripts or assets. There are 3 steps to get started:
1. Import the python script
2. Setup the db class and name your file
3. Define tables and their configuration
4. Insert data into the db
5. Commit changes

There are a few functions such as `dict_to_sql()` and `sql_to_dict()` that can convert dicionaries into sql and vice-versa. You can also iput data using the `execute()` command by doing `db.execute('insert into table values [...])`

## Example
Here's a quick example on how you'd use the script. Just be sure to `db.commit()` periodically or else no changes will be made to the database file.
```
from .EasySQLite3 import *

# saving this for later. Just make sure that your database keys are the same as the column names in your target table(s).
dict = {'id': 1, 'name': 'test'}

# Creates a database
db = SqliteDatabase('databasename.db')

# Creates a table
db.create_table(
  table_name='test',
  table_config='id REAL, name TEXT')

# Converts a dictionary to a SQL entry
db.dict_to_sql(
  table='test',
  dictionary=dict)

# Commit changes to the db file
db.commit()

# Pull data from the sql database and print it out
results = db.execute('''select name from test where id is "1"''')
for result in results:
  print(result)
```
