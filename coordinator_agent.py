from typing import Dict, Any
from base_agent import BaseAgent
from core_types import AgentRole
from ollama_client import OllamaClient
import json

class CoordinatorAgent(BaseAgent):
    def __init__(self, ollama_client: OllamaClient):
        super().__init__("Coordinator", AgentRole.COORDINATOR, ollama_client)
        self.available_agents = ["researcher", "writer"]
    
    def decide_next_action(self, task: str, context: str = "") -> Dict[str, Any]:
        system_prompt = """You are a project coordinator managing a team of AI agents.\nAvailable agents:\n- researcher: Can search for information, analyze topics, gather data\n- writer: Can create documents, summaries, reports, and written content\n\nYour job is to decide which agent should handle the current task.\nRespond with JSON format: {\"agent\": \"researcher|writer\", \"instruction\": \"specific task for the agent\", \"reasoning\": \"why this agent\"}\n\nIf the task is complete, respond with: {\"agent\": \"COMPLETE\", \"instruction\": \"\", \"reasoning\": \"task completed\"}"""
        prompt = f"""\nCurrent task: {task}\nRecent context: {context}\n\nWhich agent should handle this next? Provide your decision in JSON format.\n"""
        response = self.ollama.generate(prompt, system_prompt)
        print("DEBUG: Coordinator raw response:", response)
        try:
            return json.loads(response)
        except:
            if "researcher" in response.lower():
                return {"agent": "researcher", "instruction": task, "reasoning": "Detected research need"}
            elif "writer" in response.lower():
                return {"agent": "writer", "instruction": task, "reasoning": "Detected writing need"}
            else:
                print("DEBUG: Coordinator fallback triggered. Response was:", response)
                return {"agent": "COMPLETE", "instruction": "", "reasoning": "Unclear response"}
