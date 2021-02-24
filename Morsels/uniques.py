# uniques)_only - I want you to write a function that accepts an iterable and returns a
# new iterable with all items from the original iterable except for duplicates.

def uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed."""
    seen = set()
    items = []
    for item in iterable:
        if item not in seen:
            items.append(item)
            seen.add(item)
    return items

# Python 3.6+ - not real clear but it should work
# def uniques_only(iterable):
#     """Return iterable in the same order but with duplicates removed."""
#     return dict.fromkeys(iterable).keys()

# Bonus #1
# def uniques_only(iterable):
#     seen = set()
#     for item in iterable:
#         if item not in seen:
#             yield item
#             seen.add(item)

# Bonus #2
# def uniques_only(iterable):
#     seen = []
#     for item in iterable:
#         if item not in seen:
#             yield item
#             seen.append(item)

