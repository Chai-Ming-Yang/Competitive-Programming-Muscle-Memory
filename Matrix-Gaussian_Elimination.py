DIM = int(input())
matrx = [list(map(int, input().split()))]

# Forward Elimination
for PIVOT in range(DIM):
  tmp_pivot = PIVOT
  for r in range(PIVOT+1, DIM):
    if abs(matrix[r][PIVOT]) > abs(matrix[tmp_pivot][PIVOT]):
      tmp_pivot = r
  matrix[PIVOT], matrix[tmp_pivot] = matrix[tmp_pivot], matrix[PIVOT]

  for r in range(PIVOT + 1, DIM):
    factor = matrix[r][PIVOT] / matrix[PIVOT][PIVOT]
    for c in range(PIVOT, DIM + 1):
      matrix[r][c] -= factor * matrix[PIVOT][c]

# Backward Propagation
ans = [0] * DIM
for PIVOT in range(DIM-1, -1, -1):
  total = 0
  for c in range(PIVOT+1, DIM):
    total += matrix[PIVOT][c] * ans[c]
  ans[PIVOT] = (matrix[PIVOT][DIM] - total) / matrix[PIVOT][PIVOT]
