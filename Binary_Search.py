def bs(lo, hi):
  while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid
    else: lo = mid + 1
  return lo

def bs(lo, hi):
  while lo < hi:
    mid = (lo + hi + 1) // 2
    if ok(mid): lo = mid
    else: hi = mid - 1
  return hi
# (lo = mid) : +1

import bisect
idx = bisect.bisect_left(a, x)
idx = bisect.bisect_right(a, x)  # 2nd bs(lo, hi) + 1
