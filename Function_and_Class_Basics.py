#docstring
def multiply(number1, number2):
    """This function will return the two numbers multiply value
    :param number1 (int): this is the first param
    :param number2 (int): this is the second param
    :returns (int): this is the multiply return value
    """
    return number1 * number2

#在function中使用全域變數
number=10
def global_var():
    global number
    print(number)
global_var()

#Decorator裝飾器/@語法糖
#把函式當作變數傳到另一個函式進行加工，把裝飾過的函式再傳回來
def my_decorator(func):
    def wrap():
        print('裝飾器加料')
        # 執行傳入的函式
        func()
    return wrap

@my_decorator
def my_func():
    print('被裝飾函式')

my_func()
'''
裝飾器加料
被裝飾函式
'''
#類別

class Book:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
    def get_discount_price(self,discount_rate):
        return self.price*discount_rate

book1=Book('三隻小豬',200,'童話')
book2=Book('三國演義',450,'歷史')

print(book1.name,book2.name)
#('三隻小豬',) ('三國演義',)
book1_discount_price=book1.get_discount_price(0.75)
book2_discount_price=book2.get_discount_price(0.8)
print(book1_discount_price,book2_discount_price)

#HW6
"""
請設計一個函式，
讓使用的人可以傳入整數後可以回傳該數是否可以被 2 整除（True/False）
"""
def divided(num):
    if int(num)%2==0:
        return print('True')
    else:
        return print('False')
num=input('請輸入一個數字: ')
divided(num)