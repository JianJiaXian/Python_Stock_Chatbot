#tuple
#新增tuple
test=(1,3)+(2,)
print(test)
#(1, 3, 2)

#list
#新增
name=["Xian","Shein"]
name.append("Allen")
print(name)
#['Xian', 'Shein', 'Allen']

#移除
name.remove("Allen")
print(name)
#['Xian', 'Shein']

#set
fruit1={'apple','banana'}
fruit2=set(['apple','orange'])
print(fruit1,fruit2)
#{'apple', 'banana'} {'orange', 'apple'}

#新增(兩種方式)
fruit1.add('orange')
fruit2.update(['banana','kiwi'])
print(fruit1,fruit2)
#{'orange', 'apple', 'banana'} {'orange', 'apple', 'kiwi', 'banana'}

#移除
fruit2.remove('banana')
print(fruit2)
#{'kiwi', 'apple', 'orange'}

#dict
language_info_dict={
    'name':'Python',
    'released_at':1991,
    'designed_by':'Guido van Rossum',
    'filename_extensions':['.py','.pyi']
}

#key不存在也不會輸出錯誤訊息
print(language_info_dict.get('name', 12))
#Python
print(language_info_dict.get('C#', 12))
#12

#新增
language_info_dict['user']='everyone'
print(language_info_dict)
#{'name': 'Python', 'released_at': 1991, 'designed_by': 'Guido van Rossum', 'filename_extensions': ['.py', '.pyi'], 'user': 'everyone'}

#回傳被刪除的值
removed_value=language_info_dict.pop('user')
print(removed_value)
#everyone
print(language_info_dict)
#{'name': 'Python', 'released_at': 1991, 'designed_by': 'Guido van Rossum', 'filename_extensions': ['.py', '.pyi']}

#取得all keys/values
print(language_info_dict.keys())
#dict_keys(['name', 'released_at', 'designed_by', 'filename_extensions'])
print(language_info_dict.values())
#dict_values(['Python', 1991, 'Guido van Rossum', ['.py', '.pyi']])

#HW4
'''
請設計一個程式：
讓使用者可以輸入喜歡的四種顏色（使用 , 分隔），
並透過字串物件的split() 方法將字串切分成 list 物件，
最後印出 list 的最後一種顏色。
'''
colors=input('input 4 kinds of your favorite color: ')
out=colors.split(',')
print(out[-1])
