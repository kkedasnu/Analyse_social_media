import networkx as nx

# Личные параметры Толстых М.С.
n = 25  # Количество узлов
p = 0.35  # Вероятность создания ребра

# Создание графа
G = nx.erdos_renyi_graph(n, p)

# Вычисление средней степени узла в графе
a = 0
for n in G.nodes():
    a += G.degree(n)
average_degree_graph = float(a) / len(G.nodes())

# Вычисление средней степени узла по формуле
formula_average_degree = (n - 1) * p

# Вывод характеристик графа
print (G)
nx.draw(G)

# Вывод результатов и сравнение
# print(f"Средняя степень узла в графе: {average_degree_graph:.2f}")
# print(f"Средняя степень узла по формуле: {formula_average_degree:.2f}")
#rint(f"Математическая разница: {average_degree_graph - formula_average_degree}")


