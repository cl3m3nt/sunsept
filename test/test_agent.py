# Main
from sunsept.agent import Tool
from sunsept.agent import Agent


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
    calculator_result = agent._use_tool("Calculator", a=5, b=3)  
    print(f"Calculator tool result: {calculator_result}") 

    weather_result = agent._use_tool("WeatherAPI", location="Paris")
    print(f"Weather tool result: {weather_result}") 