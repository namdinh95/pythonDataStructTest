""" Facebook Interview Question: 
	Given a stack of integers, reverse the values at the odd indexes. 
	For example, [0, 1, 2, 3, 4, 5, 6, 7, 8] becomes [0, 7, 2, 5, 4, 3, 6, 1, 8]. 
	There are no guarantees as to the contents of the stack, 
	and you may only use ONE stack as auxiliary storage."""

# Input stack from command line
theStack = input('Input stack plz: ')
# input() only do string. Make it a list
theStack = [int(x) for x in theStack.split()]

# 3 or less elements stay the same
if len(theStack) < 4:
	print(theStack)
	quit()

# dummy
dummy = False
# If size is even, push a dummy node
if len(theStack)%2 == 0:
	dummy = True
	theStack.append(0);

# Size of stack
stackSize = len(theStack)

""" Take the first head odd-indexed element out when transfering to another stack, 
	keep it in a variable. Then put it at the end. 
	Then do the same at the end of the stack.
	Repeat to reverse the odd indexes."""

# Head counter
headCounter = stackSize-1

# Tail counter
tailCounter = 3

# Empty stack for operations
tempStack = []

# Temporary variable to hold odd-indexed element
odd = 0

# Start operation.
for i in range(stackSize//4):
	# Do head operation. First iteration
	a,b,c,d = 0,0,0,0
	while theStack:
		a += 1
		temp = theStack.pop()
		if a == headCounter:
			odd = temp
		else: 
			tempStack.append(temp)
	# Second iteration aka return back to original stack
	while tempStack:
		b += 1
		if b == headCounter:
			theStack.append(odd)
		else:
			temp = tempStack.pop()
			theStack.append(temp)
	# Increment the head counter
	headCounter -= 2

	# Do tail operation
	while theStack:
		c += 1
		temp = theStack.pop()
		if c == tailCounter:
			odd = temp
		else:
			tempStack.append(temp)
	while tempStack:
		d += 1
		# modified cuz first odd pushed
		if d == tailCounter-1:
			theStack.append(odd)
		else:
			temp = tempStack.pop()
			theStack.append(temp)
	# Increment the tail counter
	tailCounter += 2
# end operation

if dummy:
	theStack.pop()

# print modifed stack
print(theStack)

