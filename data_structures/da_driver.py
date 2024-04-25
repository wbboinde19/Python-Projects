import sys
import os.path
import dynamic_array as da

def populate(inputFileName):
	inFile=open(inputFileName,"r")
	inFilelines=inFile.readlines()
	inFile.close()
	myArray=da.DynamicArray()
	index=0
	for x in inFilelines:
		try:
			intX = int(x.strip())
		except ValueError:
			print("hey your",x,"is not an integer")
		myArray.insertEfficient(index,intX)
		index+=1
	return myArray

def displayUnique(myArray):
	uniqueArray=[]
	count=0
	for i in range(len(myArray)):
		if myArray.__getitem__(i) not in uniqueArray:
			uniqueArray.append(myArray.__getitem__(i))
		count+=1
	for j in range(len(uniqueArray)):
		print(uniqueArray[j])

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description='Lab 5 - arrays')
	parser.add_argument('-i','--inputFileName', type=str, help='File of integers, one per line', required=True)
	args = parser.parse_args()

	if not (os.path.isfile(args.inputFileName)):
		print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
		exit(-1)

	myArray = da.DynamicArray()
	myArray=populate(args.inputFileName)

	#infile = open(args.inputFileName, "r")
	#infileLines = infile.readlines()

	#for x in infileLines:
		#intX = int(x.strip())
		#myArray.append(intX)
	displayUnique(myArray)
	# To print the locations of all the values
	#for x in range(0, len(myArray)):
	#	print("location:", x, " value:", myArray[x])
	#printing the value are [-15] before 7s are removed
	print(myArray.__getitem__(-15))
	# To keep track of the indexes of 7s
	indexes=[]
	for i in range(0, len(myArray)):
		if myArray[i]==7:
			indexes.append(i)
		#	print("location:",i,"value:",myArray[i])
	# removing all 7s
	myArray.removeAll(7)
	# reprinting the value at [-15]
	print(myArray.__getitem__(-15))
	# inserting back the 7s at the previous indexes
	for k in range(len(indexes)):
		myArray.insertEfficient(indexes[k],7)
	# print the value at [-15] to confirm insertion
	#print("value at arr[-15] when 7s are re-inserted:",myArray[-15])
