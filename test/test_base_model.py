from typing import List, Any
from sunsept.models.base import BaseLLM, Message


if __name__ == "__main__":

    class fakeLlm(BaseLLM):
        def __call__(self, messages: List[Message], **kwargs: Any) -> str:
            return "LLM response to: " + "[user]: " + messages[0]["content"] + " is [LLM response]: LLM speaking."

    llm = fakeLlm()
    print(llm([{"role": "user", "content": "Hi"}]))
