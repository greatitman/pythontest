#!/usr/bin/python
class Person:
	def sayHi(self):
		print "hello ,hi"
	def __init__(self,name='tom'):
		self.name = name;
p = Person()
p.sayHi()

print p.name
