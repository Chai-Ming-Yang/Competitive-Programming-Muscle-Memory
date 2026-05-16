import sys
sys.setrecursionlimit(10**7)

def tarjan(n, adj):
  ids = [-1] * n
  low = [0] * n
  on = [False] * n
  st = []
  comp = [-1] * n

  idc = cid = 0

  def dfs(u):
    nonlocal idc, cid
    ids[u] = low[u] = idc
    idc += 1
    st.append(u)
    on[u] = True

    for v in adj[u]:
      if ids[v] == -1:
        dfs(v)
        low[u] = min(low[u], low[v])
      elif on[v]:
        low[u] = min(low[u], ids[v])

    if ids[u] != low[u]: return
    while True:
      v = st.pop()
      on[v] = False
      comp[v] = cid
      if v == u:
        break
    cid += 1

  for i in range(n):
    if ids[i] == -1:
      dfs(i)
    
  return comp, cid
