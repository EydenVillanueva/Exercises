def spaceArray(queries):
    dic = {}
    base = ["aba","baba","aba","xzxb"]
    result = []

    for i in base:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for q in queries:
        if q in dic:
            result.append(dic[q])
        else:
            result.append(0)

    return result

print(spaceArray(["xzxb","aba","ab"]))