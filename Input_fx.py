#1)
# a=int(input("Enter first numbers"))
# b=int(input("Enter second number"))
# print("The sum is:",a+b)
#         or
# print("The sum is:",int(input("Enter first numbers"))+int(input("Enter second number")))
#         or
# xple values in a single line of code 
# a,b=[int(x) for x in (input("enter 2 number:").split())]
# print(("The Division is:"),a/b)

# a,b,c=[int(x) for x in (input("enter 3 number:").split())]
# print(("The Division is:"),a+b+c) 


#2)
# a=input("Enter password:")
# b=input("confirm password:")
# print("you're successfully logged in.." if a==b else "Password mismatch found" )


#3)-->read emp data from keyboard--,eno,enameddress,esal and print to console with confirmation Head

# a=input("Enter employee name:")
# b=int(input("Enter employee number:"))
# c=int(input("Enter employee salary:"))
# d=input("Enter employee address:")
# print("confirm your information:\n","employee name:",a,"\n","employee number:",b,"\n","employee salary:",c,"\n","employee address:",d)
# 
# or
# 
# print(f"""
# confirm your information:
# employe name:{a}
# employee number:{b}
# employee salary:{c}
# employee address:{d}""")

# or

# print("""
# confirm your information:
# Employee Name:{}
# Employee Number:{}
# Employee salary:{}
# Employee Address:{}
# """.format(a,b,c,d))
# or
# print("""
# confirm your information:
# Employee Name:{A}
# Employee Number:{B}
# Employee salary:{C}
# Employee Address:{D}
# """.format(A=a,B=b,C=c,D=d))

#  or

# print("""
# Employee Name"""+a+"""
# Employee number"""+b+"""
# Employee Salary"""+c+"""
# Employee Address"""+d+"""
# """)

#4)--->read multiple values from the keyboard in a single line: Refer 3rd subpart of 1st part

#5)-->raed 2 float values from keyboard which has specified with(,)separation in ONE LINE and print sum.
# a,b=[float(x) for x in (input("Enter 2 float values:").split(","))]
# print("the sum of provided values is:",a+b)
#     or--->for removing unwanted spaces through below method
# print(f"""
# The sum of provided values is:{a+b}""")

# 6)--> eval() function; in input()--read and do operation on provided expession before hand 
# a=eval(input("Enter expression to perform operations:"))
# print("the answer for provided expression is: ",a)

#            or(entended version)

# exp=input("Enter any expression:")
# result=eval(exp)
# print(("The result is:"),result)


#eval()-->for type casting as input() by default assign "str" datatype
# exp=input("Enter some data:")
# result=eval(exp)
# print(type(result))

# eval()-->for xple value in one line
# a,b,c,d=(eval(x)for x in input("enter 4 values:").split(","))
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#   or
# for(i) in a,b,c,d:
#     print(type(i))


#7)-->command line arguement 
from sys import argv
# print("The list of command line argument:",argv)
# print("Thenumber of values in command line:",len(argv))
# print("The values in command one by one is:")
# for i in argv:
#     print(i)
# print(argv)
#print(len(argv))



#name=int(input("Enter a number:"))
#print("The square of given number is:",name**2)  # /name*name


#r=float(input("Enter the radius:"))
#print("The area of the circle is:",r*3.14)
































