import json

from config import Config
from helper import Helper
from database import Database
from entitiesContext import EntitiesContext

from entities.user import User
from entities.assistants.talos import TalosAssistant

class App():
    def __init__(self):
        Config.load_from_file("config.yaml")
        self.database = Database(Config.mysql_host, Config.mysql_port, Config.mysql_database, Config.mysql_user, Config.mysql_password)

        self.user = User(2, self.database) #TODO: [29.04.2025] Dodaj logike wyboru użytkownika teraz jestem wpisany na sztywno !ta 2 ma zniknać!
        
        self.entities_context = EntitiesContext(self.database)
        self.entities_context.add_entity(TalosAssistant(self.database, self.user.entity_id))