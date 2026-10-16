# words = ["the", "cat", "the", "dog", "the"]
# counts = {}
# for w in words:
#     if w in counts:
#         counts[w] += 1
#     else:
#         counts[w] = 1
# print("A:", counts)
words = ["the", "cat", "the", "dog", "the"]
for w in words:
    counts = {}
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1
print("B:", counts)