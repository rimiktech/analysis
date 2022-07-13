import pymongo

class MongoDBClient(object):
    SERVER = "" #THIS WILL BE THE MONGODB CONNECTION SERVER.
    PORT = "" #THIS WILL BE THE PORT OF MONGODB SERVER.

    def __init__(self, col, index=None):        
        connection = pymongo.Connection(MongoDBClient.SERVER, MongoDBClient.PORT)
        self.db = connection[settings.MONGODB_DB]
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