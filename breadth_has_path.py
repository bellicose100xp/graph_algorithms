# breadth first - has_path

from collections import deque

graph: dict[str, list[str]] = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path(graph: dict[str, list[str]], src: str, dst: str) -> bool:

    queue: deque[str] = deque(src)

    while queue:
        node = queue.pop()
        
        if node == dst:
            return True
        
        for next_node in graph[node]:
            queue.appendleft(next_node)

    return False


has_path(graph, 'f', 'k')  # ? will be true
has_path(graph, 'f', 'j')  # ? will be false
