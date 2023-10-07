import random


def gcd(a, b):
    while True:
        if a % b == 0:
            return b

        remainder = a % b
        a = b
        b = remainder


def compute_e_inverse(a, b):  # d.e =_ 1(mod phi_n)
    num_book = []
    eval = []
    i = 0

    while True:
        num_sheet = [0, 0, 0, 0, 0]
        num_book.append(num_sheet)
        q = int(a/b)
        r = a % b
        num_book[i][0] = r
        num_book[i][1] = a
        num_book[i][2] = 1
        num_book[i][3] = b
        num_book[i][4] = -q
        a = b
        b = r
        eval = num_book[i]
        i += 1
        if r == 1:
            break

    while True:
        if i == 1:
            break
        i -= 1
        eval[1] = num_book[i-1][1]
        eval[3] = num_book[i-1][3]
        x = eval[2]
        eval[2] = eval[4] * num_book[i-1][2]
        eval[4] = x + eval[4] * num_book[i-1][4]

    d = eval[4]

    while True:
        if d < 0:
            d += num_book[0][1]
            continue
        return d % num_book[0][1]


p1 = int(input("enter prime 1 : "))
p2 = int(input("enter prime 2 : "))

n = p1*p2
phi_n = (p1-1)*(p2-1)

e = 2*3*5*7*11*13*17*19

while True:
    e = random.randint(2, phi_n-1)
    if (gcd(phi_n, e) == 1):
        break
    continue

print(" PUBLIC KEY : n = {} , e = {}".format(n, e))

dd = compute_e_inverse(phi_n, e)

print(" PRIVATE KEY : n = {} , d = {}".format(n, dd))
