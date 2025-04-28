import datetime

from config import Config
from entitiesContext import EntitiesContext

class App():
    def __init__(self):
        Config.load_from_file("config.yaml")

        self.entities_context = EntitiesContext()

    def run_loop(self):
        while True:
            message = input("> ")
            if message.lower() == "exit":
                break

            message = {
                "source_id": Config.entity_app,
                "destination_id": Config.entity_system,
                "message": message,
                "timestamp": datetime.timestamp()
            }

            response = self.entities_context.send_message(message)
            print(response['message'])

App()