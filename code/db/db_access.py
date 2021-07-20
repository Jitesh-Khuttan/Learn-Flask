import sqlite3
import os
from contextlib import contextmanager
from code.db.db_utils import validate_params_for_executemany
from code.db.config import db_dir_path

class DBAccess:

    def __init__(self, db_name):
        self.db_path = os.path.join(db_dir_path, db_name)

    @contextmanager
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            yield self
        finally:
            self.close()

    def close(self):
        self.connection.close()

    def retrieve(self, sql, params=None, executemany=False, fetchall=True):
        """
        Function to query the data from DB.
        :param sql: query to run.
        :param params: parameters to pass to query
        :param fetchall: set to True, if you want all results of query.
        :param executemany: set to True, if you want to query for multiple inputs. params should not be None in this case.

        :return: a list of tuples - in case of fetchall = True, else a tuple.
        """
        if executemany:
            params = validate_params_for_executemany(params)
        execute_func = self.cursor.executemany if executemany else self.cursor.execute
        if params:
            execute_func(sql, params)
        else:
            execute_func(sql)

        result = self.cursor.fetchall() if fetchall else self.cursor.fetchone()
        return result


    def execute(self, sql, params=None, executemany=False, commit=False):
        """
        Function to execute given query. Use it to insert, update, delete or create data.
        :param sql: query to execute.
        :param params: a tuple (or) list of tuples.
        :param executemany: if True, execute for multiple inputs. (i.e. params is expected to be a list of tuples)
        :param commit: commit the transaction.
        :return: Number of rows inserted.
        """
        if executemany:
            params = validate_params_for_executemany(params)
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

        if commit:
            self.connection.commit()


