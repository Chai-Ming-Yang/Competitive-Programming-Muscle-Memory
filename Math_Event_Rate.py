# x, y : period
LCM = math.lcm(x, y)  # scale to int

def num_events(t):
  return t//x + t//y - t//LCM    # every lcm, overlap occurs

len_cycle = num_events(lcm)  # until collision

cycle = []
t = 1
while len(cycle) < len_cycle:
  if t % tick_x == 0 and t % tick_y == 0:
    cycle.append('both')
  elif t % tick_x == 0:
    cycle.append('x')
  elif t % tick_y == 0:
    cycle.append('y')
  t += 1

ans = cycle[(k - 1) % cycle_len]
