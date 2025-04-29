import json, traceback, datetime
from typing import override

from config import Config
from database import Database
from entities.assistent import Assistant

from google import genai
from google.genai import types

class TalosAssistant(Assistant):
    def __init__(self, database:Database, user_entity_id:int):
        super().__init__(Config.entity_agent_basic_info, database)

        result = self.database.query("""
            SELECT
                users.assistant_pesonalization
            FROM
                users
            WHERE
                users.entity_id = %s
        """, user_entity_id)    

        assistant_personalization: str = result[0]["assistant_personalization"]

        self.chat = self.client.chats.create(
            model=self.llm_model,
            config=types.GenerateContentConfig(
                temperature=self.llm_temperature,
                system_instruction=self.assistent_instruction.format(
                    assistant_personalization = assistant_personalization,
                    assistant_entity_id = self.entity_id,
                    user_entity_id = user_entity_id,
                    agents_list = []
                )
            )
        )
