from pymongo import MongoClient

from server.configurations.environment import env

client = MongoClient(env.database_url())
db = client.get_database(env.database_name())
