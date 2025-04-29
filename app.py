import datetime

from config import Config
from entitiesContext import EntitiesContext

from entities.user import User

class App():
    def __init__(self):
        Config.load_from_file("config.yaml")

        #TODO: [20.04.2025] Wyciagnij tworzenie obiektu database tutaj i dodaj jakko parametr do obiektów ponirzej
        self.entities_context = EntitiesContext()
        self.user = User(2, self.entities_context.database)

    def run_loop(self):
        while True:
            message = input("> ")
            if message.lower() == "exit":
                break

            message = {
                "source_id": Config.entity_app,
                "destination_id": Config.entity_system,
                "message": message,
                "timestamp": datetime.datetime.now()
            }

            response = self.entities_context.send_message(message)
            print(response['message'])