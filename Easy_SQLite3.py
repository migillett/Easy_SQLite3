# https://codereview.stackexchange.com/questions/182700/python-class-to-manage-a-table-in-sqlite
import sqlite3


class SqliteDatabase(object):
    def __init__(self, db_name=''):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print('Connected to database:', self.db_name)

    def create_table(self, table_name, table_config):
        command = f'CREATE TABLE IF NOT EXISTS {table_name} ({table_config});'
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def dict_to_sql(self, table, dictionary):
        columns = ', '.join('"' + str(x) + '"' for x in dictionary.keys())
        values = ', '.join('"' + str(x) + '"' for x in dictionary.values())
        self.execute(f'''INSERT OR REPLACE INTO {table}({columns}) VALUES ({values});''')

    def execute(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def sql_to_dict(self, select_query):
        try:
            self.connection.row_factory = sqlite3.Row
            things = self.connection.execute(select_query).fetchall()
            unpacked = [{k: item[k] for k in item.keys()} for item in things]
            return unpacked

        except Exception as e:
            print(f"Failed to execute. Query: {select_query}\n with error:\n{e}")
            return []

    def commit(self):
        self.connection.commit()
        print(f'Committed changes to {self.db_name}')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        if isinstance(exc_val, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
        print('Disconnected from database.')
