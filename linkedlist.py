
class Node():

  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class LinkedList(object):

  def __init__(self, head):
    self.head = head

  def size(self):

    if not self.head:
      return 0

    count = 0
    _tmp = self.head

    while _tmp:
      count += 1
      _tmp = _tmp.next

    return count

  def empty(self):
    if self.size() == 0:
      return True
    else:
      return False

  def value_at(self, idx):
    if self.size() < idx or idx < 0 :
      return "Invalid Index"

    _tmp = self.head
    while idx >= 0:
      _tmp = _tmp.next
      idx -= 1

    return _tmp.data

  def push_front(self, value):

    _node = Node(data=value)

    _node.next = self.head
    self.head = _node

  def pop_front(self):
    _tmp = self.head
    self.head = self.head.next
    val = _tmp.data
    del(_tmp)
    return val

  def push_back(self, value):
    _tmp = self.head
    while _tmp.next:
      _tmp = _tmp.next
    _tmp.next = Node(data=value)

  def pop_back(self):
    _tmp = self.head
    while _tmp.next.next:
      _tmp = _tmp.next
    val = _tmp.next.data
    del(_tmp.next)
    return val

#front() - get value of front item
  def front(self):
    return self.head.data

#back() - get value of end item
  def back(self):
    _tmp = self.head
    while _tmp.next:
      _tmp = _tmp.next
    return _tmp.data

#insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
  def insert(self, idx, value):
    if idx > self.size():
      return "Invalid Index"
    _tmp = self.head
    while idx > 1:
      _tmp = _tmp.next
      idx -= 1
    _node = Node(data=value)
    _node.next = _tmp.next
    _tmp.next = _node

#erase(index) - removes node at given index
  def erase(self, idx):
    if idx > self.size():
      return "Invalid Index"
    _tmp = self.head
    while idx > 1:
      _tmp = _tmp.next
      idx -= 1
    _node = _tmp.next
    _tmp.next = _tmp.next.next
    del(_node)

#value_n_from_end(n) - returns the value of the node at nth position from the end of the list
  def value_n_from_end(self, n):
    ln = self.size()
    steps = ln - n
    _tmp = self.head
    while steps > 0:
      _tmp = _tmp.next
      steps -= 1
    return _tmp.data

#reverse() - reverses the list
  def reverse(self):
    _tmp = self.head
    _prev = None
    _current = _tmp
    while _tmp.next:
      _tmp = _tmp.next
      _current.next = _prev
      _prev = _current
      _current = _tmp
    self.head = _current

#remove_value(value) - removes the first item in the list with this value
  def remove_value(self, value):
    _tmp = self.head
    if _tmp and _tmp.data == value:
      self.head = self.head.next
      del(_tmp)
    while _tmp.next:
      if _tmp.next.data == value:
        _x = _tmp.next
        _tmp.next = _tmp.next.next
        del(_x)
        break

#Is loop
  def loop(self):
    _slow = _fast = self.head

    while _slow and _fast and _fast.next:
      _slow = _slow.next
      _fast = _fast.next.next

      if _slow == _fast:
        return True, _slow

    return False, None

#remove loop
  def remove_loop(self):
    _, loop_node = self.loop()
    if not _:
      return "There is no loop in linked list"

    _p2 = loop_node
    _p1 = self.head
    # _p1-head & _p2-where pointers met. Both incrementing at same pace meets
    # at start point of the linked list
    while _p2.next != _p1.next:
      _p1 = _p1.next
      _p2 = _p2.next

    _st = _p1.next
    _p1 = _st

    while _p1.next != _st:
      _p1 = _p1.next
    _p1.next = None


def main():

  l = LinkedList(Node(data=1))
  l.head.next = Node(data=2)
  l.head.next.next = Node(data=3)
  l.head.next.next.next = Node(data=4)
  l.head.next.next.next.next = Node(data=5)

  #print LL
  print l.head.data, l.head.next.data, l.head.next.next.data, l.head.next.next.next.data, l.head.next.next.next.next.data

  print "size: ", l.size()
  print "Empty: ", l.empty()
  print "value at 3 : %s" % l.value_at(3)
  print "value at 30 : %s" % l.value_at(30)
  print "value at -3 : %s" % l.value_at(-3)

main()

def has_cycle(head):
  fast = slow = head
  while fast and fast.next and fast.next.next:
    slow , fast = slow.next , fast.next.next
    if slow is fast: # There is a cycle.
      # Tries to find the start of the cycle.
      slow = head
      # Both pointers advance at the same time.
      while slow is not fast:
        slow , fast = slow.next , fast.next
      return slow # slow is the start of cycle.
  return None # No cycle.


