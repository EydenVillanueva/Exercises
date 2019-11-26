def last_word_lenght(s):
    if s:
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1 

        array = s.split(" ")
        cadena = []

        for a,i in enumerate(array):
            if i != '':
                cadena.append(i)

        return cadena[-1]
    else:
        return 0


last_word_lenght("        ")


'''
        if s:
            words = s.split(' ')
            if len(words) == 0:
                return 0
            elif len(words) == 1:
                return 1
            else:
                while words[-1] == "":
                    del words[-1]
                return len(words[-1])
        else:
            return 0
'''