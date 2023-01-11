
iList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('iList: ',iList)

print('first element: ',iList[0]) 

print('fourth element: ',iList[3]) 

print('iList elements from 0 to 4 index:',iList[0: 5]) 

print('3rd or -7th element:',iList[-7]) 



iList.append(111)
print('iList after append():',iList)

 
print('index of \'80\': ',iList.index(80))


iList.sort()
print('after sorting: ', iList);


print('Popped elements is: ',iList.pop())
print('after pop(): ', iList);


iList.remove(80)
print('after removing \'80\': ',iList)


iList.insert(2, 100)
print('after insert: ', iList)

print('number of occurences of \'100\': ', iList.count(100))


iList.extend([11, 22, 33])
print('after extending:', iList)


iList.reverse()
print('after reversing:', iList)
