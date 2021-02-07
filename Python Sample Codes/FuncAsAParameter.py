def hello():
    print("hello")
###end of def:

def bye():
    print("Bye")
###end of def:

def send(method):
    method()
###end of def:

def send2(method):
    method
###end of def:

send(hello)

send2(bye())


