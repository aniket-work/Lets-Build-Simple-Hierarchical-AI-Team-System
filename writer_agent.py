from base_agent import BaseAgent
from core_types import AgentRole
from ollama_client import OllamaClient

class WriterAgent(BaseAgent):
    def __init__(self, ollama_client: OllamaClient):
        super().__init__("Writer", AgentRole.WRITER, ollama_client)
    
    def write_content(self, instruction: str, research_data: str = "", context: str = "") -> str:
        system_prompt = """You are a professional writer. Your job is to:\n1. Create well-structured, engaging content\n2. Use provided research data effectively\n3. Ensure clarity and readability\n4. Follow the specific instructions given\n\nWrite in a professional yet accessible style."""
        prompt = f"""\nWriting Instruction: {instruction}\nResearch Data: {research_data}\nPrevious Context: {context}\n\nPlease create the requested content.\n"""
        return self.ollama.generate(prompt, system_prompt)
