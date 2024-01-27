from .route import Route
from ..enums import HTTPMethods


class Delete(Route):
    def __init__(self, path: str):
        super().__init__(path, HTTPMethods.DELETE)
