list=[10,20,'sahil']







#i am doing it in elaborate way.
#refrence sharing in list or not.
# list=[1,2,3,4,5]
# l1=[1,2,3,4,5]
# l2=l1
# print(id(list))
# print(id(l1))
# print(id(l2))
# print(list is l1)
# print(list==l1)


# for i in list and l1:
#     # print(i==i)
    # print(i!=i) comparing the element from list(variable1) and l1(variable2) 


# print(list is l1)
# print(list==l1)
# print(list is not l1)
# print(list!=l1)  #comparing variables(list and l1).
                 #Refernce sharing not allowed in 'list'.

# # print(list)
# l1=list[0]
# l2=list[1]
# l3=list[2]
# l4=list[3]
# l5=list[4]
# l6=list[0:3]
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# print(l5)
# for i in list:print(i)
# print(l6)
# print(list[0])


# short way to do the same + mutability



# list=["lucknow","hyderabad","mumbai","delhi"]
# print(list[0])
# print(list[1])
# print(len(list))     #checking list for rivising it.



# list[2]=85
# print(list)
# for i in list:print(i)


#shortest way 
# list=[1,2,3,4,5]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])


# l1=[10,20,30]
# l2=[40,50,60]
# l3=l1+l2   #list aliasing
# # print(l3)
# l4=l3*3
# # print(l4)
# i=0
# while i<len(l3):
#     print('The value present at +ve index {} and -ve index {} is: {}'.format(i,i-len(l3),l3[i]))
#     i=i+1





# INDEXING AND SLICING IN LIST.
list=[1,2,3,'powershell',(10,'sahil',[10,20,'mohammad',10,10]),['shahida',1978,(10,20,'mohd sharif')]]
# for i in list:
#   print(i)

# print(dir(list))

# x=int(input('enter element to check in list:'))
# if x in list:
#     print("{} is prexent at index no {}".format(x,list.index(x)))
# else:
#     print(x,"not present in list.")

# index=0
# for i in list:
#     print('the value present at +ve index {} and -ve index {} is {}'.format(index,index-len(list),i).title())
#     index=index+1

# print(list[4][2][2][2:6])
# print(list[5][1])
# print(dir(list))
# print(list.count(3))
# print(list.index((10,'sahil',[10,20,'mohammad'])))
# print(list[4][2].index('mohammad'))
# print(list[4][2].count(10))
# print(len(list))
# print(type(list))
# print(type(list[0]))
# print(type(list[3]))
# print(type(list[4]))
# print(type(list[4][2]))
# print(type(list[5]))




# LIST ALIASING AND LIST CLONING.
# list1=[50,'methods',(10,'python',10.5),[10,'hashtag',True]]
# list2=list1
# list3=[50,'methods',(10,'python',10.5),[10,'hashtag',False]]
# list4=list3.copy()
# print(list1==list2)
# print(list1 is list2)
# print(id(list1))
# print(id(list2))
# list2.append(10)
# print(list2)
# print(list1)
# list4.append(20)
# print(list4)
# print(list3)






# METHODS in list.

# adding into list:-append(),insert(),extend()

# list=[1,2,3,'powershell',(10,'sahil',[10,20,'mohammad',10,10]),['shahida',1978,(10,20,'mohd sharif')]]
#1 list.append('sahil')
# print(list)
#2 list.append([80,90,124])
# print(list)
#3 list.append('sahil',[80,90,210])
# print(list)    # append() will accept only one arg mandatorly. and that is--value to append.
#4 list.append(10)
# print(list)
#5 list.append(10,20,30)
# print(list)      # ERROR
#6 list.append((10,20,30))
# print(list)
#7 list.append((10))
# print(list)      #not a tuple but own datatype
#8 list.append((10,))
# print(list)
#9 list.append([10])
# print(list)

#1 list.insert(2,'pencil')
# print(list)
#2 list.insert(0,'sahil')
# print(list)
#3 list.insert(100,10)
# print(list)          # incase indexno out of range and is +ve ->add in last.
#4 list.insert(-100,10)
# print(list)          # incase indexno out of range and is -ve ->add in beginning.
#5 list.insert()
# print(list)          # ERROR
#6 list.insert(10,'enter',20)
# print(list)            # ERROR
#7 print(len(list))
#8 list.insert(2,[10,20,30])
# print(list)
# print(len(list))

#1 list.extend([80,90,124],)
# print(list)
#2 list.extend('sahil',10)
# print(list)           #ERROR- extend will accept only one agr & should be iterable.
#3 list.extend((10,5.6))
# print(list)
#4 print(list)
# list.extend('water')
# print(list)



# Removing from list--remove(),pop(),clear().
# list=[1,2,3,3,'powershell',(10,'sahil',[10,20,'mohammad',10,10]),['shahida',1978,(10,20,'mohd sharif')]]
#1 list.remove(1)
# print(list)
#2 list.remove('sharif')
# print(list)         #V/E:value not present in list as list element.
#3 print(len(list))
# list.remove(['shahida',1978,(10,20,'mohd sharif')])
# print(list)
# print(len(list))
#4 list.remove(1,2)
# print(list)         #T/E:remove() take only one arg.
#5 list.remove(3)
# print(list)         # if xple occurance of same value--> first occurance will get removed.


#1 print(list.pop(1))  # return value removing.
# print(list)
#2 print(list.pop(12))
# print(list)          #INDEX ERROR.
#3 print(list)
# print(list.pop())
# print(list)
#4 list.clear()
# print(list.pop())    #don't work on empty list.
# print(list)


# list.clear()
# print(list)     #give empty list.
 



# ordering element of list--reverse(),sort().
# list=[1,2,3,3,'powershell',(10,'sahil',[10,20,'mohammad',10,10]),['shahida',1978,(10,20,'mohd sharif')]]

#1 list.reverse()
# print(list)
#2 l=[5,2,3,6,8,1,7]
# l.sort()
# print(l)
#3 l=['sahil','abdul','zoraver','kaamil','roshan']
# l.sort()
# print(l)


str='python'
print(str.split('py'))
