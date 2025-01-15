from Part8_RagConseptandAgent.graph.chains.generation import generation_chain
from Part8_RagConseptandAgent.graph.state import GraphState
from typing import Any,Dict

def generate(state: GraphState) -> Dict[str,Any]:

    print("-----GENERATE-----")
    question = state["question"]
    documents = state["documents"]

    generation = generation_chain.invoke(
        {"context":documents,"question":question}
    )
    return {"documents":documents,"question":question,"generation":generation}