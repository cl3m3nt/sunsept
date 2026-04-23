from typing import Optional, Callable, Any
from pydantic import BaseModel

# Pydantic model for tool
class Tool(BaseModel):
    name: str
    description: str
    func: Callable[..., Any]

# Agent main class
class Agent():
    def __init__(self, name: str, tools: Optional[list[Tool]] = None):
        self.name = name
        self.tools = tools or []

    def _list_tools(self) -> list[Tool]:
        return self.tools

    def _use_tool(self, tool_name: str, *args, **kwargs):
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found.")
        # Here you would implement the logic to use the tool based on its name and arguments.
        # This is a placeholder implementation.
        print(f"Using tool '{tool_name}' with arguments: {args} and keyword arguments: {kwargs}")
        return tool.func(*args, **kwargs)



