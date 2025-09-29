from src.state.basic_state import State

class BasicChatbotNode:
    def __init__(self, model):
        self.llm = model

    def process(self, state:State):
        """ Process the input state and generate a response """
        return {"messages":self.llm.invoke(state["messages"])}
    