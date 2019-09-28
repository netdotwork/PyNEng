vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

# transform our list-type to tuple-type for detect unique arguments only
set1 = set(vlans)

# output for checking only
#print(set1)

# transform back (we have got unique list of elements already)
# sort and print it
list1 = list(set1) 
list1.sort()
print(list1)
