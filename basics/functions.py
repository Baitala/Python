def hello(name):
    print("Hello ", name)
    
hello("John")

f = hello #упоминание фунцкии — без скобок. Тут создан синоним, ссылка f

f("Nancy") #

def hello_separated(name="World",separator=" "):
    print("Hello",name,sep=separator)

hello_separated(separator="***",name="John") #вызов с явным указанием именованных параметров