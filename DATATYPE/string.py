# str0='saaahil[1,2,3]'
# print(str0[1])
# print(ord(str0[1]))
# print(str0.replace('a','h'))
# print(str0.replace('a','h',1))
# print(str0[-1])

# str1='The quick brown fox jumps over the lazy dog'
# a=(str1[4:9].upper())
# str2=str1.replace('quick',a)
# print(str2)
# print(str2.replace('QUICK','quick'))








































# print(ord('A'))   # to check the ascii value of a character.

# s='index method'
# print(dir(s))       #dir() fx to check methods of an object. Here is string object.


# [string and operation-indexing,slicing,len.,\',\"]
# str='Durga \'Software\' Solution.'
# print(str)
# s1=str[2:10]
# s2=str[2:10:1]
# s3=str[2:]
# s4=str[5:13]
# s5=str[0:21:2]
# print(s1)
# print(str[2,10])    #slice operation directly without variable assignment.
# print(s2)
# print(s3)
# print(s4)
# length=len(str)
# print(len(str))    #lentgh fx directly without variable assignment to it.
# print(length)
# print(s5)
#print(str)

# S="""DURGA 
# SOFTWARE 
# SOLUTIONS."""
# print(S)



'''
s = "programming"
print(s[0:4])
print(s[4:])
print(s[:4])
print(s[-3:])
print(s[:-3])
print(s[2:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(s[100:200])
print(s[5:2])
print(s[-100:5])
print(s[4:-3])
print(s[:-5])
print(s[5:2:-1])
print(s[-1:-6:-1])
print(s[::-2])
print(s[-5:-1:2])
print(s[2:-2])
print(s[-2:2])
'''

# reversing only order of words.
# s=input("enter some string:")
# s1=s.split()
# reverse=s1[::-1]
# s2=' '.join(reverse)
# print(s2)

# THROUGH CORE LOGIC


# REVERSING THE WORD CHARACTERWISE AND ORDER TO REMAIN UNCHANGED.
# s=input('enter some string:')
# s1=s.split()
# r=[]
# i=0
# while i<len(s1):
#     r.append(s1[i][::-1])
#     i=i+1
# output=' '.join(r)
# print(output)
# print(r)      

# reversing evey second word and order to remain unchanged.
# s=input('enter some string:')
# s1=s.split()
# r=[]
# i=0
# while i<len(s1):
#     if i%2==0:
#         r.append(s1[i])
#     else:
#         r.append(s1[i][::-1])
#     i=i+1
# output=' '.join(r)
# print(output)



# TO PRINT CHARACTER AT EVEN AND ODD POSITION IN A STRING.
# s=input('enter any string:')
# i=0
# print('The Character Present At odd Index:')
# while i<len(s):
#        print(s[i])
#        i=i+2
# i=1
# print('The Character Present At Even Index:')
# while i<len(s):
#        print(s[i])
#        i=i+2


# s=input('enter some string:')
# i=0
# print('The Character Present At odd Index:')
# while i<len(s):
#         if i%2==0:
#              print(s[i])
#         else:pass
#         i=i+1       
# i=0
# print('The Character Present At even Index:')
# while i<len(s):
#         if i%2!=0:
#              print(s[i])
#         else:pass
#         i=i+1



# REQUIREMENT:TO MERGE TWO INPUT STRING INTO ONE BY TAKING CHARACTER ALTERNATIVELY.
# s=input("enter first string:")
# s1=input("enter second string:") 
# new=''
# i=0
# j=0
# while i<len(s) or j<len(s1):
#     new=new+s[i]+s1[i]
#     i=i+1
#     j=j+1
# print(new)

# when two string are of different lenght
# s=input("enter first string:")
# s1=input("enter second string:") 
# new=''
# i,j=0,0
# while i<len(s) or j<len(s1):
#     if i<len(s):
#         new=new+s[i]
#         i=i+1
#     if j<len(s1):
#         new=new+s1[j]
#         j=j+1  
# print(new)


# REQUIREMENT: sort character first alphabet and then number
# s=input('enter some alphanumeric string:')
# alphabet=''
# digit=''
# for ch in s:
#     if ch.isalpha():
#         alphabet=alphabet+ch
#     else:
#         digit=digit+ch
# print(alphabet)
# print(digit)
# # aplha=sorted(alphabet)
# # dig=sorted(digit)
# print(''.join(sorted(alphabet)+sorted(digit)))

