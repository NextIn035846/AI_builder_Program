from langgraph.graph import StateGraph,START,END
from src.state.basic_state import State
from src.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """Build a basic chatbot graph using Langgraph.
        This method initializes the graph structure and adds the necessary nodes and edges.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self, usecase):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        else:
            raise ValueError(f"Unknown use case: {usecase}")
        return self.graph_builder.compile()