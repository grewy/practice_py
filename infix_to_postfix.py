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

precedence = {'+':1, '-':1, '*':2, '/':3, '^':4}

def notGreater(i,top):
  # precendance check of i with top of stack
  try:
    a = precedence[i]
    b = precedence[top]
    return (a <= b)
  except KeyError:
    return False

def infix_to_postfix(exp):
  out = []
  st = Stack()
  for i in exp:
    #char is operand
    if i.isalpha():
      out.append(i)
    #char is (
    elif i == '(':
      st.push(i)
    elif i == ')':
      while not st.isEmpty() and st.peek() != '(':
        out.append(st.pop())
      if (st.isEmpty() or st.peek() != '('):
        return -1
      else:
        st.pop()
    # i is operator
    else:
      while not st.isEmpty() and notGreater(i, st.peek()):
        out.append(st.pop())
       # print st.items, out
      st.push(i)
      #print st.items, out

  while not st.isEmpty():
    out.append(st.pop())
    #print st.items, out

  print ''.join(out)


#driver
exp = "a+b*(c^d-e)^(f+g*h)-i"
infix_to_postfix(exp)

