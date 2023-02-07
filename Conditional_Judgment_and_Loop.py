#取出list的index/value
languages = ['Java', 'C', 'Python']
for index,value in enumerate(languages):
    print(index,value)
'''
0 Java
1 C
2 Python
'''

#取出dict的key/value
language_ranking_dict={
    'Java':12,
    'Python':1,
}
for key,value in language_ranking_dict.items():
    print(key,value)
'''
Java 12
Python 1
'''

#HW5
'''
根據猜數字遊戲規則撰寫一個 Python 猜數字遊戲程式。
請先設定一個解答當作解答
讓使用者可以輸入是否要玩：請問你想跟我玩猜數字遊戲嗎？（選 1 要玩，選 0 結束）
若選擇不玩結束則印出遊戲結束字串，若要則邀請使用者輸入數字進行判斷（考考你猜數字遊戲，請輸入一個數字）
若使用者輸入的數字小於該數字則印出：答案比較大喔！
若使用者輸入的數字大於該數字則印出：答案比較小喔！
若是命中解答則印出：恭喜，你答對了！
'''
import random
play=input('請問你想跟我玩猜數字遊戲嗎？（選 1 要玩，選 0 結束): ')
answer=random.randrange(100)
#print(answer)
while play=='1':
    guess=input('考考你猜數字遊戲，請輸入一個數字(0-100): ')
    if int(guess)>answer:
        print('答案比較小喔！')
    elif int(guess)<answer:
        print('答案比較大喔！')
    else:
        print('恭喜，你答對了！')
        break
print('See You Next Time.')