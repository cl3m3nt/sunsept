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

# Main
if __name__ == "__main__":

    # Tool functions
    def add_number(a: int, b: int) -> int:
        return a + b

    def get_weather(location: str) -> str:
        return f"Weather information for {location}"

    # Tool instances
    tool1 = Tool(name="Calculator", description="Performs basic arithmetic operations.", func=add_number)
    tool2 = Tool(name="WeatherAPI", description="Provides weather information.", func=get_weather)
    tools_list = [tool1, tool2]

    # Agent instance
    agent = Agent(name="MyAgent", tools=[tool1, tool2])

    # Agent tools print
    print(agent._list_tools())

    # Agent tool use
    calculator_result = agent._use_tool("Calculator", a=5, b=3)  # Output: Using tool 'Calculator' with arguments: (5, 3) and keyword arguments: {}
    print(f"Calculator tool result: {calculator_result}") 

    weather_result = agent._use_tool("WeatherAPI", location="Paris")
    print(f"Weather tool result: {weather_result}")  # Output: Using tool 'WeatherAPI' with arguments: ('New York',) and keyword arguments: {}

