#!/usr/bin/python
class ShortInputExpt(Exception):
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	s = raw_input("Enter sth:")
	if len(s)<3:
		raise ShortInputExpt(len(s),3)
except EOFError:
		print 'Why did you do an EOF on me?'
except ShortInputExpt,x:
		print 'ShortInputException: The input was of length %d\
	was exception at least %d' %(x.length,x.atleast)
else:
	print 'No exception'
