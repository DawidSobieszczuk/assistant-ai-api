import json

from config import Config
from database import Database
from entity import Entity

from entities.system import System
from entities.assistants.talos import TalosAssistant
from entities.agents.basic_info import BasicInfoAgent

class EntitiesContext:
    def __init__(self, database:Database) -> None:
        self.entities = {}
        self.database = database
        
        #self.add_entity(BasicInfoAgent(self.database))
        self.add_entity(System(Config.entity_system, self.database))
    
    def add_entity(self, entity:Entity) -> None:
        self.entities[entity.entity_id] = entity

    def send_message(self, message:json, save_to_database:bool = True) -> json:
        # TODO: [29.04.2025] Dodaj sprawdzanie czy json jest prawidowy, stwórz dodatkową klasę lub urzyj klasy Helper

        if save_to_database and message["success"]:
            self.database.query("INSERT INTO messages (source_id, destination_id, message, timestamp) VALUES (%s, %s, %s, %s)", message["source_id"], message["destination_id"], "\n".join(message["message"]), message["timestamp"])

        # TODO: [29.04.2025] Dodaj logike zapisywania wiadomości do bazy danych w przypadku błędu - do przemyślenia

        if message["destination_id"] in self.entities:            
            response = self.entities[message["destination_id"]].send_message(message)

            return self.send_message(response, save_to_database)
        else:
            return message