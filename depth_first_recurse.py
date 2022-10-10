def depth_first_print(graph: dict[str, list[str]], source: str) -> None:
    print(source)

    if graph[source]:
        for neighbor in graph[source]:
            depth_first_print(graph, neighbor)

    return None

graph: dict[str, list[str]] = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_print(graph, 'a')