class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.isEmpty():
      return self.items.pop()

  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)


class Queue:
  def __init__(self):
    self.s1 = Stack()
    self.s2 = Stack()

  def enque(self, data):
    self.s1.push(data)


  def deque(self):
    if not self.s2.isEmpty():
      return self.s2.pop()
    else:
      if self.s1.isEmpty():
        return "Empty Queue"
      else:
        while not self.s1.isEmpty():
          self.s2.push(self.s1.pop())
        return self.s2.pop()


#driver
q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)
print q.deque()
print q.deque()
print q.deque()