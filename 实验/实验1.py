#导入随机工具包
import random
wanjia1=int(input("剪(1)石(2)布(3)输入你的本次出手："))
sjs=random.randint(1,3)
if(wanjia1==1):
    chushou1="剪刀"
elif(wanjia1==2):
    chushou1="石头"
elif(wanjia1==3):
    chushou1="布"

if(sjs==1):
    diannao="剪刀"
elif(sjs==2):
    diannao="石头"
elif(sjs==3):
    diannao="布"

print("你选择出【%s】,对方使用了【%s】应对！"%(chushou1,diannao))
if((wanjia1==1 and sjs==3)
        or(wanjia1==2 and sjs==1)
        or(wanjia1==3 and sjs==2)):
    print("赢了，电脑辣鸡！")
elif(wanjia1==sjs):
    print("势均力敌！下次定要赢你！")
else:
    print("mmp，居然输给电脑！")