
from shlex import join

# 1. Reverse string using slice operator
def reverse_string_using_slice():
    name = "Chanti Babu"
    output = name[::-1]
    print("reverse string is: ", output)

def reverse_string_slice_get_from_cosole():
    name = input('Enter some string to reverse: ')
    output = name[: : -1]
    print(output)

#reverse_string_using_slice()
#reverse_string_slice_get_from_cosole()


"""Reverse string uding revesed()"""
s="New Python world"
r=reversed(s)
output = ''.join(r)
#print(output)


"""Reverse string using while loop"""
str1 = 'Pyhton'
output1 = ''
i = len(str1)-1
while i >= 0:
    output1 =output1 + str1[i]
    i = i-1
#print('reverse using while loop: ',  output1)


""" Reverse the order of words in a string """
def reverse_order_of_words_string():
    s= 'Learning Python is very easy'
    l=s.split()
    rev_list = l[: :-1]
    outPut =join(rev_list)
    print(outPut)

#reverse_order_of_words_string()

def reverse_order_of_words_string2():
    s= 'Learning Python is very easy'
    l = s.split()
    r =s[: : -1]
    print(r)

#reverse_order_of_words_string2()


"""Reverse the internal content of words in a string"""
def reverse_internal_contentofword():
    s="Lord is my Sheaperd"
    l=s.split()
    l1=[]
    for words in l:
        l1.append(words[::-1])
    print(' '.join(l1))

#reverse_internal_contentofword()



"""  Reverse the internal content of 2nd  word in a string """
def reverse_internal_contentofword_using_while_loop():
    s= "Jesus is my shepherd"
    l = s.split()
    l1 = []
    i = 0
    while i < len(l):
        if i%2 == 0:
            l1.append(l[i])
        else:
            l1.append(l[i][::-1])
        i = i+1
    output = ' '.join(l1)
    print(output)

reverse_internal_contentofword_using_while_loop()



