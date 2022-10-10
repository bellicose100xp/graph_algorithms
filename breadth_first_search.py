from collections import deque

def breadth_first_print(graph: dict[str, list[str]], source: str) -> None:
    queue: deque[str] = deque(source)

    while queue:
        curr: str = queue.pop()
        print(curr)

        for neighbor in graph[curr]:
            queue.appendleft(neighbor)


graph: dict[str, list[str]] = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


breadth_first_print(graph, 'a')