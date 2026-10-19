# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        # Changed constructor to accept credentials supplied by the dashboard -AO
        #
        USER = username 
        PASS = password 
        # Updated password for student specific password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT), authSource='admin') 
        #
        # Included authSource to dictate where to authenticate the account.
        # Does not change the database we are working with.
        #
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)
                # data should be dictionary
                return result.acknowledged
            except Exception as e:
                print("Create operation failed:", e)
                return False
        else:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                result = self.database.animals.find(query)
                return list(result)
            except Exception as e:
                print("Read operation failed:", e)
                return []
        else:
            return []
        
    # Create method to implement the U in CRUD.
    def update(self, query, data):
        if query is not None and data is not None:
            try:
                # Utilize update_many to support modifying multiple matching documents.
                result = self.database.animals.update_many(query, data)
                return result.modified_count
            except Exception as e:
                print("Update operation failed:", e)
                return 0
        else:
            return 0
    
    # Create method to implement the D in CRUD.
    def delete(self, query):
        if query is not None:
            try:
                # Utilize delete_many to allow method to handle multiple matching documents.
                # delete_many will permanently remove matching documents.
                # Use test_id when testing rather than a broad query.
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete operation failed:", e)
                return 0
        else:
            return 0
    