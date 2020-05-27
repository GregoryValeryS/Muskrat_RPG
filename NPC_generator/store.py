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


def main():
    NPC = Person('ru')
    text = Text('ru')
    type_ragger = {'type_translation': 'Оборванец',
                   'level_range': randint(1, 5),
                   'gender': choice(['М', 'Ж']),
                   'name_male': NPC.name(gender=Gender.MALE),
                   'last_name_male': NPC.last_name(gender=Gender.MALE),
                   'name_male': NPC.name(gender=Gender.FEMALE),
                   'last_name_female': NPC.last_name(gender=Gender.FEMALE),
                   'nick': text.swear_word(),
                   'name_more': " "}
    print(type_ragger)
    print(type_ragger)
    types = []

male_or_female = ['М', 'Ж']
male_or_female_or_something = ['М', 'Ж', '?']


