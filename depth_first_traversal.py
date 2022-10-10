def depth_first_print(graph: dict[str, list[str]], source: str) -> None:
    stack: list[str] = [source]

    while stack:
        curr = stack.pop()
        print(curr)

        for neighbor in graph[curr]:
            stack.append(neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_print(graph, 'a')