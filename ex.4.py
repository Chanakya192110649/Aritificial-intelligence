string = input("Enter a string: ")   
words = string.split()   
words.sort()   
for word in words:
   print(word , end = " ")
