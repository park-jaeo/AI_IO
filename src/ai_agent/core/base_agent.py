from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import uuid
from datetime import datetime

# # 기본 클래스
# class BaseAgent(ABC):
#   def ___init__(self, agent_id : str = None):
#     self.agent_id = agent_id or str(uuid.uuid4())