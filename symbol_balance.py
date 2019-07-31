class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)

def isBalance(s):
  st = Stack()
  op_symbol = ['(','{','[']
  cl_symbol = [')', '}', ']']

  for i in s:
    if i in op_symbol + cl_symbol:
      if i in op_symbol:
        st.push(i)
      else:
        if st.isEmpty():
          return False
        else:
          x = st.pop()
          if x != op_symbol[cl_symbol.index(i)]:
            return False
  # if balanced, stack should be empty
  if not st.isEmpty():
    return False
  else:
    return True



# driver
print isBalance("(A+b)+(c+d)")
print isBalance("((a+b)+[c-d]}")