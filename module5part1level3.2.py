import random

import armoredwarrior

warriors_health_points = 100
warriors_min_base_damage = 10
warriors_max_base_damage = 30
warriors_min_armor_damage = 0
warriors_max_armor_damage = 10
armor_durability = 100
warriors_damage_reduction = 0
armor_damage_reduction = 10
warriors_endurance = 100
warrior1_name = 'Lancelot'
warrior2_name = 'Tarkvin'
armored_warrior1 = armoredwarrior.ArmoredWarrior(warrior1_name,
                                                 warriors_health_points,
                                                 warriors_min_base_damage,
                                                 warriors_max_base_damage,
                                                 warriors_min_armor_damage,
                                                 warriors_max_armor_damage,
                                                 armor_durability,
                                                 armor_damage_reduction,
                                                 warriors_damage_reduction,
                                                 warriors_endurance)
armored_warrior2 = armoredwarrior.ArmoredWarrior(warrior2_name,
                                                 warriors_health_points,
                                                 warriors_min_base_damage,
                                                 warriors_max_base_damage,
                                                 warriors_min_armor_damage,
                                                 warriors_max_armor_damage,
                                                 armor_durability,
                                                 armor_damage_reduction,
                                                 warriors_damage_reduction,
                                                 warriors_endurance)
battle_round = 0
action = ['attack', 'defend']
while True:
    if (armored_warrior1.report_health_point() > 10
            and armored_warrior2.report_health_point() > 10):
        battle_round += 1
        print(f'_______________________________________________________\n'
              f'Начинается раунд {battle_round}')
        armored_warrior1.get_action(random.choice(action))
        armored_warrior2.get_action(random.choice(action))
        print(f'В раунде {battle_round} {armored_warrior1.report_name()} '
              f'решает {'атаковать' if 
              armored_warrior1.report_action() == 'attack' 
              else 'защищатся'}.')
        print(f'В раунде {battle_round} {armored_warrior2.report_name()} '
              f'решает {'атаковать' if 
              armored_warrior2.report_action() == 'attack' 
              else 'защищатся'}.\n')
        if (armored_warrior1.report_action() == 'attack'
                and armored_warrior2.report_action() == 'attack'):
            armored_warrior1.get_damage(armored_warrior2.attack())
            armored_warrior2.get_damage(armored_warrior1.attack())
        elif (armored_warrior1.report_action() == 'attack'
              and armored_warrior2.report_action() == 'defend'):
            armored_warrior2.get_damage(armored_warrior1.attack())
        elif (armored_warrior1.report_action() == 'defend'
              and armored_warrior2.report_action() == 'attack'):
            armored_warrior1.get_damage(armored_warrior2.attack())
        else:
            pass
        print(f'Состояние {armored_warrior1.report_name()}:\n'
              f'Очки здоровья: {armored_warrior1.report_health_point()}\n'
              f'Прочность брони: '
              f'{armored_warrior1.report_armor_durability()}\n'
              f'Выносливость: {armored_warrior1.report_endurance()}\n')
        print(f'Состояние {armored_warrior2.report_name()}:\n'
              f'Очки здоровья: {armored_warrior2.report_health_point()}\n'
              f'Прочность брони: '
              f'{armored_warrior2.report_armor_durability()}\n'
              f'Выносливость: {armored_warrior2.report_endurance()}\n')
    elif (armored_warrior1.report_health_point() > 10
          and armored_warrior2.report_health_point() < 10):
        print(f'{armored_warrior2.report_name()} при смерти,'
              f'пришло время решить его судьбу!')
        while True:
            user_choice = input('Введите "спасти", что бы сохранить ему '
                                'жизнь. Или "казнить", что бы казнить его: ')
            if user_choice == 'спасти':
                print(f'Вы сохранили жизнь {armored_warrior2.report_name()}.')
                break
            elif user_choice == 'казнить':
                print(f'По вашему желанию {armored_warrior1.report_name()} '
                      f'добивает {armored_warrior2.report_name()}')
                armored_warrior2.get_status('dead')
                break
            else:
                print('Неверная команда.')
        break
    elif (armored_warrior1.report_health_point() < 10
          and armored_warrior2.report_health_point() > 10):
        print(f'{armored_warrior1.report_name()} при смерти,'
              f'пришло время решить его судьбу!')
        while True:
            user_choice = input('Введите "спасти", что бы сохранить ему '
                                'жизнь. Или "казнить", что бы казнить его: ')
            if user_choice == 'спасти':
                print(f'Вы сохранили жизнь {armored_warrior1.report_name()}.')
                break
            elif user_choice == 'казнить':
                print(f'По вашему желанию {armored_warrior2.report_name()} '
                      f'добивает {armored_warrior1.report_name()}')
                armored_warrior1.get_status('dead')
                break
            else:
                print('Неверная команда.')
        break
    else:
        print('Оба воина при смерти и не могут продолжать бой.')
        break
print('Бой завершен.')
