def givechar(x):
    return chr(x)


def decrypt(c, n, d):

    if d == 0:
        return 1
    if c == 1:
        return 1
    if d == 1:
        return c
    if d == 2:
        return (c*c) % n
    i = 1
    x = c
    while True:
        c = c*x
        i += 1
        if (c > n) or i >= d:
            break
    D = int(d/i)
    left = d % i
    y = decrypt(c % n, n, D)
    y *= decrypt(x, n, left)
    return y % n


c = int(input("enter cipher text : "))

print("enter private key")
n = int(input("n : "))
d = int(input("d : "))

m = decrypt(c, n, d)

print(" message in ascii : {}".format(m))
length = len(str(m))

m = str(m)

if length % 3 == 1:
    m = "00" + m
    length += 2

if length % 3 == 2:
    m = "0" + m
    length += 1

length = int(length/3)

print("plain text : ", end="")

for i in range(length):
    s = m[3*i] + m[3*i+1] + m[3*i+2]
    new_s = int(s)
    new_char = givechar(new_s)
    print(new_char, end="")
