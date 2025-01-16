#  2.1: Letters in at least one of the two words
def letters_in_at_least_one(word1, word2):
    return sorted(set(word1) | set(word2))
word1 = "boat"
word2 = "raft"
print(letters_in_at_least_one(word1, word2)) 