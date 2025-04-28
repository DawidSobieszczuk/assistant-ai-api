import json, traceback, datetime
from typing import override

from config import Config
from database import Database
from entities.agent import Agent

from google import genai
from google.genai import types


class BasicInfoAgent(Agent):
    def __init__(self, database:Database):
        super().__init__(Config.entity_agent_basic_info, database)

        self.chat = self.client.chats.create(
            model=self.llm_model,
            config=types.GenerateContentConfig(
                temperature=self.llm_temperature,
                system_instruction=self.agent_instruction.format(
                    agent_entity_id=self.entity_id,
                    agent_name=self.agent_name,
                    system_entity_id=Config.entity_system
                )
            )
        )

    