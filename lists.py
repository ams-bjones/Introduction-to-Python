mylist = []
print (mylist)
mylist.append(1)
print (mylist)
mylist.append('a')
print (mylist)
yourList = list('hello Ash')
print (yourList)
mylist = mylist + yourList
print (mylist)
alphabetlist = list('abcdefghijklmnopqrstuvwxyz')
print (alphabetlist)
newlist = []
for letter in alphabetlist:
    asciiChar = ord(letter)
    newlist.append(asciiChar)
print (newlist)
mylist.remove('l')
print (mylist)
print (len(alphabetlist))
print (len(newlist))
print (min(alphabetlist))
print (min(newlist))
print (max(alphabetlist))
print (max(newlist))
print (alphabetlist[4])
print (alphabetlist[5:8])
print (alphabetlist[1:10:2])
print (alphabetlist[:2])
print (alphabetlist[::2])
print (alphabetlist[::-1])