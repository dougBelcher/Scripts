# When solving this week's exercise, don't look back at your previous answers and avoid searching on the Internet until you get to the bonus. I'd like to make sure you struggle on this one. See if you can think up at least a couple different ways to solve it.
#
# I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.
#
# Your function should work like this:
#
# >>> is_anagram("tea", "eat")
# True
# >>> is_anagram("tea", "treat")
# False
# >>> is_anagram("sinks", "skin")
# False
# >>> is_anagram("Listen", "silent")
# True
# Make sure your function works with mixed case.
def is_anagram(first, next_one):
    items = [1, 2, 3, 4, 2, 1]
    for i, (first, last) in enumerate(zip(items, reversed(items))):
        if first != last:
            raise ValueError(f"Item {i} doesn't match: {first} != {last}")

if __name__ == "__main__":
    first = input('first: ')
    next_one = input('next: ')
    is_anagram(first, next_one)
