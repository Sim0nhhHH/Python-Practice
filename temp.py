s=int(input("你想做什么？1 - 摄氏转华氏 ,2 - 华氏转摄氏"))
if s==1:
    celsius=float(input("请输入摄氏度："))
    fahrenheit=(celsius*9/5+32)
    print(celsius,"摄氏度=",fahrenheit,"华氏度")
elif s==2:
    fahrenheit=float(input("请输入华氏度："))
    celsius=(fahrenheit-32)*5/9
    print(fahrenheit,"华氏度=",celsius,"摄氏度")
else:
    print("输入有误，请重新输入")





