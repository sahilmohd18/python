b=(1,2,3,4,5)
b1=bytes(b)
# print(b1)    

# range (0-256) allowed
# b=(1,2,354,4,5)
# b1=bytes(b)
# print(b1)

#immutable
# b1[0]=7  #not possible
# print(b1)

#loop in bytes
for i in b1:print(i)