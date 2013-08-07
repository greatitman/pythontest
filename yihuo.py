#!/usr/bin/python
mystr="123456789"
strlen=len(mystr)
print "mystr=%s len is %d"%(mystr,strlen)
imax = strlen
for i in range(0, imax/2):
	tmp = mystr[i]
#	mystr[i] = i #	mystr[imax-i-1]
#mystr[imax-i-1]=tmp
print "after reverse the string is %s" %mystr 

