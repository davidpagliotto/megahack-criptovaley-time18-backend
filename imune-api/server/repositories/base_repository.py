import uuid

from server.database.database import db
from server.exception.exception import NotFoundException
from server.models.base_model import ApiBaseModel


class BaseRepository:

    def __init__(self, collection_name, model_clazz):
        self.db = db
        self.collection = self.db.database[collection_name]
        self.model_clazz = model_clazz

    async def upsert(self, model: ApiBaseModel, attr=None, value=None):
        model.guid = str(uuid.uuid4()) if not model.guid else str(model.guid)

        model_dict = model.dict()

        attr = 'guid' if not attr else attr
        value = model.guid if not value else value
        await self.collection.replace_one({attr: {'$eq': value}}, model_dict, upsert=True)

        return model

    async def get_all(self, parameters: dict = None):
        filters = {}
        if parameters is not None:
            for key, value in parameters.items():
                if value:
                    filters[key] = {'$eq': value}

        cursor = self.collection.find(filters)
        documents = await cursor.to_list(None)
        return [self.model_clazz.parse_obj(d) for d in documents]

    async def get_by_guid(self, guid):
        document = await self.collection.find_one({'guid': {'$eq': guid}})
        if document is None:
            raise NotFoundException("Item not found")
        return self.model_clazz.parse_obj(document)

    async def get_one_by_attr_value(self, attr, value):
        document = await self.collection.find_one({attr: {'$eq': value}})
        if document is None:
            raise NotFound("Item not found")
        return self.model_clazz.parse_obj(document)
