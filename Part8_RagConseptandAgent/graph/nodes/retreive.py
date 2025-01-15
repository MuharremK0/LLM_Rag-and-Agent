from Part8_RagConseptandAgent.ingestion import retriever
from Part8_RagConseptandAgent.graph.state import GraphState
from typing import Dict,Any

def retrieve(state: GraphState) -> Dict[str,Any]:

    print("-----RETRIEVE-----")
    question = state["question"]
    documents = retriever.invoke(question)

    return {"question": question, "documents": documents}