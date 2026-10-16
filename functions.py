# Learning & Practising Function Declaration And Function Calling.

# def hello():
#     print('hello world')
# hello()
# print(hello())


# "Parameter Practise."
# def para(a,b):
#     print('hello world')
# para(10)         --error
# para(10,20)
# para(10,10,30)   --error
# para()           --error       .


#1 def f1(a,b):
#     product=a*b
#     print(product)
# f1(4,20)
# print(f1(4,20))


# def f2(a,b):
#     sum=a+b
#     product=a*b
#     print(sum,product)
#     return sum,product
# f2(25,4)
# print(f2(5,2))


# def squareit(num):
#     print('The square of {} is {}.'.format(num,num*num))
# squareit(5)
# print(squareit(5))
# squareit(6)
# squareit(10)



# def squareit2(num):
#     if type(num)==str:
#         print("'*' is not supported between str operands <One must be int in it.>")
#     else:
#         print(num*num)
# squareit2('sahil')
# squareit2(10)
# squareit2(10,20)
# squareit2()
# a=10
# squareit2(a)











# "Argument practise."

# Positional arg.
# def f3(a,b):
#     div=a/b
#     print(div)
# f3(2,10)            #positional argument
# f3(b=2,a=10)        #keyword argument


# keyword agr.
# def greet(name,time):
#     print('Hello {} good {}'.format(name,time))
# greet('sahil','morning.')           #positional arg.
# greet('sahil','evening.')           #positional arg.
# greet('morning','sahil')            #positional arg.
# greet(time='morning.',name='sahil')     # keyword arg.
# greet(time='morning.','sahil')          # SyntaxError: positional argument follows keyword argument
# greet('sahil',time='morning.')            #positional arg and keyword arg simultaneosly.


# Default arg.
# def greet(name='sahil',time='morning'):
#     print('Hello {} good {}.'.format(name,time))
# greet()
# greet('sharif')
# greet('sahil','evening')
# greet(time='evening')

# def greet1(msg,name='sahil',time='morning',):               #while declaration can't accept non default parameter after default parameter only before.
#     print('Hello {} good {} {}'.format(name,time,msg))
# greet1(',hope you are doing good.')
# greet1(',hope you are doing good.','sharif','evening')
# greet1('how are you',name='ibrahim')



# variable len argument.
# def greet(*x):
#     print('Hello {} good {},{}'.format(x,x,x))
# greet('sahil','eneving.')                            # some problem.

def add(*x):
    sum=0
    for i in x:
        sum=sum+i
    print(sum)
add(10,20,30)
add(224,545,365,25,12)