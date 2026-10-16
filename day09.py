sentence = "the cat and the dog and the bird and the fish"
words = sentence.split()
counts = {}
for n in words:          # ← 遍历单词列表
    if n in counts:     # ← 这个词以前见过吗？
        counts[n] +=1   #过：次数 +1
    else:
        counts[n]=1         # ← 没见过：记成 1 次
num=len(counts)
for word, n in counts.items():
    print(f"{word}: {n} 次")
print(num)