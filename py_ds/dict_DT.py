d={1:'sahil',2:'sharif','palik':3,'ibrahim':4}
# print(d)
# for i in d:print(i)
# print(d[2])


# accesing dict--default,get,items,values,keys.
#-->default()
#1 print(d[1])
#2 print(d[2])
#3 print(d[3])                 # KeyError.
#4 print(d['palik'])
# print(d[1,2])                  # keyerror.
# print(d[])                     # syntax error.
#5 for i in d:
#     print(i)
#     print(type(i))
#     print(d[i])

#-->get()
# print(d.get())                  # TypeError.
# print(d.get(1))
# print(d.get(2,1))               # accept xple arg but gill value for 1st arg only.
# print(d.get(3))
# print(d.get(3,'key not found'))   #default value instead of none.



#-->items().
# print(d.items())             # in case dict is empty-give list of tuple but empty & do not through any error.
# print(d.items(1))            # TypeError: dict.items() takes no arguments (1 given).



#-->values()
# print(d.values())            # in case dict is empty-give empty list & do not through any error.
# print(d.values(1))           # TypeError: dict.values() takes no arguments (1 given).



#-->keys()
# print(d.keys())                # in case dict is empty-give empty list & do not through any error.
# print(d.keys(1))               # TypeError: dict.keys() takes no arguments (1 given)


# Add,update.

#default_method.
# d[3]='python'
# print(d)
# d[4]='python'
# print(d)
# d[4]='django'
# print(d)


# update() method.
#1 d.update({5:'python'})
# print(d)
#2 d.update({6:'django'},{7:'development'})          #TypeError: update expected at most 1 argument, got 2
# print(d)
#3 d1={6:'django',7:'development'}
# d.update(d1)                                        # one agr but can be a variable having xple value.
# print(d)


#Deletion in dict.--pop(key),pop(key,value),popitem(),clear()
#1 d.pop(1)
# print(d)
# d.pop(3)
# print(d)                # keyerror in case key given not found.
# d.pop(2,1)
# print(d)                  # no error in case arg is more than 1 but perform deletion of 1st arg.
# d.pop()
# print(d)                    # TypeError.

# pop(key,default value)
#1 d.pop(3,'key not found')
# print(d)                   # no error print dict as it is.
#2 print(d.pop(3,'key not found'))


#-->popitem().
# d.popitem()
# print(d)
# d.popitem()
# print(d)
# d.popitem()
# print(d)
# d.popitem()
# print(d)
# d.popitem()                            # keyerror in case dict is empty.
# print(d)


#-->clear().
#1 print(d)
# d.clear()
# print(d)
d.clear(1)


























#d1={}--->>empty dict and not set(for set-->d1=set{})

# n=int(input("Enter Number of student:"))
# d={}
# for i in range(n):
#     name=input("enter name of student:")
#     marks=int(input("enter marks of student:"))
#     d[name]=marks
# print('_'*30)
# print('NAMES','\t\t\t','MARKS')
# print('_'*30)
# for name in d:
#     print(name,'\t\t\t',d[name])