from foundation.core.schema.model import BaseModel
from schematics.types import StringType


class Post(BaseModel):
    title = StringType(required=True)
    content = StringType(required=True)
    user = StringType()
