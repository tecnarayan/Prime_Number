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


c_main = (input("enter cipher text : "))

print("plain text : ", end="")

for z in range(int(len(c_main)/16)):
    c = c_main[16*z+0] + c_main[16*z+1] + c_main[16*z+2] + c_main[16*z+3] + c_main[16*z+4] + c_main[16*z+5] + c_main[16*z+6] + c_main[16*z+7] + \
        c_main[16*z+8] + c_main[16*z+9] + c_main[16*z+10] + c_main[16*z+11] + \
        c_main[16*z+12] + c_main[16*z+13] + c_main[16*z+14] + c_main[16*z+15]
    c = int(c)
    m = decrypt(c, 1903458872013011, 1252263165993733)

    length = len(str(m))

    m = str(m)

    if length % 3 == 1:
        m = "00" + m
        length += 2

    if length % 3 == 2:
        m = "0" + m
        length += 1

    length = int(length/3)

    for i in range(length):
        s = m[3*i] + m[3*i+1] + m[3*i+2]
        new_s = int(s)
        new_char = givechar(new_s)
        print(new_char, end="")
