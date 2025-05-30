#Использование алгоритма Дейкстры

def deikstry(graph, start):
    # Инициализация
    R = {start}  # Результирующие вершины
    Q = set()    # Кандидаты
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    prev = {node: None for node in graph}  # Для восстановления пути

    # Шаг 1: Добавить смежные с n0 в Q
    for neighbor, weight in graph[start]:
        Q.add(neighbor)
        distances[neighbor] = weight
        prev[neighbor] = start

    while Q:
        # Шаг 2: Выбрать из Q ближайшую к R
        u = min(Q, key=lambda node: distances[node])
        Q.remove(u)
        R.add(u)  # Добавить в R

        # Шаг 3: Просмотреть смежные с u
        for v, weight in graph[u]:
            if v in R:
                continue  # Вершина уже обработана
            if v not in Q:
                Q.add(v)
            # Обновить расстояние, если путь через u короче
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                prev[v] = u

    return distances, prev

# Пример использования

    # Граф в виде словаря: {вершина: [(сосед, вес), ...]}
graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 5), ('D', 10)],
        'C': [('A', 2), ('B', 5), ('D', 3)],
        'D': [('B', 10), ('C', 3)]
        }

start_node = 'D'
distances, prev = deikstry(graph, start_node)

print(f"Кратчайшие расстояния от вершины {start_node}:")
for node, dist in distances.items():
        print(f"  До {node}: {dist}")
        path = []
        current = node
        while current:
            path.append(current)
            current = prev[current]
        path.reverse()
        print(f"    Путь: {' -> '.join(path)}")