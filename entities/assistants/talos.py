import json, traceback, datetime
from typing import override

from config import Config
from database import Database
from entities.assistant import Assistant

from google import genai
from google.genai import types

class TalosAssistant(Assistant):
    def __init__(self, database:Database, user_entity_id:int):
        super().__init__(1, database) # TODO: Change to Config.entity_assistant_talos

        result = self.database.query("""
            SELECT
                *
            FROM
                users
            WHERE
                users.entity_id = %s
        """, user_entity_id)[0]

        user_name: str = result["user_name"]
        user_description: str = result["user_description"]
        assistant_personalization: str = result["assistant_personalization"]

        self.chat = self.client.chats.create(
            model=self.llm_model,
            config=types.GenerateContentConfig(
                temperature=self.llm_temperature,
                system_instruction=self.assistent_instruction.format(
                    user_name = user_name,
                    user_description = user_description,
                    assistant_personalization = assistant_personalization,
                    assistant_entity_id = self.entity_id,
                    user_entity_id = user_entity_id,
                    agents_list = []
                )
            )
        )
