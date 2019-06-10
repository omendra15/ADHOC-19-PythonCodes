#!/usr/bin/python3


adhoc = [1,2,3,1,4,5,66,22,2,6,0,9]
list1 = []
list2 = []

print("no greater than 5")
for i in adhoc :
 if i>5 :
  print(i)
  list1.append(i)

print("no lesss than 2")
for i in adhoc :
 if i<2 :
  print(i)
  list2.append(i)

print("list for numbers >5----",list1)
print("list for numbers <2----",list2)

'''
list1 = [i for i in adhoc if i>5]
print(*list1)

list2 = [i for i in adhoc if i<2]
print(*list2)
'''
