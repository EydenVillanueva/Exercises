#Medium
def is_diferent(n):
    if n != '[' and n != ']':
        return True
    return False


def decode_string(encode):

    f_open = False
    c_aux,result,c_mult = '','',''

    for item in encode:
        if item.isdigit():
            c_mult += item
        if f_open and is_diferent(item):
            c_aux+= item
        if not (f_open) and c_aux != '' or item == ']':
            result += int(c_mult) * str(c_aux)
            c_mult, c_aux = '',''
            f_open = False
        if (not (f_open) and not (item.isdigit()) and is_diferent(item)):
            result+= item
        if item == '[':
            f_open = True
            
    
    return result


if __name__ == "__main__":
    print(decode_string('3[ab]0[c]1[e]'))