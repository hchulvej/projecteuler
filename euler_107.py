from unionfind import unionfind

# Initializing the list of edges with their weights

edges = set()

with open("euler_107_small.txt", "r") as f:
    lines = f.readlines()
    for row, line in enumerate(lines):
        weights = [n.strip() for n in line.split(",")]
        for col, weight in enumerate(weights):
            if weight != "-" and row != col:
                edges.add((min(row,col), max(row,col),int(weight)))

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

print(edges)
print(sum([edge[2] for edge in edges]))

        
               
    