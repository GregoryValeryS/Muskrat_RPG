from mimesis import Person
from mimesis.enums import Gender
from mimesis import Text
from random import randint, choice


def test():
    text = Text('ru')
    print(text.swear_word())
    print(text.answer())
    print(text.level())
    print(text.word())

    person = Person('ru')  # мы создали объект person, класса Person()

    man = person.full_name(gender=Gender.MALE)
    woman = person.full_name(gender=Gender.FEMALE)
    age = person.age(minimum=16, maximum=66)
    height = person.height(minimum=1.5, maximum=2.0)
    weight = person.weight(minimum=38, maximum=90)
    sexual_orientation = person.sexual_orientation(symbol=False)
    worldview = person.worldview()
    political_views = person.political_views()

    print(man, woman)
    print(age)
    print(height)
    print(weight)
    print(sexual_orientation)
    print(worldview)
    print(political_views)


NPC_types_dict = {
    'Разбойник':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 60,  # процент мужчин

         'elite_chance': 30, 'legend_chance': 5,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 50,  # веролятность носить кличку
         'full_name_chance': 50,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 50,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 5, 'max_lvl': 50,

         'base_physique': 3, 'base_mastery': 2, 'base_intelligence': 2,  # базовые характеристики

         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
}
"""
    'Мирный житель':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола. Ставится значение 'Н'
         'male_percent': 70,  # процент мужчин
         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'full_name_chance': 20,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 80,  # вероятность идентификации себя по имени, остальное - по фамилии
         'nick_chance': 70,  # веролятность носить кличку
         'base_physique': 3, 'base_mastery': 2, 'base_intelligence': 2,
         'elite_chance': 30, 'legend_chance': 10,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Разбойник':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Стражник':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Воин':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Маг':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Рыцарь':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Странник':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Дракон':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Гигант':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Зверь':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Элементаль':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Мутант':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
    'Ребёнок':
        {'name_chance': 1, 'last_name_chance': 1, 'nick_chance': 0,
         'weapon_chance': 0.1, 'armor_chance': 0, 'shield_chance': 0, 'health_damage': 2},
}"""

plate = {  # шкура. Название: значение брони
    'Без лат': 0,
    'Ржавый доспех': 4,
    'Обычный доспех': 9,
    'Хороший доспех': 12,
    'Отличный доспех': 17,
    'Эпический доспех': 25,
    'Легендарный доспех': 50,
}

shell = {  # шкура. Название: значение брони
    'Роговое покрытие': 6,
    'Каменное покрытие': 10,
    'Железное покрытие': 15,
    'Стальное покрытие': 20,
    'Титановое покрытие': 30,
}

weapons_types = {
    'Без оружия':
        {'name': 'Без оружия', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 1},
    'Кастет':
        {'name': 'Обычный кастет', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    'Кинжал':
        {'name': 'Обычный кинжал', 'two-handed': False, 'crit': 4,
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    'Меч':
        {'name': 'Обычный меч', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 0, 'health_damage': 3},
    'Копьё':
        {'name': 'Обычное копьё', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 1, 'health_damage': 2},
    'Топор':
        {'name': 'Обычный топор', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 2, 'health_damage': 2},
    'Молот':
        {'name': 'Обычный молот', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 3, 'penetration_damage': 1, 'health_damage': 2},
    '2хПосох':
        {'name': 'Обычный посох', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    '2хМеч':
        {'name': 'Обычный 2х меч', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 1, 'health_damage': 6},
    '2хКопьё':
        {'name': 'Обычное 2х копьё', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 2, 'health_damage': 5},
    '2хТопор':
        {'name': 'Обычный 2х топор', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 5, 'penetration_damage': 4, 'health_damage': 4},
    '2хМолот':
        {'name': 'Обычный 2х молот', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 7, 'penetration_damage': 2, 'health_damage': 4},
    'Метательное':
        {'name': 'Обычное метательное оружие', 'two-handed': False, 'crit': 4,
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    'Пистолет':
        {'name': 'Обычный пистолет', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 2, 'health_damage': 3},
    'Лук':
        {'name': 'Обычный лук', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 3},
    'Праща':
        {'name': 'Обычная праща', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 1, 'health_damage': 3},
    'Арбалет':
        {'name': 'Обычный арбалет', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 3, 'penetration_damage': 5, 'health_damage': 6},
    'Ружьё':
        {'name': 'Обычное ружьё', 'two-handed': True, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 6, 'health_damage': 6},
    'Щит':
        {'name': 'Обычный щит', 'two-handed': False, 'crit': 2,
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 0},
}

spells_dict = {
    'Свет Монету': 'Восстанавливает +2 хп всем союзникам',
    'Гнев Монету': 'Наносит -1 хп всем врагам',
    'Жар Монету': 'Наносит -3 хп противнику',
    'Проклятье плоти ': '-1хп врагу каждый ход',
    'Проклятье железа': '-2 брони врагу каждый ход',
    'Заморозка': '-2 хп врагу',
    'Затягивание ран': '+3 хп союзнику',
    'Гипноз ': 'попытка взять врага под контроль',
    'Огненный шар': '-2 хп врагу',
    'Буря': 'каждый ход молния бьёт случайного соперника -2хп ',
    'Корни': 'обездвиживает противника',
    'Болотная твердь': 'обездвиживает противников и союзников вокруг',
    'Столп света': '+2 хп себе за ход',
    'Благословление': '+2 к применяемому навыку союзника',
    'Проклятие': '-1 к применяемому навыку соперника',
    'Ангельские удары': 'До конца боя ваши удары без оружия = удару молота',
    'Слёзы любви': 'ваши раны затягиваются каждый ход +1 хп',
}

talents_dict = {
    'Отталкивание': 'Толчёк всех в непосредственной близости',
    'Берсерк': 'Вы наносите и получаете 2 раза больше урона',
    'Кулаки - молоты': 'Урон ваших ударов кулаком равен урону молотов по умолчанию',
    'Когти - кинжалы': 'Урон ваших ударов равен урону кинжалов',
    'Невидимость': 'Вы можете 1 раз за бой (или перед) стать невидимым',
    'Девственность': 'Вы наносите и получаете в 2 раза меньше урона',
    'Молитва': 'Вы восстанавливаете 2 очка здоровья',
    'Принуждение': 'Вы срываете одежду и броню с врага - секс-интереса',
}

skills_dict = {
    'Тип: Ближний бой': ['1хМетать/кулак', '1хКлинки', '1хУдарное', '1/2хКопья/Посох', '2хКлинки', '2хУдарное'],
    'Тип: Дальний бой': ['1хПистолеты', '2хРужья', '2хАрбалет', '2хЛук', '2хПраща'],
    'Тип: Небоевые': ['Взлом', 'Ремонт', 'Карты', 'Выживание', 'Животные']
}

skills_types_list = []
for skill_type in dict.keys(skills_dict):
    skills_types_list.append(skill_type)
skills_list = [skills_types_list[0]] + skills_dict['Тип: Ближний бой'] + \
              [skills_types_list[1]] + skills_dict['Тип: Дальний бой'] + \
              [skills_types_list[2]] + skills_dict['Тип: Небоевые']
