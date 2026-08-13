# Conditional statements-->if, elif, else

#--->reuirement:brand feature one tagline:

# brand_name=input("Enter your brand name:")
# if brand_name=="KFC":
#    print("It's a Grilled Chiken serving chain.")
# elif brand_name=="TATA":
#    print("TATA is a conglomerate and bussiness house.")
# elif brand_name=="Bata":
#    print("It's a premium Footwear Brand.")
# elif brand_name=="Reliance":
#    print("Relaince is a conglomerate and bussiness house.")
# else:
#    print("Others Are Not Suggestable Brands.")

# listBrands=["kfc","bata","tata","toyota"]
# print(listBrands)
# user=input("select your brand : ")
# if user==listBrands[0]:
#     print("it's a grilled chicken serving food chain.")
# elif user==listBrands[1]:
#     print("it's a premium footwear brand.")
# elif user==listBrands[2]:
#     print("TATA is a coglomerate and bussiness house.")
# elif user==listBrands[3]:
#     print("TOYOTA is a leading automobile co.")
# else:
#     print("others brands are out of my scope to suggest.")



#--->requirement: finding biggest among three numbers.
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))
# if num1>num2:
#   print("The first number {0} is greater than second number {1}.".format(num1,num2))
# else:
#   print("The second number {0} is grater among two numbers.".format(num2))   # flawed program.
# if num1>num2 and num1>num3:
#     print("Biggest Number:",num1)
# elif num2>num3:
#     print("Biggest Number:",num2)
# else:
#     print("Biggest Number:",num3)



#--->requiremnet:check even and odd number.
# num1=int(input("enter first number:"))
# if num1%2==0:
#     print("the number {0} is an even number.".format(num1))
# else:
#     print("the number {0} is an odd number.".format(num1))


#--->Reuirement: Check whether a number is greater than 100.
# num1=int(input("enter any number:"))
# if num1>100:
#     print("The number",num1,"is greater than 100")
# else:
#     print("The number",num1,"is not grater than 100")
  

#--->Requirement: Check whether a person is eligible to vote (age ≥ 18)
# name=input("enter your name:")
# age=int(input("enter your age:"))
# if age>=18:
#     print("The person named",name,"aged",age,"years old is eligible to vote.")
# else:
#     print("The person named",name,"aged",age,"years old is not eligible to vote.")


#---> requirement: Check whether a student has passed (marks ≥ 33).
# name=input("enter student name:")
# marks=int(input("enter students marks:"))
# if marks>=33:
#     print("The student named",name, "has been passed with a score of",marks,)
# else:
#     print("The student named",name, "has not passed the exam and has scored",marks,)


#--->Requirement: Check whether a number is divisible by 5.
# num=eval(input("enter any number:"))
# if num%5==0:
#     print("The number",num,"is divisible by 5.")
# else:
#     print("The number",num,"is not divisible by 5.")
        

#--->Requirement:Check whether a character is a vowel
# char=input("enter any character:")
# if char in "a,e,i,o,u":
#     print("yes",char,"is a vowel.")
# else:
#     print("no",char,"is not a vowel.")    

#--->Reqirement:Check whether a character is an uppercase letter.(uppercase->.isupper();lowercase-->.islower())
# char=input("input any character:")
# if char.isupper():
#     print("the character",char,"is an uppercase character.")
# else:
#     print("the character",char,"is not a uppercase character.")
    


        
#--->Requirement:Check whether the entered password is "python123".
# password=input("Enter Password:")
# if password=="python123":
#     print("Password Entered Is python123.")
# else:
#     print("Password Entered Is Not python123.")



#--->Requirement:Check whether a number is even or odd.
# number=int(input("Enter Any Number :"))
# if number%2==0:
#     print("The Number",number,"is an even number.")
# else:
#     print("The number",number,"is an odd number.")


#--->Requirement:Find the greater of two numbers.
# number1=int(input("enter first number:"))
# number2=int(input("enter second number:"))
# if number1>number2:
#     print("first number",number1,"is greater.")
# elif number1==number2:
#     print("both the numbers are equal.")
# else:print("second number",number2,"is greater.")


#--->Requirement:Check whether a number is positive or negative.
# number=eval(input("enter any number:"))
# if number>=0:
#     print(number,"is a positive number")
# else:print(number,"is a negative number")


#--->Requirement:Check whether a number is divisible by both 3 and 5.
# number=eval(input("Enter Any Number:"))
# if number%3==0 and number%5==0:
#     print(number,"is divisible by both 3 and 5.")
# elif number%3==0 and number%5!=0:
#     print(number,"is divisble by 3 but not by 5.")
# elif number%3!=0 and number%5==0:
#     print(number,"is not divisible by 3 but divisible by 5.")
# else:print(number,"is not divisible either by 3 or by 5.") 


#--->Requirement:Check whether a year is a leap year (basic version).
# year=int(input("Enter Any Year:"))
# if year%400==0 or (year%4==0 and year%100!=0):
#     print("Year",year,"is a leap year.")
# else:
#     print("Year",year,"is not a leap year.")

#--->Requirement:Check whether a character is a vowel or consonant.
# c=input("Enter Any Character:")
# if c in "aeiouAEIOU":
#     print(c,"is a vowel.")
# else:
#     print(c,"is a constant.")


