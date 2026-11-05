# 函数的定义
def add(a,b):
    return a+b

def is_pass(score):
    return score >= 60

name = "康康"
age = 38
skills = ["功能测试","Linux","AI应用基础"]
profiles ={"name":"kangkang","age":age,"city":"北京"}

scores = [89,98,40,60,70]
passed = 0
for i in scores:
    if is_pass(i):
        passed += 1

print(f"及格人数：,{passed}")

for k,v in profiles.items():
    print(k,"=",v)

double =[x *2 for x in scores]
print(double)

def average(scores):
    total = 0
    for i in scores:
        total += 1
    return round(total / len(scores),1)

print(average(scores))

def average
