from pymongo import MongoClient


class MongoBase(object):
    def __init__(self, host, port):
        self.client =  MongoClient('mongodb://' + host + port)
         
    def switchDataBase(self, db_name):
        try:
            self.db = self.client[db_name]
        except:
            return False
        else:
            return True

    def conCollection(self, collection_name):
        try:
            self.collection = self.db[collection_name]
        except:
            return False
        else:
            return True

    def getDocument(self, query_object):
        try:
            self.document = self.collection.find_one(query_object)
            return self.document
        except:
            return False
        else:
            return True

    def getData(self, query_object, query_key):
        try:
            self.getDocument(query_object)
            self.data = self.document
            return self.data
        except:
            return False
        else:
            return True

    def inserDocument(self, document):
        try:
            self.retId = self.collection.insert_one(document)
        except:
            return False
        else:
            return True