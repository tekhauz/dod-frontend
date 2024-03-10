from pymongo import MongoClient

class MongoHandler:
    def __init__(self, mongodb_connection_string):
        self.client = MongoClient(mongodb_connection_string)
        self.db = self.client["fpds"]
        self.collection = self.db["contracts"]
    
    def insert_document(self, document):
        return self.collection.insert_one(document)
    
    def find_document(self, query):
        return self.collection.find_one(query)
    
    def get_con_count(self):
        num_contracts_values = self.db["metrics"].distinct("num_contracts")
        return num_contracts_values

    def update_document(self, query, update):
        return self.collection.update_one(query, {"$set": update})
    
    def delete_document(self, query):
        return self.collection.delete_one(query)
    
    def count_documents(self, query=None):
        if query:
            return self.collection.count_documents(query)
        else:
            return self.collection.estimated_document_count()
