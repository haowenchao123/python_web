def MyIterator():
	for i, data in enumerate([1, 3, 9]):
		print("I am in the idx:{0} call of next()".format(i))
		yield data

for i in MyIterator():
	print(i)