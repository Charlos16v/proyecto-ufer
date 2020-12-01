import pymongo

# LIBS== PYMONGO, DNSPYTHON
def to_mongo(dic):
    try:
        client = pymongo.MongoClient("mongodb+srv://charlos:Ufer69@cluster0.35hqi.mongodb.net/<dbname>?retryWrites=true&w=majority")
        db = client["Ufer"]
        collection = db["ufer_services"]
        collection.insert_one(dic)
    except Exception:
        print("Impossible connect to the DataBase")