# or we can also do it using empty list.


#REQUIREMENT-input format a4b3c2 alphabet followed by digit and exp output 'aaaabbbcc'.
# s=input('enter alpha numeric string:')
# output=''
# for ch in s:
#     if ch.isalpha():
#         alpha=ch
#         # output=output+alpha
#     else:
#         # d=int(ch)
#         output=output+(alpha*int(ch))
# print(output)

#same thing but in sorted format format.
# s=input('enter alphanumeric string:')
# unsorted=''
# for ch in s:
#     if ch.isalpha():
#         alpha=ch
#     else:
#         d=int(ch)
#         unsorted=unsorted+(alpha*d)
# output=''.join(sorted(unsorted))
# print(output)

#what if format starting with digit and then aplhabet like 4a3b2c
# s=input('enter aplhanumeric string:')
# output=''
# for ch in s:
#     if ch.isdigit():
#         dig=int(ch)
#     else:
#         output=output+(ch*dig)
# print(output)
# print(sorted(output))
# print(''.join(sorted(output)))

#REQUIREMENT-input format='aaaabbbcc' and exp.output='a4b3c2','4a3b2c
# s=input('enter aplhanumeric string:')
# previous=s[0]
# output=''
# c=1
# i=1
# while i<len(s):
#     if s[i]==previous:
#         c=c+1
#     else:
#         output=output+str(c)+previous
#     if i==len(s)-1:
#         output=output+str(c)+previous
#     i=i+1
# print(output)           #Incomplete


# s1=sorted(input("enter first string:")) 
# s2=sorted(input('enter second string:'))
# if s1==s2:
#     print("both strings are anagrams.")
# else:
#     print("both strings are not anagrams.")

    
    














# .find(), .rfind(), .index(), .rindex()---> to find the index position of sub-string.
# s='industry best facaf'
# print(s.find('s',5,13))     # finding starting from left to right & specific index pack.
# print(s.find('t'))          # finding starting from left to right.
# print(s.rfind('t'))         # finding starting from right to left.
# print(s.rfind('a',14,19))   # finding starting from right to left direction & specific index pack.
# print(s.index('d'))            
# print(s.rindex('d',5,100))
# print(s.index('m'))
# print(s.rindex('m'))         # index and rindex method same as find and rfind method except return response in case sub string not found in main string


# strip(),rstrip(),lstrip()
# locity=['lucknow','mumbai','kanpur','bangaluru']
# city=input("enter any city name:").strip()
# if city in locity:
#     print("{} is your selected city".format(city))
# else:
#     print("city not found.")


# s='abababa'
# print(s.replace('a','b'))
# s='durga software solutions'
# s1=s.replace(' ','')
# print(s1)
# print(s)
# print(id(s1))
# print(id(s))

















#[multiline string using \n(new line)]
# s="it's great to be back on the\ntop step after a few difficult\nrounds,said antonelli,who\nhad drawn a blank in two of the\npast three rounds and seen his\nlead shlashed from a hefty 66\npoints over hamilton in june."            
# print(s)
    

















# STRING MANIPULATION.


# 1-Requirement:to access character of a string taken from keyboard with index positions-->BY USING INDEX AND SLICE OPERATIONS. 
# s=input("enter any string:")
# count=0
# for i in s:
#     print("The character present at positive index {} and negative index {} is {}".format(s[0],i-len(s),i))
#     count+=1         #-->wrong code 


# forward directions.-->sahil
# s=input("enter some string:")
# count=0
# while count<len(s):
#     print("the character present at +ve index {} and -ve index {} is {}".format(count,count-len(s),s[count]))
#     count=count+1


# backward direction-->lihas
# s=input("Enter Any String:")
# count=len(s)-1
# while count>=0:
#     print("The Character Present At +ve Index {} and -ve index{} is {}".format(count,count-len(s),s[count]))
#     count=count-1

# with for loop + forward directions.
# s=input("Enter Any String:")
# count=0
# for i in s:
#     print("The Value Present At +ve index {} and -ve index {} is {}".format(count,count-len(s),i))
#     count=count+1

# with for loop + backward directions.
# s=input("Enter Any String:")
# count=len(s)-1
# for i in s:
#     print("The Value Present At +ve index {} and -ve index {} is {}".format(count,count-len(s),s[count]))
#     count=count-1


