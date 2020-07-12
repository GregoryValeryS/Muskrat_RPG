NPC_types_dict = {
    'Разбойник':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 70,  # процент мужчин

         'elite_chance': 20, 'legend_chance': 5,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 80,  # вероятность носить кличку
         'full_name_chance': 50,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 50,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 10, 'max_lvl': 50,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 80,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 80,  # процент скилов, сотальное - спелы

         'ranged_percent': 40, 'melee_percent': 50,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 3, 'base_mastery': 2, 'base_intelligence': 2,  # базовые характеристики

         'weapon_percent': 100,  # вероятнось быть вооруженным
         'shield_percent': 100,
         'armor_percent': 20,  # вероятность носить латы
         },
    'Мирный житель':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 10, 'legend_chance': 5,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 10,  # веролятность носить кличку
         'full_name_chance': 80,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 90,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 5, 'max_lvl': 60,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 80,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 90,  # процент скилов, сотальное - спелы

         'ranged_percent': 20, 'melee_percent': 10,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 2, 'base_mastery': 2, 'base_intelligence': 2,  # базовые характеристики

         'weapon_percent': 30,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 0,  # вероятность носить латы
         },
    'Стражник':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 60,  # процент мужчин

         'elite_chance': 30, 'legend_chance': 10,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 10,  # веролятность носить кличку
         'full_name_chance': 50,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 50,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 10, 'max_lvl': 50,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 100,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 0,

         'skill_or_spell': 100,  # процент скилов, сотальное - спелы

         'ranged_percent': 40, 'melee_percent': 50,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 5, 'base_mastery': 2, 'base_intelligence': 4,  # базовые характеристики

         'weapon_percent': 100,  # вероятнось быть вооруженным
         'shield_percent': 50,
         'armor_percent': 100,  # вероятность носить латы
         },
    'Воин':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 50, 'legend_chance': 20,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 10,  # веролятность носить кличку
         'full_name_chance': 50,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 70,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 20, 'max_lvl': 70,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 90,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 0,

         'skill_or_spell': 100,  # процент скилов, сотальное - спелы

         'ranged_percent': 50, 'melee_percent': 50,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 8, 'base_mastery': 7, 'base_intelligence': 2,  # базовые характеристики

         'weapon_percent': 100,  # вероятнось быть вооруженным
         'shield_percent': 50,
         'armor_percent': 50,  # вероятность носить латы
         },
    'Маг':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 60, 'legend_chance': 40,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 90,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 80,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 60, 'max_lvl': 80,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 0,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 10,  # процент скилов, сотальное - спелы

         'ranged_percent': 10, 'melee_percent': 40,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 5, 'base_mastery': 2, 'base_intelligence': 10,  # базовые характеристики

         'weapon_percent': 20,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 30,  # вероятность носить латы
         },
    'Рыцарь':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 70, 'legend_chance': 30,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 100,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 20, 'max_lvl': 60,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 80,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 70,  # процент скилов, сотальное - спелы

         'ranged_percent': 0, 'melee_percent': 80,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 8, 'base_mastery': 8, 'base_intelligence': 5,  # базовые характеристики

         'weapon_percent': 100,  # вероятнось быть вооруженным
         'shield_percent': 100,
         'armor_percent': 100,  # вероятность носить латы
         },
    'Странник':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 50, 'legend_chance': 50,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 50,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 40, 'max_lvl': 100,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 50,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 40,  # процент скилов, сотальное - спелы

         'ranged_percent': 50, 'melee_percent': 50,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 10, 'base_mastery': 10, 'base_intelligence': 10,  # базовые характеристики

         'weapon_percent': 100,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 100,  # вероятность носить латы
         },
    'Дракон':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 40, 'legend_chance': 50,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 0,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 50, 'max_lvl': 100,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 50,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 0,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 0,  # процент скилов, сотальное - спелы

         'ranged_percent': 0, 'melee_percent': 0,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 15, 'base_mastery': 10, 'base_intelligence': 10,  # базовые характеристики

         'weapon_percent': 0,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 100,  # вероятность носить латы
         },
    'Гигант':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 30, 'legend_chance': 20,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 50,  # веролятность носить кличку
         'full_name_chance': 0,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 20, 'max_lvl': 50,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 90,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 90,  # процент скилов, сотальное - спелы

         'ranged_percent': 50, 'melee_percent': 50,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 3, 'base_mastery': 1, 'base_intelligence': 2,  # базовые характеристики

         'weapon_percent': 100,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 50,  # вероятность носить латы
         },
    'Зверь':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 30, 'legend_chance': 10,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 0,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 0,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 10, 'max_lvl': 50,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 50,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 0,  # имеет скилы и спелы вообще
         'has_spells': 0,

         'skill_or_spell': 0,  # процент скилов, сотальное - спелы

         'ranged_percent': 0, 'melee_percent': 0,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 6, 'base_mastery': 4, 'base_intelligence': 2,  # базовые характеристики

         'weapon_percent': 0,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 0,  # вероятность носить латы
         },
    'Элементаль':
        {'has_sex': 0,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 100,  # процент мужчин

         'elite_chance': 50, 'legend_chance': 50,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 0,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 0,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 20, 'max_lvl': 80,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 50,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 50,  # процент скилов, сотальное - спелы

         'ranged_percent': 0, 'melee_percent': 70,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 10, 'base_mastery': 1, 'base_intelligence': 5,  # базовые характеристики

         'weapon_percent': 100,  # вероятнось быть вооруженным
         'shield_percent': 50,
         'armor_percent': 100,  # вероятность носить латы
         },
    'Мутант':
        {'has_sex': 0,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 100,  # процент мужчин

         'elite_chance': 50, 'legend_chance': 30,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 0,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 0,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 20, 'max_lvl': 80,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 100,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 0,  # имеет скилы и спелы вообще
         'has_spells': 0,

         'skill_or_spell': 100,  # процент скилов, сотальное - спелы

         'ranged_percent': 0, 'melee_percent': 0,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 10, 'base_mastery': 5, 'base_intelligence': 2,  # базовые характеристики

         'weapon_percent': 0,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 100,  # вероятность носить латы
         },
    'Ребёнок':
        {'has_sex': 1,  # 1 - есть пол, 0 - нет пола (ставится значение 'Н')
         'male_percent': 50,  # процент мужчин

         'elite_chance': 0, 'legend_chance': 0,  # trash = 100-'elite_chance'-'legend_chance'

         'name_chance': 1,  # 0 - нет имени, 1 - есть имя
         'nick_chance': 0,  # веролятность носить кличку
         'full_name_chance': 50,  # вероятность именть полное и имя, и фамилию
         'first_name_or_last_name': 100,  # вероятность идентификации себя по имени, остальное - по фамилии

         'min_lvl': 4, 'max_lvl': 14,  # каждый уровень - очко навыков/характеристик

         'might_or_magic': 50,  # шанс иметь уклон в физ.навыки, а не в магию

         'has_skills': 1,  # имеет скилы и спелы вообще
         'has_spells': 1,

         'skill_or_spell': 90,  # процент скилов, сотальное - спелы

         'ranged_percent': 5, 'melee_percent': 5,  # считаем от 100, остальное - 'non-combat_percent'

         'base_physique': 2, 'base_mastery': 2, 'base_intelligence': 3,  # базовые характеристики

         'weapon_percent': 0,  # вероятнось быть вооруженным
         'shield_percent': 0,
         'armor_percent': 0,  # вероятность носить латы
         },
}

