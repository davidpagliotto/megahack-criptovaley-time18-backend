import uuid

from server.database.database import db
from server.models.base_model import ApiBaseModel


class BaseRepository:

    def __init__(self, collection_name):
        self.db = db
        self.collection = self.db.database[collection_name]

    async def upsert(self, model: ApiBaseModel):
        if not model.guid:
            model.guid = str(uuid.uuid4())

        model_dict = model.dict()

        await self.collection.replace_one({'guid': {'$eq': model.guid}}, model_dict, upsert=True)

        return model

    async def get_all(self):
        cursor = self.collection.find()
        documents = await cursor.to_list(None)
        return [ApiBaseModel.parse_obj(d) for d in documents]
