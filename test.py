# https://stackoverflow.com/questions/34774409/build-a-dynamic-update-query-in-psycopg2

'''
We have a class which is used to insert data from dictionary to mysql database. 
Please add a new method with name of "update" to update data from dictionary to mysqldb.

This function will accept three parameters:
1. data -- list of dictionaries having records
2. tableName -- which database table will be updated.
3. key -- which key from dictionary will be the primary column in database table.

'''


import os
from pickle import NONE
from sqlalchemy import create_engine
import pymysql


class mysqldb:

    LOGGER = None
    CONFIG = None

    def __init__(self):
        self.__config = mysqldb.CONFIG()
        self.connection = create_engine(self.__config.get_db_connection(), pool_recycle=3600)
        self.__connect()
        

    def __connect(self):
        h, u = self.__config.get("DATABASE.HOST"), self.__config.get("DATABASE.USER")
        p, db = self.__config.get("DATABASE.PASSWORD"), self.__config.get("DATABASE.DB_NAME")
        port = int(self.__config.get("DATABASE.PORT"))
        self.raw_connection = pymysql.connect(host=h, user=u, password=p, db=db, port=port)
    
    #execute insert query on table by using params(dictionary)
    def insert(self, data, tableName):
        if len(data) == 0: return True

        cursor = self.raw_connection.cursor()
        try:
            cols = ",".join(["`{0}`".format(l) for l in list(data[0].keys())])
            for d in data:
                query = "insert into {0}({1}) values{2}".format(tableName, cols, tuple(d.values()))
                query = query.replace("None", "NULL")
                print(cursor.mogrify(query))
                cursor.execute(query)
            cursor.close()
            self.raw_connection.commit()
            return True
        except Exception as e:
            mysqldb.LOGGER.log("Exeception occured:{}".format(e))
            cursor.close()
            return False


    #execute insert query on table by using params(dictionary)
    def update(self, data, tableName):
        if len(data) == 0: return True

        cursor = self.raw_connection.cursor()
        try:
            cols = ",".join(["`{0}`".format(l) for l in list(data[0].keys())])
            for d in data:
                query = "update {0} set {1} where {2} = {3}".format(tableName, cols, tuple(d.values()))
                query = query.replace("None", "NULL")
                cursor.execute(query)
            cursor.close()
            self.raw_connection.commit()
            return True
        except Exception as e:
            mysqldb.LOGGER.log("Exeception occured:{}".format(e))
            cursor.close()
            return False