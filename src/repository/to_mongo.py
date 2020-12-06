import pymongo

# LIBS== PYMONGO, DNSPYTHON
def to_mongo(dic):
    # try:
    uri = "mongodb+srv://charlos:Ufer69@cluster0.35hqi.mongodb.net/Ufer?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    db = client.Ufer
    collection = db.ufer_services
    collection.insert_one(dic)  # else añadir upsert true
    # except Exception:
        # print("Impossible connect to the DataBase")


# finally: terminar conex bbdd