# 2-Requirement-->Reversing the string.
# s=input("Enter Any String:")
# count=1
# for i in s:
#     value=s[len(s)-count]  #s[4],s[3],s[2],s[1],s[0]
#     print(value,end='')
#     count=count+1

        #OR
# print(s[::-1])    # simply just using slice operation.

# 3-Requirement--> remove duplicates from string'
# s=input("Enter Any String:")
# string=''
# for i in s:
#     if i not in string:
#         string=string+i
#     else:pass
# print(string)


# or through while loop
# s=input("Enter Any String:")
# count=1
# indxvalue=0
# string=''
# while count<=len(s):
#     if s[indxvalue] not in string:
#         string=string+s[indxvalue] 
#     else:pass
#     count=count+1
#     indxvalue=indxvalue+1
# print(string)


# 4-Requirement-->print lenght of the string without using len() function.
# through--for loop
# s=input("enter any string:")
# lenght=0
# for i in s:
#     lenght=lenght+1
# print("The Lenght of The Entered String is {}.".format(lenght))
# print("The Lenght of The Entered String is",lenght)

        
# 5-Requirement-->Each character how many times it is Representing.
# s=input("Enter Any String:")
# for i in s:
# 	count=0
# 	num=i
# 	while count<=len(s)-1:
# 		if i in num:
# 			num+=i
# 		else:pass
# 		count=count+1
# 		print("{} is representing {} times.".format(i,len(num)))   #Not Done.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


# s=input("enter some string:")
# for i in s:
# 	one_value=''
# 	val_count=i
# 	for y in s:
# 		if y in val_count:
# 			val_count=val_count+y
# 		elif y not in val_count:
# 			pass
# 	if len(val_count)>2:
# 		print("{} is representing {} times.".format(i,len(val_count)-1))
# 	else:
# 		print("{} is representing {} times.".format(i,len(val_count)-1))



# for i in s:
# 	val_count=''
# 	if i not in val_count:
# 		val_count=val_count+i
# 		for i in s:
# 			if i in val_count:
# 	for i in s:
# 		if i in val_count:
			




# changing the cases of string.		
# s=input("Enter Any String:")
# print(s.upper())
# print(s.title())
# print(s.swapcase())
# print(s.capitalize())
 


# 6-Requirement-->Count how many vowels are in a given string.
# s=input("Enter Any String:")
# l="AaEeIiOoUu"
# vowels=""
# for i in s:
#     if i in l:
#         vowels=vowels+i
#     else:pass
# print("There are {} vowels in the above provided string.".format(len(vowels)))


# 7-Requirement:Check whether a given string is a palindrome.
# s=input("Enter Any String:")
# reverse=""
# index=1
# for i in s:
#     reverse=reverse+s[len(s)-index]
#     index=index+1
# if reverse==s:
#     print("The String Is Palindrome.")
# else:
#     print("The String Is Not Palindrome.")


# 8 REQUIREMENT: Remove all spaces from a string.
# str=input('Enter multiworld string:')
# newstr=''
# for i in str:
#     if i.isalpha():
#         newstr=newstr+i
# print(newstr)     # issue in this program as is also removes other special character.
          # OR
# str=input('Enter multiword string:')
# newstr=''
# for i in str:
#     if i!=' ':
#         newstr=newstr+i
#     else:pass    
# print(newstr)      # issue of previous program resolved.


# 9 REQUIREMENT:Find the first and last character of a string.
# str=input("Enter string to find it's first and last world:")
# first_word=''
# last_word=''
# ind1=0
# ind2=-1
# while str[ind1]!=' ':
#     if str[ind1].isalpha():
#         first_word=first_word+str[ind1]
#     ind1+=1
# while str[ind2]!=' ':
#     if str[ind2].isalpha():
#         last_word=last_word+str[ind2]
#     ind2-=1
# print("The first word in given string is:",first_word)
# print("The last word in given string is:",last_word[::-1])

# 10 REQUIREMENT: Check if a string has all unique characters (no repeats), without using a set.
str=input('Enter some string:')
newstr=''
for i in str:
    if i not in newstr:
        newstr=newstr+i

    







    
    
        
# s="mississippi"
# s1="".join(dict.fromkeys(s))
# print(s1) 


	
	


























