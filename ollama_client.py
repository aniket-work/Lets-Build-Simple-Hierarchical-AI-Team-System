import requests

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3"):
        self.base_url = base_url
        self.model = model
    
    def generate(self, prompt: str, system_prompt: str = "") -> str:
        """Generate response using Ollama"""
        data = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False
        }
        try:
            response = requests.post(f"{self.base_url}/api/generate", json=data)
            response.raise_for_status()
            return response.json()["response"].strip()
        except Exception as e:
            return f"Error: {str(e)}"
