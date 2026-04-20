def toposort(n, adj):
  indeg = [0] * n
  for u in range(n):
    for v in adj[u]:
      indeg[v] += 1
  
  q = deque([i for i in range(n) if indeg[i] == 0])
  order = []
  while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
      indeg[v] -= 1
      if indeg[v] == 0:
        q.append(v)
  
  if len(order) == n:
    return order
  return []
