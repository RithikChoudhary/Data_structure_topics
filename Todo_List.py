# Output List, The Main List that we are performing our ops
outputList = []

# The STACK which keeps the history of commands priviously used
undoTask = []

# The STACK which keeps the history of commands priviously undone
redoTask = []

def add(arg):
	# add function to literally add elements to the outputList
	global outputList, undoTask
	undoTask.append(('append', arg, len(outputList)))
	outputList.append(arg)

def remove(arg):
	# remove function to literally remove elements to the outputList
	global outputList, undoTask
	undoTask.append(('remove', arg, outputList.index(arg)))
	outputList.remove(arg)

def undo():
	# remove function to literally remove elements to the outputList
	global outputList, undoTask, redoTask
	task, val, index = undoTask.pop()
	if task == 'remove':
		outputList.insert(index, val)
		redoTask.append( ('append', val, index) )

	elif task == 'append':
		outputList.pop(index)
		redoTask.append( ('remove', val, index) )

def redo():
	global outputList, undoTask, redoTask
	task, val, index = redoTask.pop()

	if task == 'remove':
		outputList.insert(index, val)

	elif task == 'append':
		outputList.pop(index)
	
	undoTask.append( (task, val, index) )

if __name__ == '__main__':
	add(1)
	print("add(1) -> " ,outputList)
	# print(outputList)
	add(2)
	print("add(2) -> ",outputList)
	# print(outputList)
	add(3)
	print("add(3) -> ",outputList)
	# print(outputList
	add(4)
	print("add(4) -> ",outputList)
	# print(outputList)
	undo()
	print("undo() -> ",outputList)
	# print(outputList)
	undo()
	print("undo() -> ",outputList )
	# print(outputList)
	redo()
	print("redo() -> ",outputList)
	# print(outputList)
	redo()
	print("redo() -> ",outputList)
	# print(outputList)
	remove(3)
	print("remove(3) -> ",outputList)
	# print(outputList)
	remove(1)
	print("remove(1) -> ",outputList)
	# print(outputList)
	remove(2)
	print("remove(2) -> ",outputList)
	# print(outputList)
	undo()
	print("undo() -> ",outputList)
	# print(outputList)
	undo()
	print("undo() -> ",outputList)
	# print(outputList)
	undo()
	print("undo() -> ",outputList)
	# print(outputList)
	redo()
	print("redo() -> ",outputList)
	# print(outputList)
	
