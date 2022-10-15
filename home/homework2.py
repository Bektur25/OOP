from homewr1 import Hero


class Air(Hero):
    two_heads = 2

    def __init__(self, name, nickname, hp, damage, fly=False):
        Hero.__init__(self, name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def Gen_x(self, value):
        pass

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')


class Ground(Hero):
    foot = 4

    def __init__(self, name, nickname, hp, damage, fly=0):
        Hero.__init__(self, name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')


class Galaxy(Hero):
    hands = 4

    def __init__(self, name, nickname, hp, damage, fly=not True):
        Hero.__init__(self, name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')


air_hero = Air('Beka', 'Bek', 100, 20)
ground_hero = Ground('Bektur', 'beka556', 80, 50)
galaxy_hero = Galaxy('Asyl', 'asyl312', 90, 10)

galaxy_hero.brand_phrase()

