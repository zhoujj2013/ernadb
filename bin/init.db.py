import os, sys
import pymongo

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

# init a databse named: test_database
db = client.test_database
collection = db.test_collection

# document
import datetime
post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

posts = db.posts

# insert a post
# result = posts.insert_one(post)
post_id = posts.insert_one(post).inserted_id

# db.collection_names(include_system_collections=False)

import pprint
pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

ppirnt.pprint(posts.find_one({"author": "Eliot"}))

post_id
pprint.pprint(posts.find_one({"_id": post_id}))

# failed
#post_id_as_str = str(post_id)
#posts.find_one({"_id": post_id_as_str})

# insert many
>>> new_posts = [{"author": "Mike",
...               "text": "Another post!",
...               "tags": ["bulk", "insert"],
...               "date": datetime.datetime(2009, 11, 12, 11, 14)},
...              {"author": "Eliot",
...               "title": "MongoDB is fun",
...               "text": "and pretty easy too!",
...               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
>>> result = posts.insert_many(new_posts)
>>> result.inserted_ids

for post in posts.find():
	pprint.pprint(post)

posts.count()


