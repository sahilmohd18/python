s={1,2,3,4,"sahil",'sharif',10.5,(45,'sahil')}
# print(s)
# for i in s:print(i)
# s.add("shahida")
# s.remove(3)
# print(s)


# add()
# s.add(True)
# s.add("palik")
# s.add(10.5)
# s.add("palik")
# s.add(10.6)
# s.add(14)
# s.add(1000)
# s.add("kareemganj")
# s.add(10+34j)
# print(s)
# s.add([10,20])      # TypeError.
# print(s)            
# s.add({'a':10})       # TypeError.
# print(s)


# -->update()
# s.update('sahil')
# print(s)
# s.update('sahil',[10,20])
# print(s)
# s.update(10)           # TypeError.
# print(s)
# s.update(True)           # TypeError.
# print(s)



# -->deletion-remove(),discard(),pop(),clear().
# s.remove(10)            # Key error
# s.remove(10.5)
# print(s)
# s.remove([10,20])       # TypeError.
# s.remove('sahi')        # Key Error.
# s.remove(10.5,"sahil")  #Type Error.--excess arg.

# s.discard(10)             # will not through error.
# print(s)
# s.discard(10.5,'sahil')     # Type Error.--excess arg.
# s.discard((45,'sahil'))     # one arg & should be immutable.-as set accept value as hashing.
# print(s)

# 1 s.pop()                       # Return the popped value. Raise KeyError if empty.
# 2 print(s.pop())
# print(s)
# 3 s.pop()
# print(s)
# s.pop()
# print(s)


# print(s.clear())                # NONE.
# s.clear()
# print(s)                          # empty set.





# methods for mathmetical operations.
# s1={10,20,30,40}
# s2={30,40,50,60}
# s3={50,60,70,80}

# union()   or | operator
# s4=s1.union(s2)
# print(s3)
# s5=s1|s2
# print(s4)
# s5=s1.union(s2,s3)            union of 3 set.
# print(s5)


# intersection(). and '&' operator.
# s4=s1.intersection(s2)
# print(s4)
# s4=s2.intersection(s1)
# print(s4)
# s4=s1.intersection(s2,s3)           # Empty set
# print(s4)


# s4=s1.difference(s2)                # uncommon but from one set 
# print(s4)
# s4=s2.difference(s1)
# print(s4)
# s4=s1.difference(s2,s3)
# print(s4)








