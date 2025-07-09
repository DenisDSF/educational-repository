import random

class ArmoredWarrior():

    def __init__(self, name, health_point, min_base_damage, max_base_damage,
                 max_armor_damage, armor_durability,
                 armor_damage_reduction, endurance):
        self.name = name
        self.health_point = health_point
        self.min_base_damage = min_base_damage
        self.max_base_damage = max_base_damage
        self.armor_durability = armor_durability
        self.armor_damage_reduction = armor_damage_reduction
        self.endurance = endurance
        self.endurance_damage_penalty = 10
        self.max_armor_damage = max_armor_damage
        self.armor_damage = 0
        self.base_damage_reduction = 0
        self.damage_reduction = self.base_damage_reduction
        self.damage = 0
        self.action = ''

    def get_action(self, action):
        self.action = action

    def attack(self, other):
        self.endurance -= 10
        if self.endurance <= 0:
            self.damage = random.randint(self.min_base_damage,
                                           self.max_base_damage
                                           - self.endurance_damage_penalty)
        else:
            self.damage = random.randint(self.min_base_damage,
                                           self.max_base_damage)
        other.health_point = (other.health_point
                                - (self.damage - other.damage_reduction))
        if other.armor_durability > 0 and other.action == 'defend':
            self.armor_damage = random.randint(0, self.max_armor_damage)
            other.armor_durability -= self.armor_damage

    def defend(self):
        if self.armor_durability > 0:
            self.damage_reduction = (self.base_damage_reduction
                                     + self.armor_damage_reduction)

    def remove_defence_bonuses(self):
        self.damage_reduction = self.base_damage_reduction

    def __str__(self):
        return (f'Состояние {self.name}:\n'
                f'Очки здоровья: \t {self.health_point}\n'
                f'Прочность брони: \t {self.armor_durability}\n'
                f'Выносливость: \t {self.endurance}')