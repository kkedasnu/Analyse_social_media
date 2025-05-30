import sys

def deikstr(graph, first_versh):
    n = len(graph)  # Количество вершин в графе
    short_path = [sys.maxsize] * n  # Инициализация расстояний в массиве с бесконечностью
    short_path[first_versh] = 0  # Расстояние до начальной вершины равно 0
    visited = [False] * n  # Массив для отслеживания уже обойденных вершин

    for i in range(n):
        # Находим вершину с минимальным расстоянием
        min_dist = sys.maxsize
        min_index = -1 # Пока нет ни одной вершины в текущей итерации

        for versh in range(n):
            if not visited[versh] and short_path[versh] < min_dist:
                min_dist = short_path[versh]
                min_index = versh
        # Помечаем найденную вершину как посещенную
        visited[min_index] = True

        # Обновляем расстояния до соседних вершин
        for neighbour in range(n):
            if graph[min_index][neighbour] > 0 and not visited[neighbour]:
                        # Если есть ребро
                new_path = short_path[min_index] + graph[min_index][neighbour]
                if new_path < short_path[neighbour]:
                    short_path[neighbour] = new_path

        return short_path

   # Пример графа
graph = [
[0, 8, 11, 7, 8, 13],
[8, 0, 10, 15, 0, 0],
[11, 10, 0, 11, 0, 2],
[0, 15, 11, 0, 6, 0],
[0, 0, 0, 6, 0, 9],
[13, 0, 2, 0, 9, 0]
]

# Указываем вершину
first_versh = 4
short_path = deikstr(graph, first_versh)

# Вывод резудьтата на экран
print(f"Кратчайшие расстояния от вершины {first_versh }:")
for versh, distance in enumerate(short_path):
    if distance == sys.maxsize:
        print(f"с вершиной {versh} нет связей")
    else:
        print(f"До вершины {versh} расстояние: {distance}")

