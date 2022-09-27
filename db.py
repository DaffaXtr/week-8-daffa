import pymongo
import uuid 
import datetime

client = pymongo.MongoClient("mongodb+srv://daffa:xstore111@cluster0.pgbsxqu.mongodb.net/?retryWrites=true&w=majority")
db = client.MyRepo
collection = db.MyCollect

def save_to_db(kecepatan, latitude, longitude) -> tuple:
    try:
        data = {
            "request_id": str(uuid.uuid4()),
            "kecepatan": kecepatan,
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": datetime.datetime.now()
        }

        rec_id1 = collection.insert_one(data)

        print("Data inserted with record ids",rec_id1)
        return True,None
    except Exception as e:
        return False,str(e)

save_to_db(90, -7.8114, 112.0255)