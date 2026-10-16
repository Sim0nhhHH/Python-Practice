def get_average(nums):
    num=len(nums)
    total=0
    for n in nums:
        total +=n
    average=total/num
    return(average)
def get_max(scores):
    max_score=scores[0]
    i=0
    while i<len(scores):
        if max_score<scores[i]:
            max_score=scores[i]
        i +=1
    return(max_score)
def get_min(scores):    
    min_score=scores[0]
    i=0
    while i<len(scores):
        if min_score>scores[i]:
            min_score=scores[i]
        i +=1
    return(min_score)
def count_grades(scores):
    ex=0
    gr=0
    pa=0
    fa=0
    exp=0
    grp=0
    pap=0
    fap=0
    for a in scores:
        if a>=90:
                ex += 1
        elif a>=80:
                gr += 1
        elif a>=60:
                pa += 1
        else: 
                fa += 1   
    num=len(scores)
    exp=(ex/num*100)
    grp=(gr/num*100)
    pap=(pa/num*100)
    fap=(fa/num*100)
    return(ex,gr,pa,fa,exp,grp,pap,fap) 
scores=[]
with open("scores.txt") as f:
     for line in f:
          scores.append(int(line.strip()))
avg = get_average(scores)
mx  = get_max(scores)
mn  = get_min(scores) 
ex,gr,pa,fa,exp,grp,pap,fap= count_grades(scores)
print(f"平均分:{avg:.2f}")
print(f"最高分:{mx}")
print(f"最低分:{mn}")
print(f"优秀:{ex} {exp:.1f}%")
print(f"良好:{gr} {grp:.1f}%")
print(f"及格:{pa} {pap:.1f}%")
print(f"不及格:{fa} {fap:.1f}%")
# scores = [88,92,79,60,45,100]
# num = len(scores)       
# total=0
# for s in scores:
#     total +=s
# max_score=scores[0]
# min_score=scores[0]
# ex=0
# gr=0
# pa=0
# fa=0
# average=total/num
# for i in scores:
#     if i>=max_score:
#         max_score =i
# for m in scores:
#     if m<=min_score:
#         min_score =m       
# for a in scores:
#     if a>=90:
#         ex += 1
#     elif a>=80:
#         gr += 1
#     elif a>=60:
#         pa += 1
#     else: 
#         fa += 1    
# exp=(ex/num*100)
# grp=(gr/num*100)
# pap=(pa/num*100)
# fap=(fa/num*100)
#print("平均分：",average,"最高分:",max_score,"最低分:",min_score,"优秀:",ex,exp,"%","良好:",gr,grp,"%","及格:",pa,pap,"%","不及格:",fa,fap,"%")
# 在 stats.py 最后加一行