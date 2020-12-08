from src.services.config.ufer_conf import UFER_URI
import pymongo


def to_mongo(dic):
    try:
        client = pymongo.MongoClient(UFER_URI)
    except (AttributeError, pymongo.errors.OperationFailure):
        print("Impossible connect to the DataBase")
    else:
        db = client.Ufer
        collection = db.ufer_services
        collection.insert_one(dic)
        print("Inserting document")
    finally:
        print("...")

