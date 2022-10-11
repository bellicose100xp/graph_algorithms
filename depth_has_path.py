graph: dict[str, list[str]] = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i<'],
    'k': []
}

def hasPath(graph: dict[str, list[str]], src: str, dst: str) -> bool:
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        result = hasPath(graph, neighbor, dst)

        if (result == True):
            return True
        
    return False


hasPath(graph, 'f', 'k') #? true
hasPath(graph, 'f', 'j') #? false