NPC_types_list = list(NPC_types_dict.keys())

talents_dict = {  # индексы талантов для единоборств не стоит менять (на их основе работает программа)
    'Кулаки-молоты': 'Урон ваших ударов кулаком равен урону молотов по умолчанию',
    'Когти-кинжалы': 'Урон ваших ударов равен урону кинжалов',
    'Отталкивание': 'Толчёк всех в непосредственной близости',
    'Берсерк': 'Вы наносите и получаете 2 раза больше урона',
    'Невидимость': 'Вы можете 1 раз за бой (или перед) стать невидимым',
    'Девственность': 'Вы наносите и получаете в 2 раза меньше урона',
    'Молитва': 'Вы восстанавливаете 2 очка здоровья',
    'Принуждение': 'Вы срываете одежду и броню с врага - секс-интереса',
}

talents_list = list(talents_dict.keys())

skills_dict = {
    'Melee': ['Единоборства', '1хКлинок', '1хУдарное', '1/2хКопьё/Посох', '2хКлинок', '2хУдарное'],
    'Ranged': ['1хПистолеты', '2хРужьё', '2хАрбалет', '2хЛук', '2хПраща'],
    'Noncombat': ['Взлом', 'Ремонт', 'Карты', 'Выживание', 'Животные', 'Музыка']
}
skills_type_list = list(skills_dict.keys())

