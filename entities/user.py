import json, datetime, requests

from database import Database
from entity import Entity

class User(Entity):
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)