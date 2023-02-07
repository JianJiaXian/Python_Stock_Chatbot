from Python_Module.my_module import print_text
def main():
    print_text('Life is short,I keep Learning.')
main()

#random模組
import random
random_fruits=random.choice(['apple','banana','kiwi'])
#0~10
random_num1=random.randint(1,10)
#0~1
random_num2=random.random()

#request
import requests
resp=requests.get('https://www.google.com')
print(resp.text)