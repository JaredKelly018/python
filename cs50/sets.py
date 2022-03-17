#create an empty set
s = set()

#add elements to set
#only can appeare once no matter how many times it appears

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(3)
s.remove(1)
s.add(6)
print(s)

#how many elements in set
print(f'The set has {len(s)} elements.')
