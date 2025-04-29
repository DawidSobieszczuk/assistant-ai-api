import json, datetime, requests

from database import Database
from entity import Entity

class System(Entity):
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)
    
    def send_message(self, message:json) -> json:
        match message["action_type"]:
            case "get_datetime":
                return self.get_datetime(message)
            case "get_data_from_external_api":
                return self.get_data_from_external_api(message)
            case _:
                return {
                    "success": False,
                    "error": "Invalid action type",
                    "error_details": {
                        "action_type": message["action_type"]
                    },
                    "source": self.entiry_id,
                    "destination": message["source_id"],
                    "timestamp": datetime.datetime.now()
                }
            
    def get_datetime(self, message:json) -> json:
        return {
            "success": True,
            "message": ["Wszystkie inforamacje w polu 'data'"],
            "data": {
                "datetime": datetime.datetime.now().isoformat()
            },
            "source": self.entiry_id,
            "destination": message["source_id"],
            "timestamp": datetime.datetime.now()
        }
    
    def get_data_from_external_api(self, message:json) -> json:
        url = message["action_details"]["url"]

        response = requests.get(url)

        return {
            "success": True,
            "message": ["Wszystkie inforamacje z api w polu 'data'"],
            "data": response.json(),
            "source": self.entiry_id,
            "destination": message["source_id"],
            "timestamp": datetime.datetime.timestamp(datetime.datetime.now())
        }