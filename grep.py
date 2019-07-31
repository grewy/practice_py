

class Grep(object):

  def grep(self, pattern, file):
    with open(file) as fp:
      i = 1
      for line in fp:
        if pattern in line:
          print i, ":", line
        i += 1



obj = Grep()
obj.grep("def ", "lru.py")