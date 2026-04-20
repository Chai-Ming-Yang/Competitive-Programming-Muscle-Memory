def bellman_ford(n, src, edges):
  dist = [float('inf')] * n
  dist[src] = 0

  for _ in range(n-1):
    updated = False
    for u, v, w in edges:
      if w + dist[u] < dist[v]:
        dist[v] = w + dist[u]
        updated = True
    if not updated:
      break

  for u, v, w in edges:
    if w + dist[u] < dist[v]:
      dist[v] = float('inf')
      return dist, True

  return dist, False
