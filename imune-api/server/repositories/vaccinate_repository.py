from server.enums.enums import Collections
from server.models.vaccinate_model import Vaccinate, VaccinateOutput
from server.repositories.base_repository import BaseRepository


class VaccinateRepository(BaseRepository):

    def __init__(self):
        super().__init__(Collections.VACCINATES.value, Vaccinate)

    async def get_all(self, parameters: dict = None):
        cursor = self.collection.aggregate([{
            '$lookup': {
                'from': 'vaccines',
                'localField': 'vaccine',
                'foreignField': 'guid',
                'as': 'vaccine_obj'
            }
        }, {
            '$project': {
                'vaccine_obj': {
                    '$arrayElemAt': ["$vaccine_obj", 0]
                },
                'document': "$$ROOT"
            }
        }])

        documents = await cursor.to_list(None)
        ret = []
        for d in documents:
            vaccinate_response = d['document']
            vaccinate_response['vaccine_obj'] = d['vaccine_obj']
            vaccine_output = VaccinateOutput.parse_obj(vaccinate_response)
            ret.append(vaccine_output)
        return ret
