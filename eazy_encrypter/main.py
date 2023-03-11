import random

def new_pin(is_print: bool = False):
    '''Function create pin.\n
    If get True: print generated pin\n
    If get Falce: willn`t print generated pin'''
    if is_print == True:
        pin = random.randint(1000, 9999)
        print(pin)
    else:
        pin = random.randint(1000, 9999)
    return pin

def coder(txt: str, pin: int = 0, lit_len: int = 5):
    '''Function create from text code\n
    txt - Text\n
    pin - Pin-code(standart - 0)(max = 9999)\n
    lit_len - len for one literal(standart - 5)\n
    return coded str'''
    resu = []
    textList = list(txt)
    for let in textList:
        cod_let = ord(let)
        cod_let += pin
        numoflet = lit_len - len(str(cod_let))
        res = numoflet*"0" + str(cod_let)
        resu.append(res)
    result = "|".join(resu)
    return result

def de_coder(code: str, pin: int = 0):
    '''Function create from text code\n
    code - Text\n
    pin - Pin-code(standart - 0)(max = 9999, min = 0)\n
    return decoded str'''
    res = []
    mas_code = code.split("|")
    for codlet in mas_code:
        let1 = int(codlet) - pin
        res.append(chr(let1))
    result = ''.join(res)
    return result