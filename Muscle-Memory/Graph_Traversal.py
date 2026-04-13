vis = set()
def dfs(u):
  vis.add(u):
  for v in adj[u]:
    if v not in vis: continue
    dfs(v)

def bfs(src):
  q = deque([src])
  dist = {src:0}
  while q:
    u = q.popleft()
    for v in adj[u]:
      if v in dist: continue
      q.append(v)
      dist[v] = dist[u] + 1
  return dist
