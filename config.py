from configparser import ConfigParser
import os
  
class Config:

    def __init__(self):
        self.configur = ConfigParser() 
        self.configur.read('config.ini')
    
    def get(self, key):
        keys = key.split(".")
        if len(keys) == 2 and self.configur.has_option(keys[0], keys[1]): 
            return self.configur.get(keys[0], keys[1])
        return None

    def get_db_connection(self):
        h, u = self.get("DATABASE.HOST"), self.get("DATABASE.USER") 
        p, db = self.get("DATABASE.PASSWORD"), self.get("DATABASE.DB_NAME")
        port = self.get("DATABASE.PORT")
        return "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(u, p, h, port, db)