from pymongo import MongoClient
mc = MongoClient()
db=mc["test_database"]
    for i in db["posts"].find({}):
    print(i)
