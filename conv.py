import math
#base1 = input('enter the base of number:')
base2 = input('enter the conversion base:')
number = input('enter the number:')
x = []
def bintosome(stringconverted, base2):
    lentouse = log(base2, 2)
    lentouse = int(lentouse)
    somestring = stringconverted
    if len(stringconverted) % lentouse != 0:
        adjuststring(somestring, lentouse)
    else:
        stringparts = len(string)/lentouse
        bintodec(somestring)
        
def adjuststring(somestring, lentouse):
    temp = somestring
    temprev = "".join(reversed(somestring))
    number = ceil(len(temprev)/ lentouse)
    for i in range(number):
        temprev.append('0')
    temp = "".join(reversed(temprev))
    return bintosome(temp, base2)
    
def bintodec(stringtoconvert):
    newlength = len(stringtoconvert)
    numberoftimes = log(newlength, 2)
    lengthofbase = log(base2, 2)
    i = 0
    for i in range(numberoftimes):
        compile_string(stringtoconvert[i:i + lengthofbase])
    
def compile_string