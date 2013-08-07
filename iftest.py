#!/usr/bin/python
def test(number, num=2, message="shit"):
	print "test function"
	print message*num
	guess = (raw_input("please entern a number"))
	print guess.isdigit()
	if guess.isdigit()==False:
		exit()
	guess = int (guess)
	con = True
	i=0
	while con  and i<num:
		if number==guess:
			print "congratulation"
		elif number<guess:
			print "bigger"
		else:
			print "smaller"
		guess = raw_input("enter a number")
		if guess=='quit':
			break
		guess= int(guess)
		i=i+1
	print "done"
print "begin to call test fun"
test(3)
test(22,3,"wo")
