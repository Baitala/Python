# список вершин + список ребер
V = {'A', 'B', 'C', 'D'}
E = {('A', 'B'), ('B', 'C'), ('C', 'D')}

#O(N) на перебір сусідів конкретної вершини

# матриця суміжності

V = ['A' , 'B', 'C', 'D']
index = {V[i]:i for i in range(len(V))}
A = [[0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]]

# список суміжності

'''A: B
    B: A, C
    C: B, D
    D: C'''

G = {'A': {'B'}
    'B': {'A', 'C'}
    'C': {'B', 'D'}
    'D': {'C'}}

# перебір сусідів 
for neighbour in G[V]:
    print(neighbour)

""" NM
    AB
    BC
    BD"""

M, N = [int(*)for * in input().split()]
V = []
index = {}
A = [[0]*N for i in range(N)]
for in in range(N):
    v1, v2 = input().split()
    for v in v1, v2:
        if v not in index:
            V.append(v)
            index[v] = len(V)-1
    v1_i = index[v1]
    v2_i = index[v2]
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1

# зчитування для списків суміжності
M, N = [int(*)for * in input().split()]
G = {}
for i in range(N):
    v1,v2 = input().split()
    for v,u in (v1,v2), (v2,v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)

#Компактне зберігання списків суміжності для незмінного графа

0: 1
1: 0, 2, 3
2: 1, 3
3: 1, 2, 4
4: 3

edges = [1, 0, 2, 3, 1, 3, 1, 2, 4, 3]
#offset[i] - початок списку суміжності і-ї вершини
offset = [0, 1, 4, 6, 9, 10] #10 фіктивний офсет для наступної вершини
edges[offset[i]:offset[i+1]]
