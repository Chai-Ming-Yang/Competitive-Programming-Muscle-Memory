from collections import deque

class Dinic:
  class Edge:
    def __init__(self, to, rev, cap):
      self.to = to
      self.rev = rev
      self.cap = cap

  def __init__(self, n):
    self.n = n
    self.g = [[] for _ in range(n)]

  def add_edge(self, u, v, cap):
    fwd = self.Edge(v, len(self.g[v]), cap)
    rev = self.Edge(u, len(self.g[u]), 0)
    self.g[u].append(fwd)
    self.g[v].append(rev)

  def bfs(self, s, t):
    self.level = [-1] * self.n
    self.level[s] = 0

    q = deque([s])
    while q:
      u = q.popleft()

      for e in self.g[u]:
        if e.cap > 0 and self.level[e.to] == -1:
          self.level[e.to] = self.level[u] + 1
          q.append(e.to)
    return self.level[t] != -1

  def dfs(self, u, t, f):
    if u == t:    return f

    for i in range(self.ptr[u], len(self.g[u])):
      self.ptr[u] = i
      e = self.g[u][i]

      if e.cap > 0 and self.level[e.to] == self.level[u] + 1:
        pushed = self.dfs(e.to, t, min(f, e.cap))
        if pushed:
          e.cap -= pushed
          self.g[e.to][e.rev].cap += pushed
          return pushed
    return 0

  def maxflow(self, s, t):
      flow = 0
      INF = 10**18

      while self.bfs(s, t):
          self.ptr = [0] * self.n
          while True:
              pushed = self.dfs(s, t, INF)
              if pushed == 0:
                  break
              flow += pushed
      return flow
