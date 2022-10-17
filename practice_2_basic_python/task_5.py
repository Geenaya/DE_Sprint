#5. Умножить два бинарных числа в формате строк

def mult(a, b):
    na, nb = len(a), len(b)
    res = [False] * (na+nb)
    b = [True if d == '1' else False for d in b[::-1]]
    a = [True if d == '1' else False for d in a[::-1]]
    
    for i in range(nb):
        if b[i]:
            t = False
            for j in range(na):
                res[i+j], t = res[i+j]^a[j]^t, (res[i+j]+a[j]+t) > 1
            res[i+j+1] = t 
    tmp = ['1' if d else '0' for d in res[::-1]]
    return ''.join(tmp).lstrip('0')
    
 
x1 = '111' 
x2 = '101'

print(mult(x1, x2))
print(int(mult(x1, x2),2))