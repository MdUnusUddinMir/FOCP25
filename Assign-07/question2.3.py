# Task 2.3: Letters in either word, but not both
def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))
word1 = "boat"
word2 = "raft"
print(letters_in_either_but_not_both(word1, word2)) 