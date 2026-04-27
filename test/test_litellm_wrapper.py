from typing import List, Any
from sunsept.models.base import BaseLLM, Message
from sunsept.models.litellm_wrapper import LiteLLMWrapper



if __name__ == "__main__":
    print("Greetings from LiteLLM Wrapper test...")
    litellmwrapper = LiteLLMWrapper()
    print(litellmwrapper([{"role": "user", "content": "Hi, Clement speaking. How are you?"}]))