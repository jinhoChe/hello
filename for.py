import random
for i in range(50):
    print(i)
    print(f'{i+1}.hello world')
    print('짜장면이냐 짬뽕이냐?')
    a =input
    print(f'니가 입력한 값: {a}')
    menu = '짜장' , '짬뽕'
    if a =='짜장' or a == '짬뽕':
        print('나오나? 나오면 True') 
    print('인공지능이 추천 해주는 결과는?')
    m = random.choice(menu)
    print(f"{m} 먹어!!")
else:
    print('짬짜면 먹어!!')
    print('1 .hello world')
    print('2 .hello world')
    print('hello world')
    print('hello world')
