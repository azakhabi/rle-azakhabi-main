def encode(string):
    if string == '':
        return(string)
    else:
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

def decode(string):
    if string == '':
        return(string)
    else:
        l = len(string)
        h = ''
        m = ''
        if string[0].isalpha() == True:
            h += string[0]
        for i in range(l - 1):
            if string[i].isdigit() == True:
                m += string[i]
            if string[i].isdigit() == True and (string[i + 1].isalpha() == True or string[i + 1] == ' '):
                h += string[i + 1] * int(m)
                m = ''
            if string[i].isdigit() == False and string[i + 1].isdigit() == False:
                h += string[i + 1]
        return (h)