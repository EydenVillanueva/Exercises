def LongestCommonPrefix(array):

    if len(array) < 1:
        return ""
    if len(array) == 1:
        return array[0]

    word_compute = array.pop()
    store = ""

    for word in array:
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
