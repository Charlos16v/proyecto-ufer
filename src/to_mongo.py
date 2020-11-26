import pymongo

def to_mongo(dic):
    client = pymongo.MongoClient("mongodb+srv://charlos:Ufer69@cluster0.35hqi.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client["Ufer"]
    collection = db["ufer_services"]
    collection.insert(dic)