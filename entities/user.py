import json, datetime, requests

from database import Database
from entity import Entity

class User(Entity):
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)

        result = self.database.query("""SELECT 
                                        users.*,
                                        assistants.entity_id as assistant_entity_id
                                     FROM 
                                        users 
                                        LEFT JOIN assistants ON users.assistant_id = assistants.assistant_id
                                     WHERE users.entity_id = %s""", self.entity_id)[0]

        self.user_id = result["user_id"]
        self.user_name = result["user_name"]
        self.user_description = result["user_description"]
        self.assistant_id = result["assistant_id"]
        self.assistant_entity_id = result["assistant_entity_id"]
        self.assistant_personalization = result["assistant_personalization"]