from foundation.common.log import getLogger
from .schema import Post

logger = getLogger(__name__)


def __setup__(module):
    module.resource("post", Post)

    @module.endpoint('/post/hello')
    def hel():
        return "hello"
