def breadth_first_search(graph, start, search_request):
    vertexes_to_check = [[start]]
    checked_vertexes = set()
    while len(vertexes_to_check) >= 1:
        path = vertexes_to_check.pop(0)
        vertex = path[-1]
        if vertex not in checked_vertexes:
            checked_vertexes.add(vertex)
            if vertex == search_request:
                return path, checked_vertexes
            for adjacent_vertex in graph.get(vertex):
                if adjacent_vertex not in checked_vertexes:
                    new_path = list(path)
                    new_path.append(adjacent_vertex)
                    vertexes_to_check.append(new_path)
    return False, checked_vertexes


graph = {
    '0': {'1'},
    '1': {'0', '2', '3', '4'},
    '2': {'1', '5', '6'},
    '3': {'1', '7'},
    '4': {'1', '8', '9'},
    '5': {'2'},
    '6': {'2', '10'},
    '7': {'3', '10'},
    '8': {'4', '11'},
    '9': {'4'},
    '10': {'6', '7'},
    '11': {'8'}
}
start_vertex = '1'
search_request = '7'
result, checked_vertexes = breadth_first_search(graph, start_vertex,
                                                search_request)
if not result:
    print(f'Искомой вершины нет в графе. Проверенные вершины:'
          f' {checked_vertexes}')
else:
    print(f'Путь от стартовой до искомой вершины:'
          f' {result}. Проверенные вершины: {checked_vertexes}')