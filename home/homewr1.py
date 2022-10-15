class Hero:
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        a = self.hp + 100
        return a

    def two_damage(self):
        b = self.damage * 2
        return b

    def greetings(self):
        print(f'my name is {self.name}')

    def brand_phrase(self):
        print('good will win.')


gur = Hero('gurat', 'gura', 120, 10)
bek = Hero('Bektur', 'beka', 1000, 1000)
ali = Hero('Alihan', 'Front', 10, 5)
abdumalik = Hero('Malik', 'Mali', 268, 15)
result = [ali, abdumalik, bek, gur]
gur.heal()
ali.brand_phrase()
bek.two_damage()
abdumalik.greetings()
