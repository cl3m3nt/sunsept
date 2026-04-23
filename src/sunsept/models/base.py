# sunsept/models/base.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any

# Define a type for messages
Message = Dict[str, str]

# Base class for any LLMs
class BaseLLM(ABC):
    # Abstract method to be implemented by subclasses
    @abstractmethod
    def __call__(
        self,
        messages: List[Message],
        **kwargs: Any
    ) -> Any:
        pass