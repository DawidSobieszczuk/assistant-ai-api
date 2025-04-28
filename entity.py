import json

from config import Config
from database import Database

class Entity:
    def __init__(self, entity_id:int, database:Database) -> None:
        self.entity_id:int = entity_id
        self.database = database

    def send_message(self, message:json) -> json:
        raise NotImplementedError("send_message method not implemented in Agent class")