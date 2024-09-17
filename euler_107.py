from unionfind import unionfind

# Initializing the list of edges with their weights

edges = set()

with open("euler_107.txt", "r") as f:
    lines = f.readlines()
    matrix = [list(line.replace("\n", "").split(",")) for line in lines]
    for row, line in enumerate(matrix):
        for col, weight in enumerate(line):
            if weight != "-" and row != col:
                edges.add((min(row, col), max(row, col), int(weight)))

edges = list(edges)
edges = sorted(edges, key=lambda x: x[2])

# Setting up Union-Find structure

uf = unionfind(40)


# Seetting up Kruskal's algorithm

def kruskal(edges, uf):
    
    mst = []
    mst_weight = 0
    
    for edge in edges:
        if not uf.issame(edge[0], edge[1]):
            uf.unite(edge[0], edge[1])
            mst.append(edge)
            mst_weight += edge[2]
        
        if len(mst) == 39:
            break
    
    return mst_weight

print(sum([edge[2] for edge in edges])-kruskal(edges, uf))


        
               
    