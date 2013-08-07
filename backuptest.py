#!/usr/bin/python
import time
import os
source = ['/home/mnt/c/pythontest','/home/mnt/c/ctests']
target_dir = '/home/mnt/c/backup/'
today = target_dir + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")
if not os.path.exists(today):
#	os.mkdirs(today)
	os.makedirs(today)
	print "Successfully created dir", today
comment = raw_input("Enter comment:")
if len(comment)==0:
	target = today+os.sep+now+'.tar.gz'
else:
	target = today+os.sep+now +'_'+ comment.replace(' ', '_')+'.tar.gz'
print target
zip_command = "tar -cvzf %s %s -X /home/mnt/c/pythontest/backuptest.py"%(target, ' '.join(source))
if os.system(zip_command)==0:
	print "success bakcup to ", target
else:
	print "backup failed"
