class MyList(list):

    def count(self):
        return len(self)

llist = MyList([1, 2, 3, 5])
print(llist.count())