def dijkstras(src, n):
  dist = [float('inf')] * n
  dist[src] = 0
  pq = [(0, src)]

  while pq:
    d, u = heapq.heappop()
    if d > dist[u]: continue
    for v, wt in adj[u]:
      if dist[u] + wt < dist[v]:
        dist[v] = dist[u] + wt
        heapq.heappush(pq, (dist[v], v))
  return dist
