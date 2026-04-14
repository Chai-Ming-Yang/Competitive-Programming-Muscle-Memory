def dijkstra(src, n):
  dist = [float('inf')] * n
  dist[src] = 0
  pq = [(0, src)]

  while pq:
    d, u = heapq.heappop(pq)
    if dist[u] < d: continue
    for v, wt in adj[u]:
      if dist[v] < d + wt: continue
      dist[v] = d + wt
      heapq.heappush(pq, (dist[v], v))
  return dist
