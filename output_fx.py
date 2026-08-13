# print("hello")
# print()
# print("good evening")
# print()
# print("how are you")
# print() w/o argument-->blank line

# print()-->with argument and string concatination
# print("durga"+"software")
# print("durga"*2)

# print with "sep" attribute.

a,b,c=10,20,30
#print("The result is:",a,b,c)
# print(a,b,c)  --->default separator is space
# print(a,b,c,sep='')
print(a,b,c,sep=',')
#print(a,b,c,sep=':')
#print(a,b,c,sep=';')

# print with end='' attribute.

#print(a,b,c,end='/')
#print(a,b,c,end='/')
#print(a,b,c)

#print with "sep=''" and "end=''" attribute

#print(a,b,c,sep=' ',end='/')
#print(a,b,c,sep=',',end='/')
#print(a,b,c,sep=':',end='/')
#print(a,b,c,sep=';') 


# print(formatted string)
#print("a value is %i" %a)
#print("b value is %i" %b)
#print("c value is %i" %c)
#print("c value is %i and a value is %i" %(c,a))

#name="Mohammad Sahil"
#age=25
#print("My name is %s and i am %i years old." %(name,age))


# print() with replacement operators.

# name="sahil"
# salary=10000
# name1="shahida"
# print("hello {0} your salary is {1} and your mother {2} is waiting..".format(name,salary,name1))  #order sensetive case
# print("hello {s} your salary is {s1} and your mother {s2} is waiting for you at home..".format(s2=name1,s=name,s1=salary))    #order insensetive case


  