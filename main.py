#coding=utf-8
from mylib import Hello
from mylib import Hi
print ("你好")
for i in range(0,1):
    print ("item {0},{1}".format(i,"hello python"))


h = Hello("world")
h.sayHello()
h1 = Hi("python")
h1.sayHi()

def max(a,b):
    if(a>b):
        return a
    else:
        return b

print("max {0} and {1} is {2}".format(2,3,max(2,3)))
