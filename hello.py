import random
chouma = 10000
jixu = 1
ercixunhuan = 0
i = 1
while jixu == 1:
    if chouma == 0:
        print('您已经输光啦')
    else:(f'您拥有{chouma}元')
    a = int(input('请下注：'))
    while int(a) > int(chouma):
        print('余额不足，请重新下注')
        a = int(input(''))
    print('下注成功')
    math1 = random.randrange(1,7)
    math2 = random.randrange(1,7)
    first = math1 + math2
    print(f'骰子数为{first}')
    if first in [7,11]:
        print(f'win,您获得了{a}元')
        chouma += a
    elif first in (2,3,12):
        print(f'您失去了{a}元')
        chouma -= a
    else: print('再投一次吧');ercixunhuan = 1
    while ercixunhuan == 1:
            i += 1
            second = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'第{i}次骰子数为{second}')
            if second == 7:
                print(f'您失去了{a}元')
                chouma -= a
                ercixunhuan = 0
            elif second == math1 + math2:
                print(f'win,您获得了{a}元')
                chouma += a
                ercixunhuan = 0
            else: ercixunhuan = 1;print('请再投一次')
    print(f'您的余额为{chouma},按回车继续，按e键加回车键结束')
    b = input('')
    if b == 'e':
        jixu = 0;print('您的余额将归零，期待下次再见')
    else: jixu = 1