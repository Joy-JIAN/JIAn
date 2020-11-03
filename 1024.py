import sys
num= int(sys.argv[1])
if isinstance(num,(int)):
    if num<100:
        print("wrong,please input numbem,the number should be integer and greater than 100.")
    else:
        print("binary system:", bin(num))
        print("octonary system:",oct(num))
        print("hexadecimal system:",hex(num))
else:
        print("wrong,please input numbem,the number should be integer and greater than 100.")
