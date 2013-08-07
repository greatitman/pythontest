#!/usr/bin/python
def make_rep(n):
	return lambda s:s*n
twice = make_rep(2)
three = lambda a:a*3
print twice("world")
print twice(5)
print three('hello')

