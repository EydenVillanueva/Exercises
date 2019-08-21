from StacksQueues.Stack import Stack

def minAdd(s):
    if not s:
        return 0
    
    cont,pila = 0,Stack()

    for c in s:
        if c == "(":
            pila.push(")")
        elif pila.peak() == c:
            pila.pop()
        elif c == ")" and pila.peak() != c:
            cont+=1

    return pila.size() + cont



if __name__ == "__main__":
    print(minAdd("())"))
    print(minAdd("((("))
    print(minAdd("()"))
    print(minAdd("()))(("))