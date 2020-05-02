from enum import Enum

from server.models.base_model import ApiBaseModel


class CategoryEnum(str, Enum):
    LAB = 'lab'
    SHIPPING = 'shipping '
    HEALTH_FACILITY = 'health_facility'
    WAREHOUSE = 'warehouse'
    FINAL_USER = 'final_user'


class PersonTypeEnum(str, Enum):
    PF = 'pf'
    PJ = 'pj'


class Person(ApiBaseModel):
    address: str = None
    type: PersonTypeEnum
    category: CategoryEnum
    enable: bool = True
    full_name: str
    document: str
