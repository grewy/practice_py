
class VM(object):
  def __init__(self):
    print "in Vm init"

  def vmfoo(self):
    print self.name



class Drive(VM):
  def __init__(self):
    self.name = "mk"

# test
a=Drive()
a.vmfoo()
