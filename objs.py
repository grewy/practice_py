
# !/usr/bin/env python



class Descriptor:

  def __init__(self):
    print ("constructor")

  def __delete__(self, instance):
    print ("destructor")
    del obj

class TestClass(object):
  name = Descriptor()

if __name__ == "__main__":
  obj = TestClass()
  del obj.name
