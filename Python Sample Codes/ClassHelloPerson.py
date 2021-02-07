class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)
    ###end of def

###end of class

moonkee = Person()
keebeom = Person()

moonkee.put_bag("책")
keebeom.put_bag("게임기")
moonkee.bag.append("컴퓨터")
moonkee.bag[len(moonkee.bag)-1] = "노트북"

print(moonkee.bag)
print(keebeom.bag)
print(moonkee.bag)
