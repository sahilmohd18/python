# Converting one DT to other-->>Functions--int(),float(),complex(),boolean(),str()

#int()--converting other DT to int DT (yes-float,boolean,str(str value must be number with base 10) ;No-complex)
# print(int(12.6))
# print(int(True))
# print(int("120"))

#float()--converting other DT to float DT (yes-int,boolean,str(for int and float str value and not words) ;No-complex)
# print(float(10))
# print(float(True))
# print(float("10"))
# print(float("10.5"))
# print(float("twenty"))

#complex()--converting other DT to complex DT (yes-boolean,number(int-any base,float-decimal base),No-str)
# print(complex(10))
# print(complex(10,15))
# print(complex(123,100))
# print(complex(10.5,10))
# print(complex(10.5,12.3))
# print(complex(0b10,12.3))
# print(complex(True,False))

#boolean()--converting other DT to boolean DT
# print(bool(10))
# print(bool(0)) #int--> 0-false,non zero true
# print(bool(10.0))
# print(bool(0.0)) #float-->total is zero-false,else true
# print(bool(1+0j))
# print(bool(0+0j)) #complex-->both R and I are 0-false , if any one is non zero then -true
# print(bool("2"))
# print(bool("")) #str-->empty str-false, non empty str-true


#str()--no restriction(any to any)
print(str(1))
print(str(0b10))
print(str(0x10))
print(str(10.5))
print(str(True))
print(str(10+20j))
print(str(1))















