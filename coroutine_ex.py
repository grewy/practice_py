
def coroutine():
  data = yield
  while True:
    print("I am doing stuff with data now")
    data = data * 2
    data = yield data


co = coroutine()
co.next()
print co.send(10)
