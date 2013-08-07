#!/usr/bin/python
import pickle as p
shoplistfile = "shoplist.data"
shoplist = ['apple','mango','carrot']
f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
print shoplist
del shoplist
print 'after del the shoplist'

f = file(shoplistfile)
storedlist = p.load(f)
print "after load from file"
print storedlist
#print shoplist

