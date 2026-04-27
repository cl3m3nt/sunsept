# sunsept/models/litellm_wrapper.py

from typing import List, Any
from litellm import completion
from sunsept.models.base import BaseLLM, Message
from importlib.metadata import version
import os

# env variables
LLM_MODEL = os.getenv('LLM_MODEL')
LITELLM_API_KEY = os.getenv("LITELLM_API_KEY")

# Greeting message
print("Greetings from LiteLLM Wrapper...")

# Check LiteLLM version
print("LiteLLM version:", version("litellm"))

# Defining the LiteLLMWrapper class
print("Defining LiteLLMWrapper...")
class LiteLLMWrapper(BaseLLM):
    def __init__(
        self,
        model: str = LLM_MODEL,
        temperature: float = 0.0,
        api_key=LITELLM_API_KEY,
        **default_kwargs: Any,
        
    ):
        self.model = model
        self.temperature = temperature
        self.default_kwargs = default_kwargs
        self.api_key = api_key

    def __call__(
        self,
        messages: List[Message],
        **kwargs: Any,
    ) -> str:
        merged_kwargs = {
            "temperature": self.temperature,
            **self.default_kwargs,
            **kwargs,
        }

        # completion comes from litellm package, it will call the API and return the response
        response = completion(
            model=self.model,
            messages=messages,
            **merged_kwargs,
            api_key=self.api_key
        )

        return (
            f"User prompt:\n"
            f"[user]: {messages[0]['content']}\n"
            f"LiteLLMWrapper response:\n"
            f"[LiteLLMWrapper response]:{response.choices[0].message.content}."
            f"[LiteLLMWrapper full response]: {response}"
        )