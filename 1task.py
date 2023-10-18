class MyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} не найден в списке")

    def get(self, index):
        if 0<= index  <len(self.items):
            return self.items[index]

    def lenth(self):
        return len(self.items)
    def display(self):
        print(self.items)

my_list = MyList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
print(f"Длина списка: {len(my_list.items)}")
my_list.remove(3)
my_list.display()
print(f"Элемент с индексом 2: {my_list.get(2)}")