import sys
input = sys.stdin.input().rstrip('\n')
from collections import Counter, defaultdict, deque
import heapq

a = list(map(int, input().split()))
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
freq = Counter(a)
q = deque()

pq = []
heapq.heappush(pq, 1)
x = heapq.heappop(pq)
