#medium
def keyRooms(rooms):
    seen = [False] * len(rooms)
    seen[0] = True
    stack = [0]

    while stack: 
        node = stack.pop() 
        for nei in rooms[node]:
            if not seen[nei]:
                seen[nei] = True
                stack.append(nei)
    return all(seen)

if __name__ == "__main__":
    print(keyRooms([[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]])) #False