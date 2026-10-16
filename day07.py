names  = ["张三", "李四", "王五", "赵六"]
scores = [92, 45, 88, 92]
i1=0
i2=1
max_name=[names[0]]
max_score=scores[0]
while i1<len(names):
    print(names[i1],":",scores[i1])
    i1 +=1
while i2<len(names):
    if max_score<scores[i2]:
        max_score=scores[i2]
        max_name=[names[i2]]
    elif max_score==scores[i2]:
        max_name.append(names[i2])
    i2 +=1   
print(max_score,max_name)
