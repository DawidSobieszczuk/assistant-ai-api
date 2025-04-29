import json, datetime, requests

from database import Database
from entity import Entity

class User(Entity):
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)

        result = self.database.query("SELECT * FROM users WHERE entity_id = %s", self.entity_id)[0]

        self.user_id = result["user_id"]
        self.user_name = result["user_name"]
        self.user_description = result["user_description"]
        self.assistant_id = result["user_assistant_id"]
        self.assistant_personalization = result["user_assistant_personalization"]