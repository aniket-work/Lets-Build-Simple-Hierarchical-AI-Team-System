from enum import Enum
from dataclasses import dataclass

class AgentRole(Enum):
    COORDINATOR = "coordinator"
    RESEARCHER = "researcher"
    WRITER = "writer"

@dataclass
class Message:
    role: str
    content: str
    agent: str
    timestamp: float
