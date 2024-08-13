def GCD(s, l):
    rem = 1
    tmp = 0
    while rem != 0:
        rem = l % s
        tmp = s
        s = rem
        l = tmp
    return l


print(GCD(66528, 52920))
