class House:
    def __init__(self, name, number_of_floors, ):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            new_floor = list(range(1, new_floor + 1))
            print(self.name, *new_floor)

        return self.number_of_floors

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name},  Количество этажей: {self.number_of_floors}"


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Акация', 22)

h1.go_to(12)
h2.go_to(3)

print(len(h1))
print(len(h2))

print(str(h1))
print(str(h2))