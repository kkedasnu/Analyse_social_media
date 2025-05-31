import networkx as nx

G = nx.Graph()
G.add_nodes_from(range(21))

# Спад (0 → 5) — делаем "яму"
for i in range(5):
    G.add_edge(i, i+1)  # 0-1, 1-2, ..., 4-5
# Ослабляем центральность узла 5, уменьшая его связи
G.remove_edge(4, 5)
G.add_edge(5, 6)

# Подъём (6 → 10) — усиливаем центральность
for i in range(6, 10):
    G.add_edge(i, i+1)  # 6-7, 7-8, 8-9, 9-10
# Делаем узел 10 самым центральным
G.add_edge(10, 8)  # Дополнительная связь
G.add_edge(10, 9)
G.add_edge(10, 11)  # Переход к спаду

# 3. Второй спад (11 → 20) — падение
for i in range(11, 20):
    G.add_edge(i, i+1)  # 11-12, ..., 19-20

# Вычисляем центральность
centrality = nx.eigenvector_centrality(G, max_iter=1000)
sorted_values = [centrality[i] for i in range(21)]

# Выводим значения на экран
print("Централизация узлов:", sorted_values)
