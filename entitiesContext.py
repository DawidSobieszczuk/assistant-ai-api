import json

from config import Config
from database import Database
from entity import Entity

from entities.system import System
from entities.agents.basic_info import BasicInfoAgent

class EntitiesContext:
    def __init__(self):
        self.entities = {}
        self.database = Database(Config.mysql_host, Config.mysql_port, Config.mysql_database, Config.mysql_user, Config.mysql_password)
        
        self.add_entity(BasicInfoAgent(self.database))
        self.add_entity(System(self.database))
    
    def add_entity(self, entity:Entity) -> None:
        self.entities[entity.entity_id] = entity

    def send_message(self, message:json, save_to_database:bool = True) -> json:
        if save_to_database:
            self.database.query("INSERT INTO messages (source_id, destination_id, message, timestamp) VALUES (%s, %s, %s, %s)", (message["source_id"], message["destination_id"], message["message"], message["timestamp"]))

        if message["destination_id"] in self.entities:            
            response = self.entities[message["destination_id"]].send_message(message)

            return self.send_message(response, save_to_database)
        else:
            return message