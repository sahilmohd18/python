# Iterative statements---> for loop , while loop , infinite Loop , nested loop

# FOR LOOP:

# l = range(5)
# print(l[1])
# print(type(l))


# str = range("sharif")
# # print(str)

# for i in range(5):
#     print(i*2)


# str="sharif"
# i=1
# for r in str:
#     if i<len(str):
#       print(r,end='_')
#     else:
#        print(r,end='')    
#     i+=1

# str="sharif"
# i=1
# for r in str:
#     if i<3 or i>3:
#         print(r,end='')
#     elif i==3:
#         print(r,end='_')    
#     i+=1


# str="sharif"
# print('_',str,sep='',end='_')
# print('_',str,'_',sep='')

# print('_',end='')
# print(str,end='')
# print('_')

# i=1
# for r in str:
#     if i==1:
#         print('_',r,sep='',end='')
#     elif i==6:
#         print(r,'_',sep='')    
#     else:
#         print(r,end='')
#     i+=1        



# Requirement---> value at each index
# name=input("Enter Name:")
# ind=0
# for i in name:
#     print("The Value Present At",ind,"index is",i)
#     ind+=1


# Print numbers from 1 to 10.
# R=range(1,11)
# for i in R:
#     print(i)

# Print numbers from 10 to 1.
# r=range(1,11)
# ind=-1
# for i in r:
#     print(r[ind])
#     ind-=1


# Requirement--->Print all even numbers from 1 to 20.
# r=range(1,21)
# for i in r:
#     if i%2==0:
#         print(i)
#     else:pass    


# Requiement--->Print all multiples of 5 up to 100. (multiple of 5 is those number which we get if we multiply 5 with any whole no OR integars.)
# r=range(5,101,5)
# for i in r:
#     print(i)


# Requirement--->Print the multiplication table of a number.
# num=int(input("Enter Any Number:"))
# time=1
# while time<=10:
#     print(num,'*',time,'=',num*time)
#     time+=1
# print(num)

# for i in range(1,11):
#     print(num,'*',i,'=',num*i)



    
# Requirement--->Print the squares of numbers from 1 to 10.
# for i in range(1,11):
#     print(i*i)     #-->for loop

# num=1
# while num<=10:
#     print(num*num)
#     num+=1           #-->while loop


# Requirement:--->Print numbers divisible by both 3 and 5 from 1 to 100.
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)
#     else:pass      #for loop


# num=1
# while num<=100:
#     if num%3==0 and num%5==0:
#         print(num)
#     else:pass
#     num+=1         #while loop


# Requirement--->Find the sum of numbers from 1 to N
# num=int(input("Enter Number Uptil You Want Sum:"))
# r=range(1,num+1)
# print(sum(r))   #very direct

# num=int(input("Enter First N Number To Do Sum:"))
# r=range(1,num+1)
# t=0
# for i in r:
#     t=i+t
# print(t)


# Requirement--->Count how many numbers between 1 and N are even.
# num=int(input("Enter First N Number:"))
# c=0
# for i in range(1,num+1):
#     if i%2==0:
#         c+=1
#     else:pass

# print("The Numbers of Even No.s betweeen 0 -",num,"=",c)



# Requirement--->Count how many numbers between 1 and N are divisible by 7.
# num=int(input("Enter N Number:"))
# c=0
# for i in range(1,num+1):
#     if i%7==0:
#         c+=1
#     else:pass

# print("The Total numbers of Number Between 0 -",num,"Which Are Divisible By 7","=",c)


# Requirement--->Find the product of numbers from 1 to N (Factorial).
# num=int(input("Enter First N Number:"))
# product=1
# for i in range(1,num+1):
#     product=product*i
# print("The Product of Fisrt",num,"numbers is =",product)
























# WHILE LOOP:

# Requirement--->Print your name 10 times(10 iterations).
# s="sahil"
# n=0
# while n<=10:
#     print(s)
#     n+=1    #it's a while loop program.

# name="sahil"
# for i in range(10):
#     print(name)    #it's a for loop program



# Requirement--->Print numbers from 1 to 10 using while.
# r=1
# while r<=10:
#     print(r)
#     r+=1


#Requirement--->Print numbers from 10 to 1
# r=10
# while r>=1:
#     print(r)
#     r-=1


#Requirement--->Print all even numbers between 1 and 50.
# count=1
# while count<=50:
#     if count%2==0:
#         print(count)
#     else:pass
#     count+=1

