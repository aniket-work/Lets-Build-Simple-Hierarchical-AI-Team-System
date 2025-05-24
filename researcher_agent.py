from base_agent import BaseAgent
from core_types import AgentRole
from ollama_client import OllamaClient

class ResearcherAgent(BaseAgent):
    def __init__(self, ollama_client: OllamaClient):
        super().__init__("Researcher", AgentRole.RESEARCHER, ollama_client)
    
    def research(self, topic: str, context: str = "") -> str:
        system_prompt = """You are a research specialist. Your job is to:\n1. Analyze the research topic thoroughly\n2. Provide detailed information and insights\n3. Suggest key points that should be covered\n4. Identify important aspects that need further investigation\n\nBe comprehensive but concise. Focus on factual information and useful insights."""
        prompt = f"""\nResearch Topic: {topic}\nContext from previous work: {context}\n\nPlease provide a comprehensive research summary on this topic.\n"""
        return self.ollama.generate(prompt, system_prompt)
