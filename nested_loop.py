city=["LUCKNOW","MUMBAI","DELHI","JAIPUR"]
zones=["north","south","east","west"]
sr=1
# for c in city:
#      for z in zones:
#         print(z)

#      print(c)     

for c in city:
    print(sr,')',c,"city can be divided into-",end='')
    for z in zones:
        print(z,end=';')
    print()
    sr+=1    

# city=["lucknow","mumbai","delhi","jaipur"]
# for c in city:
#     print(c)
#     for c1 in city:
#         print(c1)


# for i in range(3):
#     for j in range(3):
#         print(i,j)

# listStudent = [[101,"sahil",24,"kareemganj"], [102,"sharif",29,"amberganj"],[103,"palik",50,"yaseenganj"]]
# for student in listStudent:
#     print(student)
#     for details in student:
#         print(details)

# i=0
# j=0
# a=0
# while i<len(listStudent):
#     while j<len(listStudent[a]):
#         print(listStudent[i][j],end=' ')
#         j+=1
#     i+=1
#     a+=1 
#     j=0   
#     print()







