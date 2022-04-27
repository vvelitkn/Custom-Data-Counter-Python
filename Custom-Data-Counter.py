# Python3 program to find number of
# times a string appears in an array.

# Returns count of occurrences of s in arr[]
import csv


def search(arr, s):
	counter = 0
	for j in range(len(arr)):
		if (s == (arr[j])):
			counter += 1
    
	return counter

def final(arr, arr1):
    arr1.sort()
    number = 4                                          # how much participate/etc will be accepted
    for i in range(len(arr1)):
        if (search(arr, arr1[i])>=number):
            print(*arr1[i])                             # *arr1[i] gives us without (' ')


with open(r"YOURFILEPATH", newline='') as f:            # don't forget to change YOURFILEPATH
    _noduplicatedata =[]
    _transformed = []

    reader = csv.reader(f)
    alldata = list(reader)

    
    for data in alldata:                                # transform data to use list(set(_transformed))
        data = tuple(data)
        _transformed.append(data)   
    
    _transformed.sort()                                 # we want a sorted list
    _noduplicatedata = list(set(_transformed))          
    final(_transformed,_noduplicatedata)                # final is a good name :)


