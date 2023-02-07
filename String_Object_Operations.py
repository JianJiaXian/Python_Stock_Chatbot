#字串格式化（formatting）
name="Xian"
text='python'
sentence1='hello {}, hello {}'.format(name,text)
print(sentence1)
#hello Xian, hello python

#字串插值（Formatted String Literal）
sentence2=f"Hello, {text}"
print(sentence2)
#Hello, python

#HW3
'''
請設計一個程式：
讓使用者可以輸入英文字串（文字提示就好不用做判斷），
並透過取出使用者輸入的字串將最後所有字串轉成大寫後，
取出最後三個字元印出結果。
'''
last=input('輸入英文字串: ')
out=str(last).upper()
print(out[-3:])