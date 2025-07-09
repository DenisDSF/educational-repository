import random

class Warrior():

    def __init__(self, name, health_point, damage):
        self.name = name
        self.health_point = health_point
        self.damage = damage

    def attack(self):
        return self.damage

    def get_damage(self, incoming_damage):
        self.health_point -= incoming_damage


warriors_health_points = 100
warriors_damage = 20
warrior1 = Warrior('Lancelot', warriors_health_points, warriors_damage)
warrior2 = Warrior('Tarkvin', warriors_health_points, warriors_damage)
round_num = 0
while True:
    if warrior1.health_point != 0 and warrior2.health_point !=0:
        dueling_warriors = [warrior1, warrior2]
        round_num += 1
        num = random.randint(0, 1)
        attacker = dueling_warriors.pop(num)
        defender = dueling_warriors.pop()
        defender.get_damage(attacker.attack())
        print(f'В раунде {round_num} атакует {attacker.name}, нанося'
              f' {attacker.damage} едениц урона, теперь у {defender.name} - '
              f'{defender.health_point} очков здоровья!')
    else:
        print(f'{attacker.name} побеждает в {round_num} раунде!')
        break



