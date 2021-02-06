class Person:
    count = 0 ##클래스 속성

    def __init__(self):
        Person.count += 1
    ###end of def

    @classmethod
    def print_count(cls):
        print("{0}명 생성되었습니다.".format(cls.count)) ##cls로 클래스속성에 접근
    ###end of def
###end of class

james = Person()
maria = Person()

Person.print_count() ## 2명이 생성되었습니다.
