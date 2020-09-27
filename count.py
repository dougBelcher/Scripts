def count(word, alpha):
    count = 0
    for letter in word:
        if letter == alpha:
            count += 1
    return count