skills_list_noncombat = skills_dict['Melee']
skills_list_ranged = skills_dict['Ranged']
skills_list_melee = skills_dict['Noncombat']

skills_list = skills_dict['Melee'] + skills_dict['Ranged'] + skills_dict['Noncombat']

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

spells_list = list(spells_dict.keys())

weapons_dict = {
    'Без оружия':
        {'name': 'Без оружия', 'ranged': False, 'two-handed': False, 'crit': 2, 'speed': 2, 'skill': 'Единоборства',
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 1},
    'Кастет':
        {'name': 'Обычный кастет', 'ranged': False, 'two-handed': False, 'crit': 2, 'speed': 2, 'skill': 'Единоборства',
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    'Кинжал':
        {'name': 'Обычный кинжал', 'ranged': False, 'two-handed': False, 'crit': 3, 'speed': 2, 'skill': '1хКлинки',
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    'Меч':
        {'name': 'Обычный меч', 'ranged': False, 'two-handed': False, 'crit': 2, 'speed': 1, 'skill': '1хКлинки',
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 0, 'health_damage': 3},
    'Копьё':
        {'name': 'Обычное копьё', 'ranged': False, 'two-handed': False, 'crit': 2, 'speed': 1,
         'skill': '1/2хКопья/Посох',
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 1, 'health_damage': 2},
    'Топор':
        {'name': 'Обычный топор', 'ranged': False, 'two-handed': False, 'crit': 2, 'speed': 1, 'skill': '1хУдарное',
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 2, 'health_damage': 2},
    'Молот':
        {'name': 'Обычный молот', 'ranged': False, 'two-handed': False, 'crit': 2, 'speed': 1, 'skill': '1хУдарное',
         'magic_damage': 0, 'armor_damage': 3, 'penetration_damage': 1, 'health_damage': 2},
    '2хПосох':
        {'name': 'Обычный посох', 'ranged': False, 'two-handed': True, 'crit': 2, 'speed': 1,
         'skill': '1/2хКопья/Посох',
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    '2хМеч':
        {'name': 'Обычный 2х меч', 'ranged': False, 'two-handed': True, 'crit': 2, 'speed': 1, 'skill': '2хКлинки',
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 1, 'health_damage': 6},
    '2хКопьё':
        {'name': 'Обычное 2х копьё', 'ranged': False, 'two-handed': True, 'crit': 2, 'speed': 1,
         'skill': '1/2хКопья/Посох',
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 2, 'health_damage': 5},
    '2хТопор':
        {'name': 'Обычный 2х топор', 'ranged': False, 'two-handed': True, 'crit': 2, 'speed': 1, 'skill': '2хУдарное',
         'magic_damage': 0, 'armor_damage': 5, 'penetration_damage': 4, 'health_damage': 4},
    '2хМолот':
        {'name': 'Обычный 2х молот', 'ranged': False, 'two-handed': True, 'crit': 2, 'speed': 1, 'skill': '2хУдарное',
         'magic_damage': 0, 'armor_damage': 7, 'penetration_damage': 2, 'health_damage': 4},
    'Метательное':
        {'name': 'Обычное метательное оружие', 'ranged': True, 'two-handed': False, 'crit': 4, 'speed': 2,
         'skill': 'Единоборства',
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 2},
    'Пистолет':
        {'name': 'Обычный пистолет', 'ranged': True, 'two-handed': False, 'crit': 2, 'speed': 1, 'skill': '1хПистолеты',
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 2, 'health_damage': 3},
    'Лук':
        {'name': 'Обычный лук', 'ranged': True, 'two-handed': True, 'crit': 2, 'speed': 1, 'skill': '2хЛук',
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 3},
    'Праща':
        {'name': 'Обычная праща', 'ranged': True, 'two-handed': True, 'crit': 2, 'speed': 1, 'skill': '2хПраща',
         'magic_damage': 0, 'armor_damage': 1, 'penetration_damage': 1, 'health_damage': 3},
    'Арбалет':
        {'name': 'Обычный арбалет', 'ranged': True, 'two-handed': True, 'crit': 2, 'speed': 1, 'skill': '2хАрбалет',
         'magic_damage': 0, 'armor_damage': 3, 'penetration_damage': 5, 'health_damage': 6},
    'Ружьё':
        {'name': 'Обычное ружьё', 'ranged': True, 'two-handed': True, 'crit': 2, 'speed': 1, 'skill': '2хРужья',
         'magic_damage': 0, 'armor_damage': 2, 'penetration_damage': 6, 'health_damage': 6},
    'Щит':
        {'name': 'Обычный щит', 'ranged': False, 'two-handed': False, 'crit': 2, 'speed': 1,
         'skill': 'Навык оружия в другой руке',
         'magic_damage': 0, 'armor_damage': 0, 'penetration_damage': 0, 'health_damage': 0},
}

weapons_list = list(weapons_dict.keys())

weapons_one_hand_melee_list = []
for weapon in weapons_list:
    if not weapons_dict[weapon]['ranged'] and not weapons_dict[weapon]['two-handed']:
        weapons_one_hand_melee_list.append(weapon)

weapons_two_hand_melee_list = []
for weapon in weapons_list:
    if not weapons_dict[weapon]['ranged'] and weapons_dict[weapon]['two-handed']:
        weapons_two_hand_melee_list.append(weapon)

weapons_one_hand_range_list = []
for weapon in weapons_list:
    if weapons_dict[weapon]['ranged'] and not weapons_dict[weapon]['two-handed']:
        weapons_one_hand_range_list.append(weapon)

weapons_two_hand_range_list = []
for weapon in weapons_list:
    if weapons_dict[weapon]['ranged'] and weapons_dict[weapon]['two-handed']:
        weapons_two_hand_range_list.append(weapon)

weapons_types_dict = {
    'Одноручное оружие ближнего боя': weapons_one_hand_melee_list,
    'Двуручное оружие ближнего боя': weapons_two_hand_melee_list,
    'Одноручное оружие дальнего боя': weapons_one_hand_range_list,
    'Двуручное оружие дальнего боя': weapons_two_hand_range_list
}

weapons_types_list = list(weapons_types_dict.keys())

plate_dict = {  # шкура. Название: значение брони
    'Без лат': 0,
    'Ржавый доспех': 4,
    'Обычный доспех': 9,
    'Хороший доспех': 12,
    'Отличный доспех': 17,
    'Эпический доспех': 25,
    'Легендарный доспех': 50,
}

plate_list = list(plate_dict.keys())

loot_dict = {
    1: ['Отмычки х2', 'Ткань', 'Солонина', 'Бекон', 'Морковь', 'Сыр', 'Вода', 'Нож', 'Бинт', 'Картоха', 'Рюмка',
        'Карты', 'Флейта', 'Медное кольцо', 'Медный браслет', 'Железная цепочка', 'Железный браслет',
        'Железное кольцо'],
    2: ['Золотые часы', 'Антисептик', 'Книжка (обычн.)', 'Золотое кольцо', 'Серебряное кольцо', 'Золотая цепочка',
        'Серебряная цепочка', 'Золотой браслет', 'Серебряный браслет', 'Наркотики'],
    3: ['Изумруд', 'Сапфир', 'Гранат', 'Бриллиант', 'Кольцо с камнем', 'Браслет с инкрустацией', 'Кулон с камнем',
        'Книга знаний...', 'Свиток заклинаний...', 'Учебник...'],
}
