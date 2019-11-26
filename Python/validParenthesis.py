from StacksQueues.Stack import Stack

def isValid(s):
    if not(s):
        return False
    registro = Stack()
    for c in s:
        if c == '(':
            registro.push(')')
        elif c == '[':
            registro.push(']')
        elif c == '{':
            registro.push('}')
        elif c != registro.pop():
            return False
    if registro.size() == 0:
        return True
    return False
    
    


if __name__ == "__main__":
    print(isValid('()'))
    print(isValid('([])'))
    print(isValid('([]())'))
    print(isValid('([]()'))