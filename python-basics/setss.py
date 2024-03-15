# s=set()
# print(type(s))
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# s.add(10)
# s.add(9)
# s.add(8)
# s.add(1)
# s.add(2)
# print(s)
# print(s[5])
s1={1,2,3,4,5}
s2={1,2,10,9}
s3={15,25}
s4={36,100,15,39}
print(s1.union(s2).union(s3).union(s4))
print(s1.intersection(s2))

s3.pop()
print(s3)
s4.remove(100)
print(s4)