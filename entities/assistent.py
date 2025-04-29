import json, traceback, datetime

from database import Database
from entity import Entity

from google import genai

class Assistant(Entity):
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)
        result = self.database.query("""
            SELECT 
                assistents.agent_id, 
                assistents.agent_name, 
                agents.agent_description,
                assistents.llm_api_key_id,
                assistents.llm_model,
                assistents.llm_temperature,
                api_keys.api_key as llm_api_key
            FROM 
                assistents
                LEFT JOIN api_keys ON assistents.llm_api_key_id = api_keys.api_key_id
            WHERE entity_id = %s""", 
            self.entity_id)

        self.assistent_id:int = result[0]["assistents_id"]
        self.assistent_name = result[0]["assistents_name"]
        self.assistent_instruction:str = result[0]["assistents_instruction"]
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
                "timestamp": datetime.datetime.now()
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
                "timestamp": datetime.datetime.now()
            }