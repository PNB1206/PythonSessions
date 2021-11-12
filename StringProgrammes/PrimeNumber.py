
""" Finding prime numbers """
def isPrime(n1, n2):
    for n in range(n1, n2 + 1):
        if n >1:
            for num in range(2, n):
                if n%num == 0:
                    break
            else:
                print(n, end=' ')

isPrime(0, 100)
print("")

def isPrime2(a,b):
    for i in range(a, b+1):
        if i >1:
            for num in range(2,i):
                if i%num == 0:
                    break
            else:
                print(i, end=" ")

isPrime2(20,40)

print(' ')
def is_list_prime(num):
    for i in num:
        if i >1:
            for j in range(2,i):
                if i%j ==0:
                    break
            else:
                print(i, end=' ')


is_list_prime([1,2,3,4,5,6,7,8,9,10])

