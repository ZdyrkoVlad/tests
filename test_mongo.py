from pymongo import MongoClient
import datetime
import pprint
client =MongoClient("mongodb+srv://vlad_kostya:123654@cluster0-tynru.mongodb.net/test?retryWrites=true")


# post = {"author": "DDSVW",
#        "text": "My first blog post!",
#        "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
# postone={"author":"CASDWDSA ","text":"My blog"
# }
# posts = db.posts
# post_id = posts.insert(post)

# postone_id=posts.insert_one(postone).inserted_id
# db.collection_names(include_system_collections=False)
# print(post_id)

# pprint.pprint(posts.find_one({"author":"Vlad"}))
    # pprint.pprint(posts.find_one({"_id":post_id}))
# posts.update(postone, {'$set': {'artist': 'Mariah Carey ft. Boyz II Men'}})
# pprint.pprint(posts.find_one({"_id":postone_id}))

# for i in db.test_database :
#     print(i)
