import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from server.configurations.environment import env


class DataBase:
    client: AsyncIOMotorClient = None
    database = None


db = DataBase()


async def connect_to_mongo():
    db.client = motor.motor_asyncio.AsyncIOMotorClient(env.database_url())
    db.database = db.client[env.database_name()]


async def close_mongo_connection():
    db.client.close()


async def apply_migrations():
    db.database.vaccines.create_index("guid", unique=True)
