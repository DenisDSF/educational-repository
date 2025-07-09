import random

class ArmoredWarrior():

    def __init__(self, name, health_point, min_base_damage, max_base_damage,
                 min_armor_damage, max_armor_damage, armor_durability,
                 armor_damage_reduction, damage_reduction,
                 endurance):
        self.__name = name
        self.__health_point = health_point
        self.__min_base_damage = min_base_damage
        self.__max_base_damage = max_base_damage
        self.__armor_durability = armor_durability
        self.__armor_damage_reduction = armor_damage_reduction
        self.__base_damage_reduction = damage_reduction
        self.__endurance = endurance
        self.__endurance_damage_penalty = 10
        self.__min_armor_damage = min_armor_damage
        self.__max_armor_damage = max_armor_damage
        self.__armor_damage = 0
        self.__damage = 0
        self.__action = ''
        self.__status = 'alive'

    def get_action(self, action):
        self.__action = action

    def attack(self):
        if self.__endurance <= 0:
            self.__damage = random.randint(self.__min_base_damage,
                                           self.__max_base_damage
                                           - self.__endurance_damage_penalty)
        else:
            self.__damage = random.randint(self.__min_base_damage,
                                           self.__max_base_damage)
        self.__armor_damage = random.randint(self.__min_armor_damage,
                                             self.__max_armor_damage)
        self.__endurance -= 10
        return [self.__damage, self.__armor_damage]

    def get_damage(self, damage):
        if self.__action == 'defend' and self.__armor_durability > 0:
            damage_reduction = self.defend()
            self.__health_point = self.__health_point - (damage.pop(0)
                                                     - damage_reduction)
            self.__armor_durability -= damage.pop()
        else:
            self.__health_point -= damage.pop(0)

    def defend(self):
        return self.__base_damage_reduction + self.__armor_damage_reduction

    def get_status(self, status):
        self.__status = status
        if self.__status == 'dead':
            self.__health_point = 0

    def report_action(self):
        return self.__action

    def report_name(self):
        return self.__name

    def report_health_point(self):
        return self.__health_point

    def report_armor_durability(self):
        return self.__armor_durability

    def report_endurance(self):
        return self.__endurance