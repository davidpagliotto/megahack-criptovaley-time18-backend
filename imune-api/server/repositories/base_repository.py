import uuid

from server.database.database import db
from server.exception.exception import NotFound
from server.models.base_model import ApiBaseModel


class BaseRepository:

    def __init__(self, collection_name, model_clazz):
        self.db = db
        self.collection = self.db.database[collection_name]
        self.model_clazz = model_clazz

    async def upsert(self, model: ApiBaseModel):
        model.guid = str(uuid.uuid4()) if not model.guid else str(model.guid)

        model_dict = model.dict()

        await self.collection.replace_one({'guid': {'$eq': model.guid}}, model_dict, upsert=True)

        return model

    async def get_all(self):
        cursor = self.collection.find()
        documents = await cursor.to_list(None)
        return [self.model_clazz.parse_obj(d) for d in documents]

    async def get_by_guid(self, guid):
        document = await self.collection.find_one({'guid': {'$eq': guid}})
        if document is None:
            raise NotFound("Item not found")
        return self.model_clazz.parse_obj(document)
