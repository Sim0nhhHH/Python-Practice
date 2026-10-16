# 错误 1：漏右括号
#print("hello"
# 错误 2：用中文引号
#print(“hello”)
# 错误 3：变量名以数字开头
#2x = 5
# 错误 4：没定义的变量
#print(score)
# 错误 5：类型不对
#print("我今年" + 18 + "岁")
scores = [88, 92, 75]
total = 0
for s in scores:
    total = total + s
    print("这一轮：s =", s, "，total =", total)
print("最终：", total)