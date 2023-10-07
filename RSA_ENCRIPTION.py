def giveval(x):
    return ord(x)


def encript(m, n, e):

    if e == 0:
        return 1
    if m == 1:
        return 1
    if e == 1:
        return m
    if e == 2:
        return (m*m) % n
    i = 1
    x = m
    while True:
        m = m*x
        i += 1
        if (m > n) or (i >= e):
            break
    E = int(e/i)
    left = e % i
    y = encript(m % n, n, E)
    y *= encript(x, n, left)
    return y % n


message = (input("enter plain text : "))

print("enter public key")
n = int(input("n : "))
e = int(input("e : "))

length = len(str(message))

m = 0
for i in range(length):
    m += (10**(i*3))*giveval(message[-(i+1)])

print("message in ascii : {}".format(m))
c = encript(m, n, e)

print("cipher : {}".format(c))