#--->Requirement:Check whether a number is a multiple of 7.
# num=eval(input("Enter Any Number:"))
# n=1
# if num%7==0:
#     print(num,"is a multiple of 7.")    7*2=14
# else:
#     print(num,"is not a multiple of 7.")



#--->Requirement:Check whether a number is less than 50.
# num=eval(input("Enter Any Number:"))
# if num<50:
#     print(num,"is less than 50.")
# else:
#     print(num,"is not less than 50.")

# if num in range(50):
#     print(num,"is less than 50.")
# else:
#     print(num,"is not less than 50.")


#--->Requirement:Compare two passwords and print:
# pwd1=input("Enter Your Password:")
# pwd2=input("Re-Enter Your Password:")
# if pwd1==pwd2:
#     print("login Successful.")
# else:
#     print("Password Mismatch.")
                # or
# pwd1=eval(input("Enter Your Password:"))
# pwd2=eval(input("Re-Enter Your Password:"))
# if pwd1==pwd2:
#     print("login Successful.")
# else:
#     print("Password Mismatch.")


#--->Requirement:Find the largest among three numbers.
num1=eval(input("Enter first Number:"))
num2=eval(input("Enter second Number:"))
num3=eval(input("Enter third Number:"))
if num1>num2 and num3:
    print("First number",num1,"is the largest no.")
elif num2>num3:
    print("Second number",num2,"is the largest no.")
else:
    print("Third number",num3,"is the largest no.")



#--->Requirement:Give grades based on marks.[90–100 : A/80–89  : B/70–79  : C/60–69  : D/Below 60 : Fail]
# marks=eval(input("Enter Your Marks:"))
# if marks in range(90,101):  #range in python can only contains int type.
#     print("Marks =",marks)
#     print("Grade = A")
# elif marks in range(80,90):
#     # print("Marks =",marks)
#     print("Grade = B")
# elif marks in range(70,80):
#     # print("Marks =",marks)
#     print("Grade = C")
# elif marks in range(60,70):
#     # print("Marks =",marks)
#     print("Grade = D")
# elif marks<60:
#     # print("Marks =",marks)
#     print("FAIL")    


# marks=eval(input("Enter Your Marks:"))
# if marks>=90.0 and marks<=100.0:
#     print("Grade = A")
# elif marks>=80 and marks<=89:
#     print("Grade = B")
# elif marks>=70 and marks<=79:
#     print("Grade = C")
# elif marks>=60 and marks<=69:
#     print("Grade = D")
# elif marks<60:
#     print("FAIL")


#--->Requirement: Calculator.
# num1=eval(input("Enter first value:"))
# opt=input("Enter operator:")
# num2=eval(input("Enter Second value:"))
# if opt=="+":
#     print("Result=",num1+num2,)
# elif opt=="-":
#     print("Result=",num1-num2)
# elif opt=="*":
#     print("Result=",num1*num2)
# elif opt=="/":
#     print("Result=",num1/num2)


#--->Requirement:Print the day of the week based on a number.
# day=int(input("Enter number of the day of week:"))
# if day==1:
#     print("SUNDAY")
# elif day==2:
#     print("MONDAY")
# elif day==3:
#     print("TUESDAY")
# elif day==4:
#     print("WEDNESDAY")
# elif day==5:
#     print("THURSDAY")
# elif day==6:
#     print("FRIDAY")
# elif day==7:
#     print("SATURDAY")


#--->Requirement:Print the month name using month number.
# month=int(input("Enter number of the month:"))
# if month==1:
#     print("JANUARY")
# elif month==2:
#     print("FEBRUARY")
# elif month==3:
#     print("MARCH")
# elif month==4:
#     print("APRIL")
# elif month==5:
#     print("MAY")
# elif month==6:
#     print("JUNE")
# elif month==7:
#     print("JULY")
# elif month==8:
#     print("AUGUST")
# elif month==9:
#     print("SEPTEMBER")
# elif month==10:
#     print("OCTOBER")
# elif month==11:
#     print("NOVEMBER")
# elif month==12:
#     print("DECEMBER") 


#--->Requirement:Check whether a person is[child,teenager,adult,senior citizen]
# name=input("Enter Your Name:")
# age=int(input("Enter Your Age:"))
# if age<=12:
#     print(name,"your age is",age,"and you are a CHILD.")
# elif age>12 and age<=17:
#     print(name,"your age is",age,"and you are a TEENAGER.")
# elif age>17 and age<=59:
#     print(name,"your age is",age,"and you are an ADULT.")
# elif age>59:
#     print(name,"your age is",age,"and you are a SENIOR CITIZEN.")






























# Iterative statements---> for loop , while loop , infinite Loop , nested loop

# for loop:

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


# Requirement--->Print all even numbers from 1 to 20.
# r=range(1,21)
# for i in r:
#     if i%2==0:
#         print(i)
#     else:pass    


# Requiement--->Print all multiples of 5 up to 100.
# r=range(5,101,5)
# for i in r:
#     print(i)


# Requirement--->Print your name 10 times.
# s="sahil"
# n=0
# while n<=10:
#     print(s)
#     n+=1    #it's a while loop program.

# name="sahil"
# for i in range(10):
#     print(name)    #it's a for loop program







# using user input:
    
# Requirement--->Print the multiplication table of a number.



        
    











# Requirement---> add sum of element present in sequence.






    