# d={1:'sahil',2:'sharif','palik':3,'ibrahim':4}
# print(d)
# for i in d:print(i)
# print(d[2])

# print(d[1])
# print(d[2])
# print(d[3])
# for i in d:
#     # print(i)
#     # print(type(i))
#     print(d[i])


#d1={}--->>empty dict and not set(for set-->d1=set{})

n=int(input("Enter Number of student:"))
d={}
for i in range(n):
    name=input("enter name of student:")
    marks=int(input("enter marks of student:"))
    d[name]=marks
print('_'*30)
print('NAMES','\t\t\t','MARKS')
print('_'*30)
for name in d:
    print(name,'\t\t\t',d[name])