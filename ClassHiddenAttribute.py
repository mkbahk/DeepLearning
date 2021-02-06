class Knight:
    __item_limit = 10 ##비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit) ##클래스 안에서만 접근할 수 있음
    ###end of def
###end of class


x = Knight()
x.__item_limit = 100

x.print_item_limit() 

print(x.__item_limit)
#print(Knight.__item_limit)
Knight.print_item_limit(x)
