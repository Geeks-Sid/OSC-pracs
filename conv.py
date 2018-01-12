import math
#base1 = input('enter the base of number:')
base2 = int(input('enter the conversion base:'))
number = input('enter the number:')
biggest = []
def bintosome(stringconverted, base2):
    print('inside bin_to_some')
    lentouse = math.ceil(math.log(base2, 2))
    lentouse = int(lentouse)
    print('len_to_use:', lentouse)
    somestring = stringconverted
    print('String to be worked on:', somestring)
    print('Length of this some string:', len(stringconverted))
    if len(stringconverted) % lentouse != 0:
        print('Going to adjust this string.')
        adjuststring(somestring, lentouse)
    else:
        #stringparts = len(string)/lentouse
        print('The length of string was just fine.')
        bintodec(somestring, base2)
        
def adjuststring(somestring, lentouse):
    print('saving string for temporary use:', somestring)
    temp = somestring
    print('Reversing the string...')
    temprev = "".join(reversed(somestring))
    print('Reversed string looks like this:', temprev)
    if len(temprev) < lentouse:
        print('string was smaller')
        print('Gonna append these many times:', lentouse-len(temprev))
        for i in range(lentouse - len(temprev)):
            temprev = temprev + '0'
    else:
        number = math.ceil(len(temprev)//lentouse)
        print('Gonna append these many times:', number)
        for i in range(number):
            temprev = temprev + '0'
    temp = "".join(reversed(temprev))
    print('The new string looks like this:', temp)
    return bintosome(temp, base2)
    
def bintodec(stringtoconvert, base2):
    print('Converting string right now!', stringtoconvert)
    newlength = len(stringtoconvert)
    print('Length of this new string is', newlength)
    lengthofbase = math.ceil(math.log(base2, 2))
    numberoftimes = math.ceil(math.log(newlength, lengthofbase))
    print('We have these many number of segments', numberoftimes)
    print('segment length we gotta cover is', lengthofbase)
    i = 0
    for _ in range(numberoftimes):
        biggest.append(compile_string(stringtoconvert[i:i + lengthofbase]))
        i += lengthofbase

def compile_string(x):
    print('String received',x)
    c = int(x)
    temp = 0
    value = 0
    for i in range(len(x)):
        temp = c%10
        print(c, temp, value)
        c = int(c/10)
        value += (2**i) * temp
    print('value of string :', value)
    return value

bintosome(number, base2)
biggest = biggest[::-1]
ans = 0
for p in range(len(biggest)):
    ans += (base2**p) * biggest[p]
print('Final Answer:', ans)