


def rev_num(n):
    r = str(n)
    n =r[: :-1]
    print(int(n))
rev_num(54321)

def revNum_whille_loop(num, rev):
    while num > 0:
        reminder = num%10
        rev = (rev*10)+reminder
        num = num // 10
    print(rev)


revNum_whille_loop(12345, 0)
