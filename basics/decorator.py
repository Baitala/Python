
def my_decorator(somefunc):
    def decorating_func(arg):
        print("Top text", arg, arg)
        somefunc(arg)
        print("Bottom text")
        somefunc(arg)
    return decorating_func

@my_decorator
def myfunc(line):
    print(line)

def html_decorator(infunc):
    def html_wrapper(arg):
        print("<html><head/><body><p>")
        infunc(arg)
        print("</p></body></html>")
    return html_wrapper

@html_decorator
def just_printing(text):
    print(text)

myfunc("sometext")

#print("\n ================================= \n")

#just_printing("Lorem ipsem dolor sit amet...")
