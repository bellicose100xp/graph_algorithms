def breadth_first_print(graph: dict[str, list[str]], neighbor_list: str | list[str]) -> None:

    if not neighbor_list:
        return None

    # on first function call the value is string, on subsequent function calls, the value is arr
    neighbor_list_arr: list[str] = [neighbor_list] if isinstance(neighbor_list, str) else neighbor_list

    new_neighbor_list: list[str] = []

    for neighbor in neighbor_list_arr:
        print(neighbor)
        if graph[neighbor]:
            for next_neighbor in graph[neighbor]:
                new_neighbor_list.append(next_neighbor)

    breadth_first_print(graph, new_neighbor_list)


graph: dict[str, list[str]] = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

breadth_first_print(graph, 'a')
