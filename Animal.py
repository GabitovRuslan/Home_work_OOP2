import random
import time


class Animal:
    def __init__(self, weight, voice, gender):
        self.weight = weight
        self.voice = voice
        self.gender = gender
        self.man_and_gerl = ['У вас девочка', 'У вас мальчик']

    def eat(self, food):
        if food != False:
            self.weight += 0.5
            return f'{self.name} из класса {self.__class__.__name__} поел, и теперь весит {self.weight} кг.'

    def __add__(self, other):
        if type(other) != type(self):
            return f'Вы пытаетесь скрестить {self.__class__.__name__} c {other.__class__.__name__}, скрещивание разных видов не возможно!'
        elif self.gender == 'female' and other.gender == 'male' or self.gender == 'male' and other.gender == 'female':
            return random.choice(self.man_and_gerl)
        else:
            return 'В России однополые браки запрещенны =)'

    def attack(self, other):
        if other.weight < self.weight:
            return (
                f'Победил {self.name} из вида {self.__class__.__name__}! Так как превосходит соперника {other.name} из вида {other.__class__.__name__} по весу!')
        elif other.weight == self.weight:
            return 'Ничья! Вес бойцов одинаковый!'
        else:
            return (
                f'Победил {other.name} из вида {other.__class__.__name__}! Так как превосходит соперника {self.name} из вида {self.__class__.__name__} по весу!')


class Birds(Animal):
    def __init__(self, name, weight, voice, gender):
        super().__init__(weight, voice, gender)
        self.name = name

    def laid_an_egg(self):
        if self.gender == 'female':
            print('Снесла 2 яйца!')
        elif self.gender == 'male':
            print('Я мальчик! И не несу яйца!')
        else:
            print('Ну нет! Я либо "female" либо "male" ')


class Goose(Birds):
    goose_list = []

    def __init__(self, name, weight, voice, gender):
        self.name = name
        super().__init__(name, weight, voice, gender)
        self.goose_list.append(self)


goose_white = Goose('Белый', 120, 'Гусь говарит: Га-га-га', 'male')
goose_white.laid_an_egg()
goose_black = Goose('Черный', 26, 'Гусь говарит: Га-га-га', 'female')
goose_gray = Goose('серый', 46, 'Гусь говарит: Га-га-га', 'male')


class Chickens(Birds):
    chickens_list = []

    def __init__(self, name, weight, voice, gender):
        super().__init__(name, weight, voice, gender)
        self.chickens_list.append(self)


koko = Chickens('Ко-ко', 20, 'кут-кудах', 'female')
sopelka = Chickens('Сопелька', 25, 'кут-кудах', 'male')

print(goose_black + koko)
print(goose_black + goose_white)
print(goose_white.attack(koko))
print(sopelka.attack(goose_black))


class Dogs(Animal):
    dogs_list = []

    def __init__(self, name, weight, voice, gender):
        self.name = name
        super().__init__(weight, voice, gender)
        self.dogs_list.append(self)

    def jump_high(self, high):
        if high > 3:
            return 'Это слишком высоко, я не могу'
        elif high == 0:
            return 'Ты издеваишся что ли!?'
        return f'Я это зделала, я прыгнула на {high} м.'

    def beat_with_a_paw(self, how_many_times):
        if how_many_times > 5:
            print('Я не могу, это слишком много!')
        elif 0 < how_many_times <= 5:
            print(f'Хорошо, я ударю лапой ровно {how_many_times}!')
            for i in range(how_many_times):
                time.sleep(1)
                print(i + 1)
            print('Я это зделала, дай вкусняшку!')
        elif how_many_times <= 0:
            print('Это не смешно, дай вкусняшку! Гав!')


dog = Dogs('Буря', 45, 'Гав-Гав', 'female')
dog.beat_with_a_paw(0)
print(dog.attack(goose_black))
print(dog.jump_high(2))
all_animal_list = Goose.goose_list + Dogs.dogs_list + Chickens.chickens_list
for i in all_animal_list:
    print(i.eat('корм'))
dog.beat_with_a_paw(5)
