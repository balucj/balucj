data = [['','one','two','three','four','five','six','seven','eight','nine','ten'],
       ['elengthven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty'],
       ['ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety','hundred'],
       ['thousand','lach','crore']]

def lget(v,x):
    return int(str(v)[x])

def once(x):
    ans = ' ' 
    ans += data[0][x]
    return ans

def teen(x):
    ans = ' '
    ans += data[1][int(str(x)[-1])-1]
    return ans

def tens(x):
    ans = ' '
    ans += data[2][int(str(x)[-2])-1]
    return ans

def hundreds(x):
    if lget(x,-3) != 0:
        ans = ''
        ans += once(lget(x,-3))
        ans += ' '
        ans += data[2][-1]
        return ans
    else: 
        return ''

def thousands(x):
    ans = ' '
    ans += once(lget(x,-4))
    ans += ' '
    ans += data[3][0]
    return ans

def tthousands(x):
    ans = '' 
    if int(str(x)[-5:-3]) < 20 and int(str(x)[-5:-3]) != 10:
        ans += teen(int(str(x)[-5:-3]))
        ans += data[3][0]
    else:    
        ans += tens(int(str(x)[-5:-3]))
        ans += once(lget(x,-4))
        ans += ''
        ans += data[3][0]
    ans += ' '
    return ans

def lach(x):
    ans = ''
    ans += once(lget(x,-6))
    ans += ' '
    ans += data[3][1]
    return ans

def tlach(x):
    ans = ''
    fc = int(str(x)[-7:-5])
    if fc < 20 and fc != 10:
        ans += teen(fc)
        ans += ' '
        ans += data[3][1]
    else:
        ans += tens(fc)
        ans += once(lget(x,-6))
        ans += ' '
        ans += data[3][1]
    return ans

def crore(x):
    ans = ''
    fc = int(str(x)[0])
    if fc < 10:
        ans += once(fc)
        ans += ' '
        ans += data[3][2]
    return ans


def l1(val):
    return once(val)

def l2(val):
    if val == 0:
        return ''
    elif val < 20 and val !=10:
        return teen(val)
    else:
        return tens(val) + once(lget(val,-1))
def l3(val):
    if val == 0:
        return ''
    elif val % 100 == 0:
        return hundreds(val)
    else:
        if int(str(val)[-2:]) < 10:
            return hundreds(val) + ' and' + l1(int(str(val)[-1])) 
        else: 
            return hundreds(val) + ' and' +l2(int(str(val)[-2:]))
def l4(val):
    if val == 0:
        return ''
    elif val % 1000 == 0:
        return thousands(val)
    else:
        ch = int(str(val)[-3:])
        if ch < 10:
            return thousands(val) + l1(ch)
        elif ch < 100:
            return thousands(val) + l2(ch)
        else:
            return thousands(val) + l3(ch)

def l5(val):
    if val % 10000 == 0:
        return tthousands(val)
    else:
        ch = int(str(val)[-4:]) 
        if ch < 10:
            return tthousands(val) + l1(ch)
        elif ch < 100:
            return tthousands(val) + l2(ch)
        else:
            return tthousands(val) + l3(ch)


def l6(val):
   if val % 100000 == 0:
       return lach(val)
   else:
       ch = int(str(val)[-5:])
       if ch < 10:
           return lach(val) + l1(ch)
       elif ch <100:
           return lach(val) + l2(ch)
       elif ch < 1000:
           return lach(val) + l3(ch)
       elif ch < 10000:
           return lach(val) + l4(ch)
       else:
           return lach(val) + l5(ch)
 
def l7(val):
    if val % 1000000 == 0:
        return tlach(val)
    else:
        ch = int(str(val)[-6:])
        if ch < 10:
            return tlach(val) + l1(ch)
        elif ch<100:
            return tlach(val) + l2(ch)
        elif ch <1000:
            return tlach(val) + l3(ch)
        elif ch < 10000:
            return tlach(val) + l4(ch)
        else:
            return tlach(val) + l5(ch)
def l8(val):
    if val % 10000000 == 0:
        return crore(val)
    else:
        ch = int(str(val)[-7:])
        if ch < 10:
            return crore(val) + l1(ch)
        elif ch < 100:
            return crore(val) + l2(ch)
        elif ch < 1000:
            return crore(val) + l3(ch)
        elif ch < 10000:
            return crore(val) + l4(ch)
        elif ch < 100000:
            return crore(val) + l5(ch)
        elif ch < 1000000:
            return crore(val) + l6(ch)
        else:
            return crore(val) + l7(ch)

def div(v):
    length = int(len(str(v)))
    res = ''
    aa = int(str(v)[-1])
    if length == 1:
        res += l1(v)
    elif length == 2:
        res += l2(v)
    elif length == 3:
        res += l3(v)
    elif length == 4:
        res += l4(v)
    elif length == 5:
        res += l5(v)
    elif length == 6:
        res += l6(v)
    elif length == 7:
        res += l7(v)
    elif length == 8:
        res += l8(v)
    return res
    

while True:
    print("""Enter 'x' or 'X' to exit: """)
    print("""The number must be greater than 0 and lengthss than 10 crore:""")
    inp = input("Enter a number: ")

    if inp == 'x' or inp == 'X':
        break
    
    try:
        i = int(inp)
    except (TypeError,ValueError):
        print("Please Enter a valid number")
        continue
    print(div(i).title())
    print()
    print()
