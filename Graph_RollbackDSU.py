class RollbackDSU:
  def __init__(self, n):
    self.par = list(range(n))
    self.sz = [1] * n
    self.hist = []
    self.comp = n
  
  def find(self, a):
    while a != self.par[a]:
      a = self.par[a]
    return a

  def union(self, a, b):
    a, b = self.find(a), self.find(b)
    if a == b: return False
    if self.sz[a] < self.sz[b]:
      a, b = b, a
    self.hist.append((b, self.par[b], a, self.sz[a]))
    
    self.par[b] = a
    self.sz[a] += self.sz[b]
    self.comp -= 1
    return True

  def snapshot(self):
    return len(self.hist)

  def rollback(self, snap):
    while len(self.hist) > snap:
      b, pb, a, sa = self.hist.pop()

      self.par[b] = pb
      self.sz[a] = sa
      self.comp += 1

dsu = RollbackDSU(n)
