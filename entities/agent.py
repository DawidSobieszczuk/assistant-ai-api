import json, traceback, datetime

from database import Database
from entity import Entity

from google import genai

class Agent(Entity) :
    def __init__(self, entity_id:int, database:Database) -> None:
        super().__init__(entity_id, database)
        results = self.database.query("""
            SELECT 
                agents.agent_id, 
                agents.agent_name, 
                agents.agent_description, 
                agents.agent_instruction,
                agents.llm_api_key_id,
                agents.llm_model,
                agents.llm_temperature,
                api_keys.api_key as llm_api_key
            FROM 
                agents 
                LEFT JOIN api_keys ON agents.llm_api_key_id = api_keys.api_key_id
            WHERE entity_id = %s""", 
            self.entity_id)
        
        if len(results) == 0:
            raise Exception(f"Agent with entity_id {entity_id} not found")
            # Pomyśl o tym, ale wydaje mi sie, że powinno wywalać bład a nie go obsługować
        
        result = results[0]

        self.agent_id:int = result["agent_id"]
        self.agent_name = result["agent_name"]
        self.agent_description = result["agent_description"]
        self.agent_instruction = result["agent_instruction"]
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

