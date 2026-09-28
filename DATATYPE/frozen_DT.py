s={10,20,30,40}
s1=frozenset(s)

# s1.add(50)----->>error:frozanset is immutable
# print(s1)

s2=frozenset(s)
# print(s2)

# print(id(s1))
# print(id(s2))------>>both are different as set is immutable(no reference sharing possible)