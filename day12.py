scores = []
with open("scores.txt") as f:
     for line in f:
         line=line.strip()
         if line=="":
              continue      
         scores.append(int(line))      # ← 去掉 \n，再转成数字
print(scores)
print(type(scores))
# import os
# print("1. 当前工作目录:", os.getcwd())
# print("2. 这个目录里的文件:", os.listdir())
# print("3. scores.txt 存在吗:", os.path.exists("scores.txt"))
# if os.path.exists("scores.txt"):
#     print("4. 它有多大（字节）:", os.path.getsize("scores.txt"))
# with open("scores.txt") as f:
#     content = f.read()
# print("5. 读到的字符数:", len(content))
# print("6. 读到的真实内容:", repr(content))   
with open("scores.txt") as f:
    content = f.read()
print("文件原始内容的 repr:")
print(repr(content))
print("第一行:", repr(content.splitlines()[0]))
print("第一个元素的类型和值:", type(scores[0]), scores[0])