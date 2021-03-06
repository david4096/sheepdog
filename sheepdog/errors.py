"""
TODO
"""

from cdiserrors import *

from sheepdog.globals import (
    SUPPORTED_FORMATS,
)

class UnsupportedError(UserError):

    def __init__(self, file_format, code=400, json=None):
        if json is None:
            json = {}
        message = (
            "Format {} is not supported; supported formats are: {}."
            .format(file_format, ",".join(SUPPORTED_FORMATS))
        )
        super(UnsupportedError, self).__init__(message, code, json)
