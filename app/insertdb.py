from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random

user = 'krishna'           # username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
password = 'vedantha'       # password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
host = 'mongodb-service'    # service name of the mongodb admin server as set in mongo-service.yaml
port = 27017              # port number of the mongodb admin server as set in mongo-deployment.yaml
conn_string = f'mongodb://{user}:{password}@{host}:{port}'

db = MongoClient(conn_string).blog
createdAt = datetime.now()
db.posts.insert_one({"title": "Blog By Karthikeya(PES1UG20CS200)", "author": "Karthikeya R Jenni", "createdAt": createdAt})
createdAt = datetime.now()
db.posts.insert_one({"title": "Blog By Krishna(PES1UG20CS219)", "author": "Krishna Vedantha", "createdAt": createdAt})
createdAt = datetime.now()
db.posts.insert_one({"title": "Blog By Kunal(PES1UG20CS225)", "author": "Kunal Kathare", "createdAt": createdAt})
createdAt = datetime.now()
db.posts.insert_one({"title": "Blog By Nahush(PES1UG20CS239)", "author": "Nahush Kashyap", "createdAt": createdAt})
