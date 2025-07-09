import random

import armoredwarrior

warriors_health_points = 100
warriors_min_base_damage = 10
warriors_max_base_damage = 30
warriors_max_armor_damage = 10
armor_durability = 100
armor_damage_reduction = 10
warrior_endurance = 100
warrior1_name = 'Lancelot'
warrior2_name = 'Tarkvin'
armored_warrior1 = armoredwarrior.ArmoredWarrior(warrior1_name,
                                  warriors_health_points,
                                  warriors_min_base_damage,
                                  warriors_max_base_damage,
                                  warriors_max_armor_damage,
                                  armor_durability,
                                  armor_damage_reduction,
                                  warrior_endurance)
armored_warrior2 = armoredwarrior.ArmoredWarrior(warrior2_name,
                                  warriors_health_points,
                                  warriors_min_base_damage,
                                  warriors_max_base_damage,
                                  warriors_max_armor_damage,
                                  armor_durability,
                                  armor_damage_reduction,
                                  warrior_endurance)

battle_round = 0
action = ['attack', 'defend']
while True:
    if (armored_warrior1.health_point > 10 and
            armored_warrior2.health_point > 10):
        battle_round += 1
        print(f'_______________________________________________________\n'
              f'Начинается раунд {battle_round}')
        armored_warrior1.get_action(random.choice(action))
        armored_warrior2.get_action(random.choice(action))
        print(f'В раунде {battle_round} {armored_warrior1.name} решает '
              f'{'атаковать' if armored_warrior1.action == 'attack' 
              else 'защищатся'}.')
        print(f'В раунде {battle_round} {armored_warrior2.name} решает '
              f'{'атаковать' if armored_warrior2.action == 'attack'
              else 'защищатся'}.')
        if (armored_warrior1.action == 'attack' and
                armored_warrior2.action == 'attack'):
            armored_warrior1.attack(armored_warrior2)
            armored_warrior2.attack(armored_warrior1)
        elif (armored_warrior1.action == 'attack' and
              armored_warrior2.action == 'defend'):
            armored_warrior2.defend()
            armored_warrior1.attack(armored_warrior2)
            armored_warrior2.remove_defence_bonuses()
        elif (armored_warrior1.action == 'defend' and
              armored_warrior2.action == 'attack'):
            armored_warrior1.defend()
            armored_warrior2.attack(armored_warrior1)
            armored_warrior1.remove_defence_bonuses()
        else:
            armored_warrior1.defend()
            armored_warrior2.defend()
            armored_warrior1.remove_defence_bonuses()
            armored_warrior2.remove_defence_bonuses()
        print(armored_warrior1)
        print(armored_warrior2)

    elif (armored_warrior1.health_point > 10 and
          armored_warrior2.health_point < 10):
        print(f'{armored_warrior2.name} при смерти,'
              f'пришло время решить его судьбу!')
        while True:
            user_choice = input('Введите "спасти", что бы сохранить ему '
                                'жизнь. Или "казнить", что бы казнить его:')
            if user_choice == 'спасти':
                print(f'Вы сохранили жизнь {armored_warrior2.name}.')
                break
            elif user_choice == 'казнить':
                armored_warrior2.health_point = 0
                print(f'По вашему желанию {armored_warrior1.name} '
                      f'добивает {armored_warrior2.name}')
                break
            else:
                print('Неверная команда. Введитие "спасти" или "казнить"')
        break

    elif (armored_warrior1.health_point < 10 and
          armored_warrior2.health_point > 10):
        print(f'{armored_warrior1.name} при смерти,'
              f'пришло время решить его судьбу!')
        while True:
            user_choice = input('Введите "спасти", что бы сохранить ему '
                                'жизнь. Или "казнить", что бы казнить его: ')
            if user_choice == 'спасти':
                print(f'Вы сохранили жизнь {armored_warrior1.name}.')
                break
            elif user_choice == 'казнить':
                armored_warrior1.health_point = 0
                print(f'По вашему желанию {armored_warrior2.name} '
                      f'добивает {armored_warrior1.name}')
                break
            else:
                print('Неверная команда. Введитие "спасти" или "казнить"')
        break

    else:
        print('Оба воина при смерти и не могут продолжать бой.')
        break

print('Бой завершен.')
