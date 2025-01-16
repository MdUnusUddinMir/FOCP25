# 2.2: Letters in both words
def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))

word1 = "boat"
word2 = "raft"
print(letters_in_both(word1, word2)) 