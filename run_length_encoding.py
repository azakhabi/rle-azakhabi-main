def decode(string):
    x = ""
    k = 1
    l1 = len(string)
    for i in range(l1 - 1):
        if string[i] == string[i + 1]:
            k += 1
        else:
            if k != 1:
                x += str(k)
                x += string[i]
            elif k == 1:
                x += string[i]
            k = 1
    if string[l1 - 2] != string[l1 - 1]:
        x += string[l1 - 1]
    else:
        x += str(k)
        x += string[i]
    return (x)
def encode(string):
    l = len(string)
    h = ''
    m = ''
    if string[0].isalpha() == True:
        h += string[1]
    for i in range(l - 1):
        if string[i].isalpha() == False:
            m += string[i]
        if string[i].isalpha() == False and string[i + 1].islapha() == True:
            h += string[i + 1] * int(m)
            m = ''
        if string[i].isalpha() == True and string[i + 1].isalpha() == True:
            h += string[i + 1]
    return (h)