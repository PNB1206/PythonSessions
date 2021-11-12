#
# s= input("Enter some string ")
# output =''
# for ch in s:
#     if ch.isalpha():
#         output = output + ch
#         x = ch
#     else:
#         d = int(ch)
#         newCh = chr(ord(x)+d)
#         output = output + newCh
# print(output)

def fibonacci(x):
    a,b =0,1
    c=0
    while a <=x:
        print(a, end=' ')
        a,b =b,a+b



fibonacci(15)
print("")

def fibonacci2(numm):
    a,b =0,1
    while a<=numm:
        print(a,end=' ')
        a,b=b,a+b

fibonacci2(25)


