from typing import List
from core_types import AgentRole, Message
from ollama_client import OllamaClient

class BaseAgent:
    def __init__(self, name: str, role: AgentRole, ollama_client: OllamaClient):
        self.name = name
        self.role = role
        self.ollama = ollama_client
        self.conversation_history: List[Message] = []
    
    def add_message(self, message: Message):
        self.conversation_history.append(message)
    
    def get_recent_context(self, limit: int = 5) -> str:
        recent = self.conversation_history[-limit:]
        context = "\n".join([f"{msg.agent}: {msg.content}" for msg in recent])
        return context
