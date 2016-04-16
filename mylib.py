class Hello:
    def __init__(self,name):
        self._name = name
    def sayHello(self):
        print ("heollo {0}".format(self._name))

class Hi(Hello):
    def __init__(self, name):
        Hello.__init__(self,name)
    def sayHi(self):
        print("hi {0}".format(self._name))