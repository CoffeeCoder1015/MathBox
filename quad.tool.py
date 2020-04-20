import math
import f_opt

ans = None
def solve(a,b,c):
    global ans
    x = ["plus :","minus:"]
    
    sqrt_block = ( b**2 - (4*a*c) )**(1/2)
    denom = 2*a
    p=(-b + sqrt_block ) / denom
    m=(-b - sqrt_block ) / denom
    pf="%s / %s"%((-b + sqrt_block),denom)
    mf="%s / %s"%((-b - sqrt_block),denom)
    x.insert(1,p)
    x.insert(2,pf)
    x.insert(4,m)
    x.insert(5,mf)
    
    ans = x

def calc(var):
    num = str(var)
    num=num.replace("pi",str(math.pi))
    num=num.replace("e",str(math.e))
    num = eval(num)
    return num

while True:
    Nums = input("Variable input:").split()
    Nums = [calc(i) for i in Nums]
    solve(Nums[0],Nums[1],Nums[2])
    for i in ans:
        print(i)
    print("------------------------------")
