#Medium
def dailyTemps(temps):
    if not temps:
        return []

    cont, cont_days = 0,1
    result = []
    cont2 = 0

    for item in temps:
        compare = temps[cont]
        for i in range(cont,len(temps)):
            if temps[i] > compare:
                result.append(cont_days)
                break
            elif temps[i] <= compare and i == len(temps)-1:
                result.append(0)
                break
            if i != 0:
                cont_days+=1
        cont+=1
        cont_days = 0

    return result

if __name__ == "__main__":
    print(dailyTemps([73, 74, 75, 71, 69, 72, 76, 73])) #[1, 1, 4, 2, 1, 1, 0, 0]
