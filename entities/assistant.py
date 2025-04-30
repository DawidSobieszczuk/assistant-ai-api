import json, traceback, datetime, time

from database import Database
from entity import Entity

from google import genai
from google.genai import errors

from helper import Helper

class Assistant(Entity):
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)
        result = self.database.query("""
            SELECT 
                assistants.*,
                api_keys.api_key as llm_api_key
            FROM 
                assistants
                LEFT JOIN api_keys ON assistants.llm_api_key_id = api_keys.api_key_id
            WHERE assistants.entity_id = %s""", 
            self.entity_id)[0]
            
        self.assistent_id:int = result["assistant_id"]
        self.assistent_name = result["assistant_name"]
        self.assistent_instruction:str = result["assistant_instruction"]
        self.llm_api_key = result["llm_api_key"]
        self.llm_model = result["llm_model"]
        self.llm_temperature = result["llm_temperature"]
        
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
                "timestamp": Helper.get_timestamp()
            }

        string_message = json.dumps(message)
        try:
            response = self.chat.send_message(string_message)
            try:
                return json.loads(response.text[7:-4], strict=False)
            except:
                return {
                    "success": False,
                    "error": "Invalid JSON response from LLM",
                    "error_details":{
                        "raw_response": response.text,
                        "error_msg": traceback.format_exc()
                    },                    
                    "source_id": self.entity_id,
                    "destination_id": message["source_id"],
                    "timestamp": Helper.get_timestamp()
                }
        except errors.APIError as e:
            if(e.code == 503):
                return {
                    "success": False,
                    "error": "Service Unavailable",                  
                    "source_id": self.entity_id,
                    "destination_id": message["source_id"],
                    "timestamp": Helper.get_timestamp()
                }
            elif(e.code == 429):
                return {
                    "success": False,
                    "error": "Rate Limit Exceeded",                  
                    "source_id": self.entity_id,
                    "destination_id": message["source_id"],
                    "timestamp": Helper.get_timestamp()
                }