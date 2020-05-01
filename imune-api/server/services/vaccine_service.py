import asyncio
import uuid

from server.database.database import db
from server.models.vacina_model import Vaccine


class VaccineService:
    @staticmethod
    async def index_vaccine(vaccine: Vaccine):
        vaccine.guid = vaccine.guid if vaccine.guid else str(uuid.uuid4())

        vaccine_dict = vaccine.dict()

        inserts = [asyncio.ensure_future(db.database.vaccines.insert_one(vaccine_dict.copy())) for r in range(5)]

        result = await db.database.vaccines.insert_one(vaccine_dict)

        await asyncio.gather(*inserts)

        print('result %s' % repr(result.inserted_id))