#Requirement--->Print all odd numbers between 1 and 50.
# count=1
# while count<=50:
#     if count%2!=0:
#         print(count)
#     else:pass
#     count+=1



#Requirement--->Print all multiples of 9 up to 100.
# count=1
# while count<=100:
#     if count%9==0:
#         print(count)
#     else:pass
#     count+=1     #already done without range.



#Requirement--->Find the sum of numbers from 1 to N.
# num=int(input("Enter First N Numbers to Find Sum:"))
# r=range(1,num+1)
# total=0
# no=1
# while no in r:
#     total=total+no
#     no+=1
# print("The sum of first",num,"Number is = ",total)

#OR

# num=int(input("Enter Any Number:"))
# no=1
# sum=0
# while no<=num:
#     sum+=no
#     no+=1
# print(sum)         #without range fx.



#Requirement--->Find the factorial of a number using while loop.
# num=int(input("Enter Any Number:"))
# r=range(1,num+1)
# no=1
# product=1
# while no in r:
#     product=product*no
#     no+=1
# print("The Factorials Of",num,"is = ",product)

#OR

# num=int(input("Enter Any Number:"))
# no=1
# product=1
# while no<=num:
#     product=product*no
#     no+=1
# print(product)      #without range fx.


#Requirement--->Count the number of digits in a number.
# num=int(input("Enter Any Number to Count Digits:"))
# count=0
# while num>0:
#     num=num//10
#     count+=1
# print(count)

#OR --->numeric string and indexing.

# num=input("Enter Number to Count digit:")
# r=range(num[0],num[-1])
# n=num[0]
# count=0
# while n in r:
#     count=count+1
#     n+=num[1]
# print(count)   ##ERROR



#Requirement--->Reverse a number.
# num=int(input("Enter Any Number:"))
# reverse=0
# while num!=0:
#     lastD=num%10
#     reverse=reverse*10+lastD
#     num=num//10
# print(reverse)



#Requirement--->Find the sum of digits of a number.
# num=int(input("enter no:"))
# sum=0
# while num>0:
#     sum+=num%10
#     num=num//10
# print(sum)


#Requirement--->Find the product of digits.
# num=int(input("Enter Number:"))
# product=1
# while num>0:
#     product*=num%10
#     num=num//10
# print(product)


#Requirement--->Find the largest digit in a number.
# num=int(input("Enter Number:"))
# lastd=0
# gdigit=0
# while num>0:
#     lastd=num%10
#     if lastd>gdigit:
#         gdigit=lastd
#     else:pass
#     num=num//10
# print(gdigit)



#Requirement--->find second largest number.
# num=int(input("Enter Number:"))
# lastD=0
# gno=0
# gno2=0
# while num>0:
#     lastD=num%10
#     if lastD>gno:
#         gno=lastD
#         if gno2<gno and gno2>lastD:
#             gno2=gno
#         else:pass
#     else:pass
#     num=num//10        
# print(gno2)


# num=int(input("Enter Number:"))
# lastD=0
# gno=0
# gno2=0
# while num>0:
#     lastD=num%10
#     if lastD>gno:
#         gno=lastD
#         if lastD<gno and lastD>gno2:
#             gno2=lastD
#         else:pass
#     else:pass
#     num=num//10
# print(gno2)


#Requirement--->Find the smallest digit.


#Requirement:Check whether a number is a palindrome.
# num=int(input("Enter Any Number:"))
# original_no=num
# lastD=0
# reverse=0
# while num!=0:
#     lastD=num%10
#     reverse=reverse*10+lastD
#     num=num//10
# if reverse==original_no:
#     print("Number is a palindrome number.")
# else:
#     print("number is not a palindrome number.")


#Requirement:Check whether a number is an Armstrong number.

#Requirement:check whether a number is a strong number.


#Requirement:Count how many even and odd digits are present in a number.(can do it separately)
# num=int(input("Enter Number:"))
# prime_no=0
# odd_no=0
# while num!=0:
#     lastD=num%10
#     if lastD%2==0:
#         prime_no+=1
#     else:
#         odd_no+=1
#     num=num//10
# print("Total count of prime number is",prime_no,
#       "And odd number is",odd_no)


#Requirement:Find the sum of even digits and the sum of odd digits separately.
# num=int(input("Enter Number:"))
# sumPN=0
# sumON=0
# while num!=0:
#     lastD=num%10
#     if lastD%2==0:
#         sumPN+=lastD
#     else:
#         sumON+=lastD
#     num=num//10
# print("Sum of even digit =",sumPN)
# print("Sum of odd digit =",sumON)


















