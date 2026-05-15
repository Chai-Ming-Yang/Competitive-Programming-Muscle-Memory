def reverse(head):
  pre, cur = None, head
  while cur:
    nxt = cur.next
    cur.next = pre
    pre = cur
    cur = nxt
  return pre

def findMid(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow

def hasCycle(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: return True
  return False

def merge(l1, l2):
  dummy = cur = Node()
  while l1 and l2:
    if l1.val < l2.val:
      cur.next = l1
      l1 = l1.next
    else:
      cur.next = l2
      l2 = l2.next
    cur = cur.next
  cur.next = l1 or l2
  return dummy.next

def cycleStart(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: break
  else:
    return None
  trail = head
  while slow != trail:
    trail = trail.next
    slow = slow.next
  return slow
