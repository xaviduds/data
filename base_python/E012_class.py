class Dog:
    def __init__(self, dogBreed, dogEyeColor, dogAge, dogBeauty='Beautiful'):
        self.breed = dogBreed
        self.eyeColor = dogEyeColor
        self.age = dogAge
        self.beauty = dogBeauty


bartolomeu = Dog('Shih-Tzu', 'Brown', 3, 'Not just beautiful, Fabulous')

print(bartolomeu.breed + '. ' + bartolomeu.beauty)


class Cat:
    def __init__(self):
        self.fur = 'kurz'
        self.personality = 'minds his business'
        self.agility = 'Professional Parkourer Board Certified'


Januario = Cat()
print(Januario.personality)

Mitski = Cat()
print(Mitski.agility)
