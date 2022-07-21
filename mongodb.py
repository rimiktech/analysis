''''
We have a pymongo class which has a method walk to yield all documents from a collection by given the skip and limit

'''
import pymongo

class MongoDBClient(object):
    SERVER = "xxxxxxx" #THIS WILL BE THE MONGODB CONNECTION SERVER.
    PORT = "" #THIS WILL BE THE PORT OF MONGODB SERVER.
    DATABASE = "xxxxxxxx" #THIS WILL BE THE DATABASE.

    def __init__(self, col, index=None):        
        connection = pymongo.Connection(MongoDBClient.SERVER, MongoDBClient.PORT)
        self.db = connection[MongoDBClient.DATABASE]
        self.collection = self.db[col]
        if index:
            self.collection.create_index(index, unique=True)
            
    """
    generator of all the documents in this collection
    """
    def walk(self, skip=0, limit=1000):
        hasMore = True
        while hasMore:
            res = self.collection.find(skip=skip, limit=limit)
            hasMore = (res.count(with_limit_and_skip=True) == limit)
            for x in res:
                yield x
            skip += limit