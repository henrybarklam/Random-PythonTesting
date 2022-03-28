def divCalculator(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        val1, val2, val3 = divCalculator(b % a, a)
        return val1, val3-(b//a) * val2, val2
def modinv(a, m):
    g, x, y = divCalculator(a, m)
    if g != 1:
        print('modInv dne')
    else:
        return x % m
def invFinder(s,p,q):
    d = s%((p-1)*(q-1))
    return d
def rsaBreaker(b,d,N):
    return ((b**d))%N
#From question
p = 101
q = 113
N = p*q
c = 7653
b = 3233
x = modinv(c,N)
d = invFinder(x,p,q)
print("Question 4b")
print("d = " + str(d))
val = rsaBreaker(b,d,N)
b = (val**c)%(p*q)
print("\nQuestion 4c")
print("a = " + str((b**d)%N))