def giveval(x):
    return ord(x)


def encrypt(m, n, e):

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
    y = encrypt(m % n, n, E)
    y *= encrypt(x, n, left)
    return y % n


letter = input("plain text : ")

l_length = len(letter)

main_length = int(l_length / 5)
sub_length = l_length % 5

cipher = ""

for i in range(main_length):
    s = letter[5*i] + letter[5*i+1] + \
        letter[5*i+2] + letter[5*i+3] + letter[5*i+4]

    m = 0
    for k in range(5):
        m += (10**(k*3))*giveval(s[-(k+1)])
    c = encrypt(m, 1903458872013011, 1395536392686061)
    c = str(c)
    temp_l = len(c)
    for j in range(16 - temp_l):
        c = "0" + c
    cipher += c

if sub_length != 0:
    min_m = 0
    for i in range(sub_length):
        min_m += (10**(i*3))*giveval(letter[-(i+1)])
    cc = encrypt(min_m, 1903458872013011, 1395536392686061)
    cc = str(cc)
    temp_lm = len(cc)
    for j in range(16 - temp_lm):
        cc = "0" + cc
    cipher += cc

print(cipher)
