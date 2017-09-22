def mirr(str):
    buf = ''
    c= len(str)
    for i in range(len(str)):
        buf += str[c-1]
        c -= 1
    return(buf)

str = 'Hii'
print(mirr(str))