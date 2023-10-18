class Animal:
    def __init__(self,breed,cost):
        self.breed = breed
        self.cost = cost
    def move(self):
        pass

class Fish(Animal):
    def move(self):
        return "Плавает"

class Bird(Animal):
    def move(self):
        return "Летает"

class ZooShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, breed, cost):
        if not breed or not cost:
            print("Ошибка Порода и стоимость должны быть заполнены")
            return

        try:
            cost = float(cost)
            if cost <= 0:
                print("Стоимость должна быть положительным числом")
                return
        except ValueError:
            print("Ошибка: Стоимость должна быть числом.")
            return

        animal = Animal(breed, cost)
        self.animals.append(animal)

    def get_most_expensive_breed(self):
        if not self.animals:
            return "Зоо пуст"

        most_expensive_animal = max(self.animals, key=lambda animal: animal.cost)
        return f"Самая дорогая порода: {most_expensive_animal.breed} ({most_expensive_animal.cost} руб.)"
    def save_to_file(self, filename):
        with open(filename,'w') as file:
            for animal in self.animals:
                file.write(f"{animal.breed},{animal.cost}\n")

zoo_shop = ZooShop()

while True:
    print("Выберите действие")
    print("1 Добавить животное")
    print("2 найти самую дорогую породу")
    print("3 сохранить инфу в файл")
    print("4 выйти")

    choice = input("Введите номер действия: ")
    if choice == "1":
        breed = input("Введите породу: ")
        cost = float(input("Введите стоимость: "))
        zoo_shop.add_animal(breed, cost)
    elif choice == "2":
        result = zoo_shop.get_most_expensive_breed()
        print(result)
    elif choice == "3":
        filename = input("Введите имя файла ")
        zoo_shop.save_to_file(filename)
        print(f"Инфа сохр в файл'{filename}'")
    elif choice == "4":
        break
    else:
        print("Снова")



