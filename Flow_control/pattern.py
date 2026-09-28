# ->PATTERN PRINTING.--> '*' ; inc/dec * ; numbers.

#Requirement-->print 3 rows with five "*" forming a square. 
# for i in range(1,4):
#     for j in range(1,7):
#         print("*",end="",)
#     print()

#:-> vertical spacing.
# for i in range(1,4):
#     for j in range(1,7):
#         print("*",end="",)
#     print()
#     print()

# :-> using \t(horizantal spacing)
# for i in range(1,4):
#     for j in range(1,7):
#         print("*",end="\t")
#     print()

#Requirement-->print rectangle 3 by 10.
# for  i in range(1,4):
#     for j in range(1,11):
#         print("*",end="")
#     print()

# NUMBER:

#Requirement-->
# output:-
# 12345
# 12345
# 12345
# 12345

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")
#     print()

#Requirement:output
# 11111
# 22222
# 33333
# 44444
# 55555

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end="")
#     print()
    
#Requirement:output
# 12345
# 23456
# 34567
# 45678
# 56789
 
# for i in range(1,6):
#     for j in range(5):
#         print(i+j,end="")
#     print()

        
#Requirement:output
# A       *
# AB      **
# ABC     ***
# ABCD    ****
# ABCDE   *****

# for i in range(1,6):
#     print(i*"*")
    # for j in range(1,6):
    #     print(j*"*")


#Requirement:output
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(j,end="")
#         else:
#             break;
#     print()

# through while loop:
# 1
# 12
# 123
# 1234
# 12345

num=1
while num<=5:
    print(num*10+num)
    num+=1






#Requirement:output
# 12345
# 1234
# 123
# 12
# 1

# for i in range(1,6):
#     for j in range(1,6):