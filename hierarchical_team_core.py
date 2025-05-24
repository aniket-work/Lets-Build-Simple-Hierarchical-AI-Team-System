import time
from typing import List, Dict
from ollama_client import OllamaClient
from coordinator_agent import CoordinatorAgent
from researcher_agent import ResearcherAgent
from writer_agent import WriterAgent

class HierarchicalTeam:
    def __init__(self, model: str = "llama3"):
        self.ollama = OllamaClient(model=model)
        self.coordinator = CoordinatorAgent(self.ollama)
        self.researcher = ResearcherAgent(self.ollama)
        self.writer = WriterAgent(self.ollama)
        self.task_history: List[Dict] = []
        
    def execute_task(self, initial_task: str, max_iterations: int = 5) -> str:
        print(f"🚀 Starting task: {initial_task}")
        print("=" * 60)
        current_task = initial_task
        final_result = ""
        iteration = 0
        while iteration < max_iterations:
            iteration += 1
            print(f"\n📋 Iteration {iteration}")
            print("-" * 30)
            context = self._get_recent_context()
            print("🎯 Coordinator analyzing task...")
            decision = self.coordinator.decide_next_action(current_task, context)
            if decision["agent"] == "COMPLETE":
                print(f"✅ Task completed: {decision['reasoning']}")
                break
            agent_name = decision["agent"]
            instruction = decision["instruction"]
            reasoning = decision["reasoning"]
            print(f"👤 Assigned to: {agent_name}")
            print(f"📝 Instruction: {instruction}")
            print(f"🤔 Reasoning: {reasoning}")
            if agent_name == "researcher":
                print("🔍 Researcher working...")
                result = self.researcher.research(instruction, context)
                self._log_result("researcher", instruction, result)
            elif agent_name == "writer":
                print("✍️ Writer working...")
                research_context = self._get_research_context()
                result = self.writer.write_content(instruction, research_context, context)
                self._log_result("writer", instruction, result)
                final_result = result
            print(f"📤 Result: {result[:200]}...")
            current_task = f"Continue with: {instruction}. Previous result: {result[:100]}..."
        return final_result or self._get_final_summary()
    def _get_recent_context(self, limit: int = 3) -> str:
        recent_tasks = self.task_history[-limit:]
        return "\n".join([f"{task['agent']}: {task['result'][:100]}..." for task in recent_tasks])
    def _get_research_context(self) -> str:
        research_results = [task['result'] for task in self.task_history if task['agent'] == 'researcher']
        return "\n\n".join(research_results)
    def _log_result(self, agent: str, task: str, result: str):
        self.task_history.append({
            "agent": agent,
            "task": task,
            "result": result,
            "timestamp": time.time()
        })
    def _get_final_summary(self) -> str:
        all_results = [task['result'] for task in self.task_history]
        return "\n\n".join(all_results)
