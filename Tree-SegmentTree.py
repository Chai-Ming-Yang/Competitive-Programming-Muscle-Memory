class SegmentTree:
  def __init__(self, data, func=lambda x, y: x + y, default=0):
    self.n = len(data)
    self.func = func
    self.default = default
    self.tree = [default] * (2 * self.n)

    for i in range(self.n):
      self.tree[self.n + i] = data[i]
    for i in range(self.n - 1, 0, -1):
      self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

  def update(self, i, value):
    i += self.n
    self.tree[i] = value
    while i > 1:
      i //= 2
      self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

  def query(self, l, r):
    res = self.default
    l += self.n;  r += self.n
    while l < r:
      if l % 2 == 1:
        res = self.func(res, self.tree[l])
        l += 1
      if r % 2 == 1:
        r -= 1
        res = self.func(res, self.tree[r])
      l //= 2;  r //= 2
    return res
