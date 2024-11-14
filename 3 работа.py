import random
import time

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.sleepiness = 0
        self.mood = 10 # 0 - плохое, 10 - отличное

    def feed(self):
        self.hunger -= 2
        self.mood += 1
        print(f"{self.name}: Мяу! Спасибо за вкусняшку!")

    def play(self):
        self.sleepiness += 1
        self.mood += 2
        print(f"{self.name}: Мяу-мяу! Это было весело!")

    def sleep(self):
        self.sleepiness -= 3
        print(f"{self.name}: Зззз...")

    def status(self):
        print(f"Имя: {self.name}")
        print(f"Голод: {self.hunger}")
        print(f"Сонливость: {self.sleepiness}")
        print(f"Настроение: {self.mood}")

    def update(self):
        self.hunger += 1
        self.sleepiness += 1
        self.mood -= 1

    # Добавлены методы с русскими названиями
    def Покормить(self):
        self.feed()

    def Поиграть(self):
        self.play()

    def Поспать(self):
        self.sleep()


my_cat = Cat("Мурзик")

while True:
    my_cat.update()
    my_cat.status()
    action = input("Что вы хотите сделать? (Покормить, Поиграть, Поспать, Уйти): ").lower()
    if action == "покормить":
        my_cat.Покормить()
    elif action == "поиграть":
        my_cat.Поиграть()
    elif action == "поспать":
        my_cat.Поспать()
    elif action == "уйти":
        break
    else:
        print("Неизвестная команда.")
    time.sleep(2)
