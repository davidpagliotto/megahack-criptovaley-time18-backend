from server.exception.exception import BusinessValidationException
from server.models.person_model import Person, CategoryEnum
from server.repositories.person_repository import PersonRepository
from server.services.base_service import BaseService
from server.services.utils import is_cpf_valid, is_cnpj_valid, keep_only_numbers


class PersonService(BaseService):

    def __init__(self):
        super().__init__(PersonRepository())

    @staticmethod
    async def validate_document(document, raise_exception=True) -> str:
        document_only_numbers = keep_only_numbers(document)
        keep_only_numbers_on_model = False
        if len(document_only_numbers) == 11:
            if not is_cpf_valid(document_only_numbers) and raise_exception:
                raise BusinessValidationException('Cpf not valid')
            else:
                keep_only_numbers_on_model = True
        elif len(document_only_numbers) == 14:
            if not is_cnpj_valid(document_only_numbers) and raise_exception:
                raise BusinessValidationException('Cnpj not valid')
            else:
                keep_only_numbers_on_model = True

        if keep_only_numbers_on_model:
            return document_only_numbers
        else:
            return document

    async def upsert(self, person: Person):
        if person.category != CategoryEnum.FINAL_USER and person.address is None:
            raise BusinessValidationException('This category of user requires address attribute')

        if person.document:
            document = await self.validate_document(person.document)
            person.document = document

        return await super().upsert(person)

    async def get_by_guid(self, guid):
        return await self._repository.get_by_guid(guid)

    async def get_all(self, parameters=None):

        if parameters.get('document'):
            parameters['document'] = await self.validate_document(parameters['document'], raise_exception=False)

        return await super().get_all(parameters)
