def LongestCommonPrefix(strs):

    if len(strs) < 1:
        return ""
    if len(strs) == 1:
        return strs[0]

    word_compute = strs.pop()
    store = ""

    for word in strs:
        small = len(word) if (word < word_compute) else len(word_compute)
        for i in range(small):
            if word[i].lower() == word_compute[i].lower():
                store += word[i]
            else:
                break
        word_compute = store
        store = ""
    return word_compute


obj = LongestCommonPrefix(["carrot"])
