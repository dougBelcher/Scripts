# count_words


# def count_words(string):
#     return string.split(' ')

def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count




print(f'{count_words("Oh what a day what a lovely day")}')

