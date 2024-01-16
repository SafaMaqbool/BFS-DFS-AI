
graph={
  '0' : ['1','2'],
  '1' : ['3','4'],
  '2' : ['5'],
  '3' : [],
  '4' : ['5'],
  '5' : []        
}

def dfs(visited, graph, node):
    visited.append(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(visited, graph, neighbour)

print("Depth First Search")
visited = []
dfs(visited, graph, '0')
