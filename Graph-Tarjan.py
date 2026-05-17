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
    on[u] = True
    st.append(u)

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
      if u == v:  break
    cid += 1

  for i in range(n):
    if ids[i] == -1:
      dfs(i)
  return comp, cid

comp, cid = tarjan(n, adj)
dag_adj = [set() for _ in range(cid)]
for u in adj:
  for v in adj[u]:
    cu, cv = compu[u], comp[v]
    if cu != cv:
      dag_adj[cu].add(cv)
dag_adj = list(map(list, dag_adj))
