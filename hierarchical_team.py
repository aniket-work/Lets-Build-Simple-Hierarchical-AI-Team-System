#!/usr/bin/env python3
"""
Simple Hierarchical AI Team using only Ollama
Simplified version of LangGraph hierarchical agent teams
"""

from hierarchical_team_core import HierarchicalTeam
import time

# Example usage
def main():
    # Initialize the team
    team = HierarchicalTeam(model="llama3")  # Change model as needed
    
    # Example tasks
    tasks = [
        "Research and write a comprehensive guide about renewable energy sources",
        "Create a business plan summary for a sustainable tech startup",
        "Research current AI trends and write a technical blog post about them"
    ]
    
    for i, task in enumerate(tasks, 1):
        print(f"\n🎯 TASK {i}: {task}")
        print("=" * 80)
        
        try:
            result = team.execute_task(task, max_iterations=4)
            
            print(f"\n🎉 FINAL RESULT:")
            print("=" * 50)
            print(result)
            print("\n" + "="*80 + "\n")
            
        except Exception as e:
            print(f"❌ Error executing task: {e}")
        
        # Small delay between tasks
        time.sleep(2)

if __name__ == "__main__":
    print("🤖 Hierarchical AI Team with Ollama")
    print("Make sure Ollama is running with your preferred model")
    print("Default model: llama3 (change in code if needed)")
    print("\n")
    
    main()