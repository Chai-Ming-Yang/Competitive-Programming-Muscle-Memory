path = []
def dfs(u):
  if u in adj:
    while adj[u]:
      dfs(adj[u].pop())
    path.append(u)
