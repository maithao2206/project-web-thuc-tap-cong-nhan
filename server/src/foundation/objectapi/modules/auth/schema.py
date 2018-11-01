from foundation.core.schema.model import BaseModel
from schematics.types import StringType


class User(BaseModel):
    username = StringType(required=True)
    firstname = StringType(required=True)
    lastname = StringType()
    password = StringType()
