import json, traceback, datetime

from database import Database
from entity import Entity

from google import genai
from google.genai import types

class Agent(Entity) :
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)
        result = self.database.query("SELECT * FROM agents WHERE entity_id = %s", self.entity_id)

        self.agent_id:int = result[0]["agent_id"]
        self.agent_name = result[0]["agent_name"]
        self.agent_description = result[0]["agent_description"]
        self.agent_instruction = result[0]["agent_instruction"]
        self.llm_api_key = result[0]["llm_api_key"]
        self.llm_model = result[0]["llm_model"]
        self.llm_temperature = result[0]["llm_temperature"]
        
        self.client = genai.Client(
            api_key=self.llm_api_key
        )

        self.chat = None

    def send_message(self, message:json) -> json:
        if self.chat is None:
            return {
                "success": False,
                "error": "Chat session not initialized",
                "source": self.entity_id,
                "destination": message["source_id"],
                "timestamp": datetime.timestamp()
            }

        self.chat.send_message(message)
        response = self.chat.get_response()
        try:
            return json.load(response.text[7:-4], strict=False)
        except:
            return {
                "success": False,
                "error": "Invalid JSON response from LLM",
                "error_details":{
                    "raw_response": response.text,
                    "error_msg": traceback.format_exc()
                },                    
                "source": self.entiry_id,
                "destination": message["source_id"],
                "timestamp": datetime.timestamp()
            }

