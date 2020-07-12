import sys
from math import ceil, floor
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main_menu import Ui_MainWindow
from ui_NPC_widget import Ui_NPC_Widget
from mimesis import Person
from mimesis.enums import Gender
from mimesis import Text
from random import randint, choice
from store import \
    NPC_types_dict, NPC_types_list, \
    talents_dict, talents_list, \
    skills_dict, skills_type_list, skills_list, skills_list_noncombat, skills_list_ranged, skills_list_melee, \
    spells_dict, spells_list, \
    plate_dict, plate_list, \
    weapons_dict, weapons_list, weapons_types_dict, weapons_types_list, \
    loot_dict

# под этим условием лежит сегмет программы, содержащий функции кнопок, передающие номер окна в действующую функцию
# и функцию инцииализации всех кнопок виджета
if True:
    def pushbutton_info_0():
        pushbutton_info(0)


    def pushbutton_info_1():
        pushbutton_info(1)


    def pushbutton_info_2():
        pushbutton_info(2)


    def pushbutton_info_3():
        pushbutton_info(3)


    def pushbutton_info_4():
        pushbutton_info(4)


    def pushbutton_info_5():
        pushbutton_info(5)


    def pushbutton_info_6():
        pushbutton_info(6)


    def pushbutton_info_7():
        pushbutton_info(7)


    def pushbutton_info_8():
        pushbutton_info(8)


    def pushbutton_info_9():
        pushbutton_info(9)


    def pushbutton_generation_0():
        pushbutton_generation(0)


    def pushbutton_generation_1():
        pushbutton_generation(1)


    def pushbutton_generation_2():
        pushbutton_generation(2)


    def pushbutton_generation_3():
        pushbutton_generation(3)


    def pushbutton_generation_4():
        pushbutton_generation(4)


    def pushbutton_generation_5():
        pushbutton_generation(5)


    def pushbutton_generation_6():
        pushbutton_generation(6)


    def pushbutton_generation_7():
        pushbutton_generation(7)


    def pushbutton_generation_8():
        pushbutton_generation(8)


    def pushbutton_generation_9():
        pushbutton_generation(9)


    def pushbutton_reset_0():
        pushbutton_reset(0)


    def pushbutton_reset_1():
        pushbutton_reset(1)


    def pushbutton_reset_2():
        pushbutton_reset(2)


    def pushbutton_reset_3():
        pushbutton_reset(3)


    def pushbutton_reset_4():
        pushbutton_reset(4)


    def pushbutton_reset_5():
        pushbutton_reset(5)


    def pushbutton_reset_6():
        pushbutton_reset(6)


    def pushbutton_reset_7():
        pushbutton_reset(7)


    def pushbutton_reset_8():
        pushbutton_reset(8)


    def pushbutton_reset_9():
        pushbutton_reset(9)


    def pushbutton_load_0():
        pushbutton_load(0)


    def pushbutton_load_1():
        pushbutton_load(1)


    def pushbutton_load_2():
        pushbutton_load(2)


    def pushbutton_load_3():
        pushbutton_load(3)


    def pushbutton_load_4():
        pushbutton_load(4)


    def pushbutton_load_5():
        pushbutton_load(5)


    def pushbutton_load_6():
        pushbutton_load(6)


    def pushbutton_load_7():
        pushbutton_load(7)


    def pushbutton_load_8():
        pushbutton_load(8)


    def pushbutton_load_9():
        pushbutton_load(9)


    def pushbutton_save_0():
        pushbutton_save(0)


    def pushbutton_save_1():
        pushbutton_save(1)


    def pushbutton_save_2():
        pushbutton_save(2)


    def pushbutton_save_3():
        pushbutton_save(3)


    def pushbutton_save_4():
        pushbutton_save(4)


    def pushbutton_save_5():
        pushbutton_save(5)


    def pushbutton_save_6():
        pushbutton_save(6)


    def pushbutton_save_7():
        pushbutton_save(7)


    def pushbutton_save_8():
        pushbutton_save(8)


    def pushbutton_save_9():
        pushbutton_save(9)


    def pushbutton_incoming_damage_enter_0():
        pushbutton_incoming_damage_enter(0)


    def pushbutton_incoming_damage_enter_1():
        pushbutton_incoming_damage_enter(1)


    def pushbutton_incoming_damage_enter_2():
        pushbutton_incoming_damage_enter(2)


    def pushbutton_incoming_damage_enter_3():
        pushbutton_incoming_damage_enter(3)


    def pushbutton_incoming_damage_enter_4():
        pushbutton_incoming_damage_enter(4)


    def pushbutton_incoming_damage_enter_5():
        pushbutton_incoming_damage_enter(5)


    def pushbutton_incoming_damage_enter_6():
        pushbutton_incoming_damage_enter(6)


    def pushbutton_incoming_damage_enter_7():
        pushbutton_incoming_damage_enter(7)


    def pushbutton_incoming_damage_enter_8():
        pushbutton_incoming_damage_enter(8)


    def pushbutton_incoming_damage_enter_9():
        pushbutton_incoming_damage_enter(9)


    def pushbutton_incoming_heal_enter_0():
        pushbutton_incoming_heal_enter(0)


    def pushbutton_incoming_heal_enter_1():
        pushbutton_incoming_heal_enter(1)


    def pushbutton_incoming_heal_enter_2():
        pushbutton_incoming_heal_enter(2)


    def pushbutton_incoming_heal_enter_3():
        pushbutton_incoming_heal_enter(3)


    def pushbutton_incoming_heal_enter_4():
        pushbutton_incoming_heal_enter(4)


    def pushbutton_incoming_heal_enter_5():
        pushbutton_incoming_heal_enter(5)


    def pushbutton_incoming_heal_enter_6():
        pushbutton_incoming_heal_enter(6)


    def pushbutton_incoming_heal_enter_7():
        pushbutton_incoming_heal_enter(7)


    def pushbutton_incoming_heal_enter_8():
        pushbutton_incoming_heal_enter(8)


    def pushbutton_incoming_heal_enter_9():
        pushbutton_incoming_heal_enter(9)


    def pushbutton_attack_0():
        pushbutton_attack(0)


    def pushbutton_attack_1():
        pushbutton_attack(1)


    def pushbutton_attack_2():
        pushbutton_attack(2)


    def pushbutton_attack_3():
        pushbutton_attack(3)


    def pushbutton_attack_4():
        pushbutton_attack(4)


    def pushbutton_attack_5():
        pushbutton_attack(5)


    def pushbutton_attack_6():
        pushbutton_attack(6)


    def pushbutton_attack_7():
        pushbutton_attack(7)


    def pushbutton_attack_8():
        pushbutton_attack(8)


    def pushbutton_attack_9():
        pushbutton_attack(9)


    def pushbutton_d20_physique_0():
        D20_roll(0, 'Телосложение',
                 widget[0].lineEdit_physique.text())  # i: int, characteristic: str, characteristic_value: str


    def pushbutton_d20_physique_1():
        D20_roll(1, 'Телосложение', widget[1].lineEdit_physique.text())


    def pushbutton_d20_physique_2():
        D20_roll(2, 'Телосложение', widget[2].lineEdit_physique.text())


    def pushbutton_d20_physique_3():
        D20_roll(3, 'Телосложение', widget[3].lineEdit_physique.text())


    def pushbutton_d20_physique_4():
        D20_roll(4, 'Телосложение', widget[4].lineEdit_physique.text())


    def pushbutton_d20_physique_5():
        D20_roll(5, 'Телосложение', widget[5].lineEdit_physique.text())


    def pushbutton_d20_physique_6():
        D20_roll(6, 'Телосложение', widget[6].lineEdit_physique.text())


    def pushbutton_d20_physique_7():
        D20_roll(7, 'Телосложение', widget[7].lineEdit_physique.text())


    def pushbutton_d20_physique_8():
        D20_roll(8, 'Телосложение', widget[8].lineEdit_physique.text())


    def pushbutton_d20_physique_9():
        D20_roll(9, 'Телосложение', widget[9].lineEdit_physique.text())


    def pushbutton_d20_mastery_0():
        D20_roll(0, 'Мастерство', widget[0].lineEdit_mastery.text())


    def pushbutton_d20_mastery_1():
        D20_roll(1, 'Мастерство', widget[1].lineEdit_mastery.text())


    def pushbutton_d20_mastery_2():
        D20_roll(2, 'Мастерство', widget[2].lineEdit_mastery.text())


    def pushbutton_d20_mastery_3():
        D20_roll(3, 'Мастерство', widget[3].lineEdit_mastery.text())


    def pushbutton_d20_mastery_4():
        D20_roll(4, 'Мастерство', widget[4].lineEdit_mastery.text())


    def pushbutton_d20_mastery_5():
        D20_roll(5, 'Мастерство', widget[5].lineEdit_mastery.text())


    def pushbutton_d20_mastery_6():
        D20_roll(6, 'Мастерство', widget[6].lineEdit_mastery.text())


    def pushbutton_d20_mastery_7():
        D20_roll(7, 'Мастерство', widget[7].lineEdit_mastery.text())


    def pushbutton_d20_mastery_8():
        D20_roll(8, 'Мастерство', widget[8].lineEdit_mastery.text())


    def pushbutton_d20_mastery_9():
        D20_roll(9, 'Мастерство', widget[9].lineEdit_mastery.text())


    def pushbutton_d20_skill_1_0():
        D20_roll(0, widget[0].comboBox_skill_1.currentText(), widget[0].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_1():
        D20_roll(1, widget[1].comboBox_skill_1.currentText(), widget[1].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_2():
        D20_roll(2, widget[2].comboBox_skill_1.currentText(), widget[2].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_3():
        D20_roll(3, widget[3].comboBox_skill_1.currentText(), widget[3].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_4():
        D20_roll(4, widget[4].comboBox_skill_1.currentText(), widget[4].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_5():
        D20_roll(5, widget[5].comboBox_skill_1.currentText(), widget[5].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_6():
        D20_roll(6, widget[6].comboBox_skill_1.currentText(), widget[6].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_7():
        D20_roll(7, widget[7].comboBox_skill_1.currentText(), widget[7].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_8():
        D20_roll(8, widget[8].comboBox_skill_1.currentText(), widget[8].lineEdit_skill_1.text())


    def pushbutton_d20_skill_1_9():
        D20_roll(9, widget[9].comboBox_skill_1.currentText(), widget[9].lineEdit_skill_1.text())


    def pushbutton_d20_skill_2_0():
        D20_roll(0, widget[0].comboBox_skill_2.currentText(), widget[0].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_1():
        D20_roll(1, widget[1].comboBox_skill_2.currentText(), widget[1].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_2():
        D20_roll(2, widget[2].comboBox_skill_2.currentText(), widget[2].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_3():
        D20_roll(3, widget[3].comboBox_skill_2.currentText(), widget[3].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_4():
        D20_roll(4, widget[4].comboBox_skill_2.currentText(), widget[4].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_5():
        D20_roll(5, widget[5].comboBox_skill_2.currentText(), widget[5].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_6():
        D20_roll(6, widget[6].comboBox_skill_2.currentText(), widget[6].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_7():
        D20_roll(7, widget[7].comboBox_skill_2.currentText(), widget[7].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_8():
        D20_roll(8, widget[8].comboBox_skill_2.currentText(), widget[8].lineEdit_skill_2.text())


    def pushbutton_d20_skill_2_9():
        D20_roll(9, widget[9].comboBox_skill_2.currentText(), widget[9].lineEdit_skill_2.text())


    def pushbutton_d20_skill_3_0():
        D20_roll(0, widget[0].comboBox_skill_3.currentText(), widget[0].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_1():
        D20_roll(1, widget[1].comboBox_skill_3.currentText(), widget[1].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_2():
        D20_roll(2, widget[2].comboBox_skill_3.currentText(), widget[2].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_3():
        D20_roll(3, widget[3].comboBox_skill_3.currentText(), widget[3].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_4():
        D20_roll(4, widget[4].comboBox_skill_3.currentText(), widget[4].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_5():
        D20_roll(5, widget[5].comboBox_skill_3.currentText(), widget[5].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_6():
        D20_roll(6, widget[6].comboBox_skill_3.currentText(), widget[6].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_7():
        D20_roll(7, widget[7].comboBox_skill_3.currentText(), widget[7].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_8():
        D20_roll(8, widget[8].comboBox_skill_3.currentText(), widget[8].lineEdit_skill_3.text())


    def pushbutton_d20_skill_3_9():
        D20_roll(9, widget[9].comboBox_skill_3.currentText(), widget[9].lineEdit_skill_3.text())


    def pushbutton_d20_skill_4_0():
        D20_roll(0, widget[0].comboBox_skill_4.currentText(), widget[0].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_1():
        D20_roll(1, widget[1].comboBox_skill_4.currentText(), widget[1].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_2():
        D20_roll(2, widget[2].comboBox_skill_4.currentText(), widget[2].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_3():
        D20_roll(3, widget[3].comboBox_skill_4.currentText(), widget[3].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_4():
        D20_roll(4, widget[4].comboBox_skill_4.currentText(), widget[4].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_5():
        D20_roll(5, widget[5].comboBox_skill_4.currentText(), widget[5].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_6():
        D20_roll(6, widget[6].comboBox_skill_4.currentText(), widget[6].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_7():
        D20_roll(7, widget[7].comboBox_skill_4.currentText(), widget[7].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_8():
        D20_roll(8, widget[8].comboBox_skill_4.currentText(), widget[8].lineEdit_skill_4.text())


    def pushbutton_d20_skill_4_9():
        D20_roll(9, widget[9].comboBox_skill_4.currentText(), widget[9].lineEdit_skill_4.text())


    def pushbutton_d20_intelligence_0():
        D20_roll(0, 'Интеллект', widget[0].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_1():
        D20_roll(1, 'Интеллект', widget[1].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_2():
        D20_roll(2, 'Интеллект', widget[2].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_3():
        D20_roll(3, 'Интеллект', widget[3].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_4():
        D20_roll(4, 'Интеллект', widget[4].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_5():
        D20_roll(5, 'Интеллект', widget[5].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_6():
        D20_roll(6, 'Интеллект', widget[6].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_7():
        D20_roll(7, 'Интеллект', widget[7].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_8():
        D20_roll(8, 'Интеллект', widget[8].lineEdit_intelligence.text())


    def pushbutton_d20_intelligence_9():
        D20_roll(9, 'Интеллект', widget[9].lineEdit_intelligence.text())


    def pushbutton_d20_spell_1_0():
        D20_roll(0, widget[0].comboBox_spell_1.currentText(), widget[0].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_1():
        D20_roll(1, widget[1].comboBox_spell_1.currentText(), widget[1].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_2():
        D20_roll(2, widget[2].comboBox_spell_1.currentText(), widget[2].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_3():
        D20_roll(3, widget[3].comboBox_spell_1.currentText(), widget[3].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_4():
        D20_roll(4, widget[4].comboBox_spell_1.currentText(), widget[4].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_5():
        D20_roll(5, widget[5].comboBox_spell_1.currentText(), widget[5].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_6():
        D20_roll(6, widget[6].comboBox_spell_1.currentText(), widget[6].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_7():
        D20_roll(7, widget[7].comboBox_spell_1.currentText(), widget[7].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_8():
        D20_roll(8, widget[8].comboBox_spell_1.currentText(), widget[8].lineEdit_spell_1.text())


    def pushbutton_d20_spell_1_9():
        D20_roll(9, widget[9].comboBox_spell_1.currentText(), widget[9].lineEdit_spell_1.text())


    def pushbutton_d20_spell_2_0():
        D20_roll(0, widget[0].comboBox_spell_2.currentText(), widget[0].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_1():
        D20_roll(1, widget[1].comboBox_spell_2.currentText(), widget[1].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_2():
        D20_roll(2, widget[2].comboBox_spell_2.currentText(), widget[2].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_3():
        D20_roll(3, widget[3].comboBox_spell_2.currentText(), widget[3].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_4():
        D20_roll(4, widget[4].comboBox_spell_2.currentText(), widget[4].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_5():
        D20_roll(5, widget[5].comboBox_spell_2.currentText(), widget[5].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_6():
        D20_roll(6, widget[6].comboBox_spell_2.currentText(), widget[6].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_7():
        D20_roll(7, widget[7].comboBox_spell_2.currentText(), widget[7].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_8():
        D20_roll(8, widget[8].comboBox_spell_2.currentText(), widget[8].lineEdit_spell_2.text())


    def pushbutton_d20_spell_2_9():
        D20_roll(9, widget[9].comboBox_spell_2.currentText(), widget[9].lineEdit_spell_2.text())


    def pushbutton_d20_spell_3_0():
        D20_roll(0, widget[0].comboBox_spell_3.currentText(), widget[0].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_1():
        D20_roll(1, widget[1].comboBox_spell_3.currentText(), widget[1].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_2():
        D20_roll(2, widget[2].comboBox_spell_3.currentText(), widget[2].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_3():
        D20_roll(3, widget[3].comboBox_spell_3.currentText(), widget[3].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_4():
        D20_roll(4, widget[4].comboBox_spell_3.currentText(), widget[4].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_5():
        D20_roll(5, widget[5].comboBox_spell_3.currentText(), widget[5].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_6():
        D20_roll(6, widget[6].comboBox_spell_3.currentText(), widget[6].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_7():
        D20_roll(7, widget[7].comboBox_spell_3.currentText(), widget[7].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_8():
        D20_roll(8, widget[8].comboBox_spell_3.currentText(), widget[8].lineEdit_spell_3.text())


    def pushbutton_d20_spell_3_9():
        D20_roll(9, widget[9].comboBox_spell_3.currentText(), widget[9].lineEdit_spell_3.text())


    def pushbutton_d20_spell_4_0():
        D20_roll(0, widget[0].comboBox_spell_4.currentText(), widget[0].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_1():
        D20_roll(1, widget[1].comboBox_spell_4.currentText(), widget[1].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_2():
        D20_roll(2, widget[2].comboBox_spell_4.currentText(), widget[2].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_3():
        D20_roll(3, widget[3].comboBox_spell_4.currentText(), widget[3].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_4():
        D20_roll(4, widget[4].comboBox_spell_4.currentText(), widget[4].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_5():
        D20_roll(5, widget[5].comboBox_spell_4.currentText(), widget[5].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_6():
        D20_roll(6, widget[6].comboBox_spell_4.currentText(), widget[6].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_7():
        D20_roll(7, widget[7].comboBox_spell_4.currentText(), widget[7].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_8():
        D20_roll(8, widget[8].comboBox_spell_4.currentText(), widget[8].lineEdit_spell_4.text())


    def pushbutton_d20_spell_4_9():
        D20_roll(9, widget[9].comboBox_spell_4.currentText(), widget[9].lineEdit_spell_4.text())


    def pushbutton_d20_spell_5_0():
        D20_roll(0, widget[0].comboBox_spell_5.currentText(), widget[0].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_1():
        D20_roll(1, widget[1].comboBox_spell_5.currentText(), widget[1].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_2():
        D20_roll(2, widget[2].comboBox_spell_5.currentText(), widget[2].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_3():
        D20_roll(3, widget[3].comboBox_spell_5.currentText(), widget[3].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_4():
        D20_roll(4, widget[4].comboBox_spell_5.currentText(), widget[4].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_5():
        D20_roll(5, widget[5].comboBox_spell_5.currentText(), widget[5].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_6():
        D20_roll(6, widget[6].comboBox_spell_5.currentText(), widget[6].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_7():
        D20_roll(7, widget[7].comboBox_spell_5.currentText(), widget[7].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_8():
        D20_roll(8, widget[8].comboBox_spell_5.currentText(), widget[8].lineEdit_spell_5.text())


    def pushbutton_d20_spell_5_9():
        D20_roll(9, widget[9].comboBox_spell_5.currentText(), widget[9].lineEdit_spell_5.text())


    def init_widget_buttons():
        """функция инцииализации всех кнопок виджета"""
        widget[0].pushButton_info.clicked.connect(pushbutton_info_0)
        widget[0].pushButton_generation.clicked.connect(pushbutton_generation_0)
        widget[0].pushButton_reset.clicked.connect(pushbutton_reset_0)
        widget[0].pushButton_load.clicked.connect(pushbutton_load_0)
        widget[0].pushButton_save.clicked.connect(pushbutton_save_0)
        widget[0].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_0)
        widget[0].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_0)
        widget[0].pushButton_attack.clicked.connect(pushbutton_attack_0)
        widget[0].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_0)
        widget[0].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_0)
        widget[0].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_0)
        widget[0].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_0)
        widget[0].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_0)
        widget[0].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_0)
        widget[0].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_0)
        widget[0].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_0)
        widget[0].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_0)
        widget[0].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_0)
        widget[0].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_0)
        widget[0].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_0)

        widget[1].pushButton_info.clicked.connect(pushbutton_info_1)
        widget[1].pushButton_generation.clicked.connect(pushbutton_generation_1)
        widget[1].pushButton_reset.clicked.connect(pushbutton_reset_1)
        widget[1].pushButton_load.clicked.connect(pushbutton_load_1)
        widget[1].pushButton_save.clicked.connect(pushbutton_save_1)
        widget[1].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_1)
        widget[1].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_1)
        widget[1].pushButton_attack.clicked.connect(pushbutton_attack_1)
        widget[1].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_1)
        widget[1].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_1)
        widget[1].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_1)
        widget[1].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_1)
        widget[1].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_1)
        widget[1].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_1)
        widget[1].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_1)
        widget[1].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_1)
        widget[1].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_1)
        widget[1].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_1)
        widget[1].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_1)
        widget[1].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_1)

        widget[2].pushButton_info.clicked.connect(pushbutton_info_2)
        widget[2].pushButton_generation.clicked.connect(pushbutton_generation_2)
        widget[2].pushButton_reset.clicked.connect(pushbutton_reset_2)
        widget[2].pushButton_load.clicked.connect(pushbutton_load_2)
        widget[2].pushButton_save.clicked.connect(pushbutton_save_2)
        widget[2].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_2)
        widget[2].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_2)
        widget[2].pushButton_attack.clicked.connect(pushbutton_attack_2)
        widget[2].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_2)
        widget[2].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_2)
        widget[2].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_2)
        widget[2].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_2)
        widget[2].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_2)
        widget[2].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_2)
        widget[2].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_2)
        widget[2].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_2)
        widget[2].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_2)
        widget[2].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_2)
        widget[2].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_2)
        widget[2].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_2)

        widget[3].pushButton_info.clicked.connect(pushbutton_info_3)
        widget[3].pushButton_generation.clicked.connect(pushbutton_generation_3)
        widget[3].pushButton_reset.clicked.connect(pushbutton_reset_3)
        widget[3].pushButton_load.clicked.connect(pushbutton_load_3)
        widget[3].pushButton_save.clicked.connect(pushbutton_save_3)
        widget[3].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_3)
        widget[3].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_3)
        widget[3].pushButton_attack.clicked.connect(pushbutton_attack_3)
        widget[3].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_3)
        widget[3].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_3)
        widget[3].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_3)
        widget[3].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_3)
        widget[3].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_3)
        widget[3].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_3)
        widget[3].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_3)
        widget[3].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_3)
        widget[3].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_3)
        widget[3].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_3)
        widget[3].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_3)
        widget[3].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_3)

        widget[4].pushButton_info.clicked.connect(pushbutton_info_4)
        widget[4].pushButton_generation.clicked.connect(pushbutton_generation_4)
        widget[4].pushButton_reset.clicked.connect(pushbutton_reset_4)
        widget[4].pushButton_load.clicked.connect(pushbutton_load_4)
        widget[4].pushButton_save.clicked.connect(pushbutton_save_4)
        widget[4].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_4)
        widget[4].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_4)
        widget[4].pushButton_attack.clicked.connect(pushbutton_attack_4)
        widget[4].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_4)
        widget[4].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_4)
        widget[4].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_4)
        widget[4].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_4)
        widget[4].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_4)
        widget[4].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_4)
        widget[4].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_4)
        widget[4].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_4)
        widget[4].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_4)
        widget[4].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_4)
        widget[4].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_4)
        widget[4].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_4)

        widget[5].pushButton_info.clicked.connect(pushbutton_info_5)
        widget[5].pushButton_generation.clicked.connect(pushbutton_generation_5)
        widget[5].pushButton_reset.clicked.connect(pushbutton_reset_5)
        widget[5].pushButton_load.clicked.connect(pushbutton_load_5)
        widget[5].pushButton_save.clicked.connect(pushbutton_save_5)
        widget[5].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_5)
        widget[5].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_5)
        widget[5].pushButton_attack.clicked.connect(pushbutton_attack_5)
        widget[5].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_5)
        widget[5].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_5)
        widget[5].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_5)
        widget[5].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_5)
        widget[5].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_5)
        widget[5].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_5)
        widget[5].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_5)
        widget[5].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_5)
        widget[5].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_5)
        widget[5].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_5)
        widget[5].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_5)
        widget[5].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_5)

        widget[6].pushButton_info.clicked.connect(pushbutton_info_6)
        widget[6].pushButton_generation.clicked.connect(pushbutton_generation_6)
        widget[6].pushButton_reset.clicked.connect(pushbutton_reset_6)
        widget[6].pushButton_load.clicked.connect(pushbutton_load_6)
        widget[6].pushButton_save.clicked.connect(pushbutton_save_6)
        widget[6].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_6)
        widget[6].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_6)
        widget[6].pushButton_attack.clicked.connect(pushbutton_attack_6)
        widget[6].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_6)
        widget[6].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_6)
        widget[6].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_6)
        widget[6].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_6)
        widget[6].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_6)
        widget[6].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_6)
        widget[6].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_6)
        widget[6].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_6)
        widget[6].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_6)
        widget[6].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_6)
        widget[6].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_6)
        widget[6].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_6)

        widget[7].pushButton_info.clicked.connect(pushbutton_info_7)
        widget[7].pushButton_generation.clicked.connect(pushbutton_generation_7)
        widget[7].pushButton_reset.clicked.connect(pushbutton_reset_7)
        widget[7].pushButton_load.clicked.connect(pushbutton_load_7)
        widget[7].pushButton_save.clicked.connect(pushbutton_save_7)
        widget[7].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_7)
        widget[7].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_7)
        widget[7].pushButton_attack.clicked.connect(pushbutton_attack_7)
        widget[7].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_7)
        widget[7].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_7)
        widget[7].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_7)
        widget[7].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_7)
        widget[7].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_7)
        widget[7].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_7)
        widget[7].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_7)
        widget[7].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_7)
        widget[7].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_7)
        widget[7].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_7)
        widget[7].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_7)
        widget[7].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_7)

        widget[8].pushButton_info.clicked.connect(pushbutton_info_8)
        widget[8].pushButton_generation.clicked.connect(pushbutton_generation_8)
        widget[8].pushButton_reset.clicked.connect(pushbutton_reset_8)
        widget[8].pushButton_load.clicked.connect(pushbutton_load_8)
        widget[8].pushButton_save.clicked.connect(pushbutton_save_8)
        widget[8].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_8)
        widget[8].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_8)
        widget[8].pushButton_attack.clicked.connect(pushbutton_attack_8)
        widget[8].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_8)
        widget[8].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_8)
        widget[8].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_8)
        widget[8].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_8)
        widget[8].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_8)
        widget[8].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_8)
        widget[8].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_8)
        widget[8].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_8)
        widget[8].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_8)
        widget[8].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_8)
        widget[8].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_8)
        widget[8].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_8)

        widget[9].pushButton_info.clicked.connect(pushbutton_info_9)
        widget[9].pushButton_generation.clicked.connect(pushbutton_generation_9)
        widget[9].pushButton_reset.clicked.connect(pushbutton_reset_9)
        widget[9].pushButton_load.clicked.connect(pushbutton_load_9)
        widget[9].pushButton_save.clicked.connect(pushbutton_save_9)
        widget[9].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_9)
        widget[9].pushButton_incoming_heal_enter.clicked.connect(pushbutton_incoming_heal_enter_9)
        widget[9].pushButton_attack.clicked.connect(pushbutton_attack_9)
        widget[9].pushButton_d20_physique.clicked.connect(pushbutton_d20_physique_9)
        widget[9].pushButton_d20_mastery.clicked.connect(pushbutton_d20_mastery_9)
        widget[9].pushButton_d20_skill_1.clicked.connect(pushbutton_d20_skill_1_9)
        widget[9].pushButton_d20_skill_2.clicked.connect(pushbutton_d20_skill_2_9)
        widget[9].pushButton_d20_skill_3.clicked.connect(pushbutton_d20_skill_3_9)
        widget[9].pushButton_d20_skill_4.clicked.connect(pushbutton_d20_skill_4_9)
        widget[9].pushButton_d20_intelligence.clicked.connect(pushbutton_d20_intelligence_9)
        widget[9].pushButton_d20_spell_1.clicked.connect(pushbutton_d20_spell_1_9)
        widget[9].pushButton_d20_spell_2.clicked.connect(pushbutton_d20_spell_2_9)
        widget[9].pushButton_d20_spell_3.clicked.connect(pushbutton_d20_spell_3_9)
        widget[9].pushButton_d20_spell_4.clicked.connect(pushbutton_d20_spell_4_9)
        widget[9].pushButton_d20_spell_5.clicked.connect(pushbutton_d20_spell_5_9)  #


def pushbutton_add_npc():
    global widgets_counter
    if widgets_counter <= 9:
        WidgetNPС[widgets_counter].show()
        widgets_counter += 1


def pushbutton_remove_npc():
    global widgets_counter
    if widgets_counter >= 1:
        widgets_counter -= 1
        WidgetNPС[widgets_counter].close()


def pushbutton_store_talents():
    main_menu.textEdit_battlelog.append('~~~~Полный перечень талантов~~~~')
    n = 1
    for talent in talents_list:
        main_menu.textEdit_battlelog.append(' ' + str(n) + ') ' + talent + ' - ' + talents_dict[talent])
        n += 1
    main_menu.textEdit_battlelog.append("~~~~~~~~~~~~~~~~~~~~~~~")


def pushbutton_store_skills():
    main_menu.textEdit_battlelog.append('~~~~Полный перечень навыков~~~~')
    for skills_type in skills_type_list:
        main_menu.textEdit_battlelog.append(skills_type+':')
        n = 1
        for skill in skills_dict[skills_type]:
            main_menu.textEdit_battlelog.append(' ' + str(n) +') ' + skill)
            n += 1
    main_menu.textEdit_battlelog.append("~~~~~~~~~~~~~~~~~~~~~~~")


def pushbutton_store_spells():
    main_menu.textEdit_battlelog.append('~~~~Полный перечень заклинаний~~~~')
    n = 1
    for spell in spells_list:
        main_menu.textEdit_battlelog.append(' ' + str(n) + ') ' + spell + ' - ' + spells_dict[spell])
        n += 1
    main_menu.textEdit_battlelog.append("~~~~~~~~~~~~~~~~~~~~~~~")


def pushbutton_store_weapons():
    main_menu.textEdit_battlelog.append('~~~~Полный перечень оружия~~~~')
    n = 1
    for weapons_type in weapons_types_list:
        main_menu.textEdit_battlelog.append(weapons_type + ':')
        for weapon in weapons_types_dict[weapons_type]:
            main_menu.textEdit_battlelog.append(f" {str(n)}) {weapon}: ключевой навык - '{weapons_dict[weapon]['skill']}',\n"
                                                f"         скорость - {weapons_dict[weapon]['speed']},"
                                                f" множитель крита - {weapons_dict[weapon]['crit']},\n"
                                                f"         маг.: {weapons_dict[weapon]['magic_damage']}, "
                                                f"уд.: {weapons_dict[weapon]['armor_damage']}, "
                                                f"прон.: {weapons_dict[weapon]['penetration_damage']}, "
                                                f"здор.: {weapons_dict[weapon]['health_damage']}")
            n += 1
        main_menu.textEdit_battlelog.append("~~~~~~~~~~~~~~~~~~~~~~~")


def pushbutton_store_plates():
    main_menu.textEdit_battlelog.append('~~~~Полный перечень лат~~~~')
    n = 1
    for plate in plate_list:
        main_menu.textEdit_battlelog.append(' ' + str(n) + ') ' + plate + ' - ' + str(plate_dict[plate]))
        n += 1
    main_menu.textEdit_battlelog.append("~~~~~~~~~~~~~~~~~~~~~~~")


def pushbutton_period():
    global round_number
    round_number += 1
    main_menu.textEdit_battlelog.append(f'Начало раунда {round_number}.\n'
                                        f'NPC подвергаются влиянию перидических эффектов')
    for i in range(9):
        periodic_effects(i)


def periodic_effects(i: int):
    lines_inspector(i)
    name = widget[i].lineEdit_name.text()
    if name != '':
        health = widget[i].lineEdit_health.text()
        if health != '':
            health = int(health)
            if health > 0:
                armor = int(widget[i].lineEdit_armor.text()) \
                    if widget[i].lineEdit_armor.text() != '' else 0
                magic_barrier = int(widget[i].lineEdit_magic_barrier.text()) \
                    if widget[i].lineEdit_magic_barrier.text() != '' else 0

                periodic_damage_health = int(widget[i].lineEdit_periodic_damage_health.text()) \
                    if widget[i].lineEdit_periodic_damage_health.text() != '' else 0
                periodic_damage_penetration_damage = int(widget[i].lineEdit_periodic_damage_penetration_damage.text()) \
                    if widget[i].lineEdit_periodic_damage_penetration_damage.text() != '' else 0
                periodic_damage_armor = int(widget[i].lineEdit_periodic_damage_armor.text()) \
                    if widget[i].lineEdit_periodic_damage_armor.text() != '' else 0
                periodic_damage_magic = int(widget[i].lineEdit_periodic_damage_magic.text()) \
                    if widget[i].lineEdit_periodic_damage_magic.text() != '' else 0

                periodic_heal_health = int(widget[i].lineEdit_periodic_heal_health.text()) \
                    if widget[i].lineEdit_periodic_heal_health.text() != '' else 0
                periodic_heal_armor = int(widget[i].lineEdit_periodic_heal_armor.text()) \
                    if widget[i].lineEdit_periodic_heal_armor.text() != '' else 0
                periodic_heal_magic = int(widget[i].lineEdit_periodic_heal_magic.text()) \
                    if widget[i].lineEdit_periodic_heal_magic.text() != '' else 0

                periodic_effect_health = 0 - periodic_damage_health
                # любой хил является проникающим
                periodic_effect_penetration_damage = periodic_heal_health - periodic_damage_penetration_damage
                periodic_effect_armor = periodic_heal_armor - periodic_damage_armor
                periodic_effect_magic = periodic_heal_magic - periodic_damage_magic

                if armor > 0:
                    periodic_effect_health = 0

                # если магические щиты есть и если эффект от восстановления и разрушения щитов отрицательный, то
                # магичиский урон превращается в проникающий
                if magic_barrier == 0 and periodic_effect_magic < 0:
                    periodic_effect_penetration_damage += periodic_effect_magic

                new_health = health + periodic_effect_health + periodic_effect_penetration_damage
                if new_health <= 0:
                    new_health = 0
                    main_menu.textEdit_battlelog.append(f'{name} умирает')
                new_armor = armor + periodic_effect_armor
                if new_armor < 0:
                    new_armor = 0
                new_magic_barrier = magic_barrier + periodic_effect_magic
                if new_magic_barrier < 0:
                    new_magic_barrier = 0

                widget[i].lineEdit_health.setText(str(new_health))
                widget[i].lineEdit_armor.setText(str(new_armor))
                widget[i].lineEdit_magic_barrier.setText(str(new_magic_barrier))


def pushbutton_loot():

    class_factor = main_menu.comboBox_trash_elite_legend.currentIndex()
    lvl = main_menu.lineEdit_lvl.text()

    if class_factor != 0 and lvl != '':

        this_loot = []
        points = int(lvl)
        while points > 0:
            for item_key in range(class_factor, 0, -1):
                if points <= 0:
                    break
                this_loot.append(choice(loot_dict[item_key]))
                points -= 10

        main_menu.textEdit_battlelog.append(f'\nДобыча:')
        for item in this_loot:
            main_menu.textEdit_battlelog.append(f'{item}')
    else:
        main_menu.textEdit_battlelog.append('Выберете класс и уровень добычи')


def pushbutton_info(i: int):  # i - widget number
    lines_inspector(i)
    type = widget[i].comboBox_type.currentText()
    full_name = widget[i].lineEdit_name.text()
    gender = widget[i].comboBox_gender.currentText()
    lvl = widget[i].lineEdit_lvl.text()
    trash_elite_legend = widget[i].comboBox_trash_elite_legend.currentText()
    if type != '' and full_name != '' and gender != '' and lvl != '' and trash_elite_legend != '':

        main_menu.textEdit_battlelog.append(
            f'~~~~~  {full_name} ({gender})  ~~~~~\n'
            f'{trash_elite_legend} {type} {lvl} lvl')

        physique = widget[i].lineEdit_physique.text()

        virtual_talents_list = [widget[i].comboBox_talent_1.currentText(),
                                widget[i].comboBox_talent_2.currentText()]

        main_menu.textEdit_battlelog.append(f'\nТелосложение - {physique}. Таланты:')
        for talent in virtual_talents_list:
            if talent != '':
                main_menu.textEdit_battlelog.append(f'{talent} - {talents_dict[talent]}')

        mastery = widget[i].lineEdit_mastery.text()

        virtual_skills_list = [widget[i].comboBox_skill_1.currentText(),
                               widget[i].comboBox_skill_2.currentText(),
                               widget[i].comboBox_skill_3.currentText(),
                               widget[i].comboBox_skill_4.currentText()]

        virtual_skills_points_list = [widget[i].lineEdit_skill_1.text(),
                                      widget[i].lineEdit_skill_2.text(),
                                      widget[i].lineEdit_skill_3.text(),
                                      widget[i].lineEdit_skill_4.text()]

        main_menu.textEdit_battlelog.append(f'\nМастерство - {mastery}. Навыки:')
        for skill_index in range(0, len(virtual_skills_list)):
            if virtual_skills_list[skill_index] != '':
                main_menu.textEdit_battlelog.append(f'{virtual_skills_list[skill_index]} - {virtual_skills_points_list[skill_index]}')

        intelligence = widget[i].lineEdit_intelligence.text()

        virtual_spells_list = [widget[i].comboBox_spell_1.currentText(),
                               widget[i].comboBox_spell_2.currentText(),
                               widget[i].comboBox_spell_3.currentText(),
                               widget[i].comboBox_spell_4.currentText(),
                               widget[i].comboBox_spell_5.currentText()]

        virtual_spells_points_list = [widget[i].lineEdit_spell_1.text(),
                                      widget[i].lineEdit_spell_2.text(),
                                      widget[i].lineEdit_spell_3.text(),
                                      widget[i].lineEdit_spell_4.text(),
                                      widget[i].lineEdit_spell_5.text()]

        main_menu.textEdit_battlelog.append(f'\nИнтеллект - {intelligence}. Заклинания:')
        for spell_index in range(0, len(virtual_spells_list)):
            if virtual_spells_list[spell_index] != '':
                main_menu.textEdit_battlelog.append(f'{virtual_spells_list[spell_index]} ({virtual_spells_points_list[spell_index]}) - '
                                                    f'{spells_dict[virtual_spells_list[spell_index]]}')

        inventary = []

        weapon_1 = widget[i].comboBox_weapon_1.currentText()
        if weapon_1 != '' and weapon_1 != 'Занято' and weapon_1 != 'Без оружия':
            weapon_1_name = widget[i].lineEdit_weapon1.text()
            if weapon_1_name != '':
                inventary.append(weapon_1_name)
            else:
                inventary.append(weapon_1)

        weapon_2 = widget[i].comboBox_weapon_2.currentText()
        if weapon_2 != '' and weapon_2 != 'Занято' and weapon_2 != 'Без оружия':
            weapon_2_name = widget[i].lineEdit_weapon2.text()
            if weapon_2_name != '':
                inventary.append(weapon_2_name)
            else:
                inventary.append(weapon_2)

        plate = widget[i].comboBox_plate.currentText()
        if plate != '' and plate != 'Без лат':
            inventary.append(plate)

        main_menu.textEdit_battlelog.append(f'\nИнвентарь:')
        for item in inventary:
            if item != '':
                main_menu.textEdit_battlelog.append(f'{item}')

        this_loot = []
        class_factor = widget[i].comboBox_trash_elite_legend.currentIndex()
        points = int(lvl)
        while points > 0:
            for item_key in range(class_factor, 0, -1):
                if points <= 0:
                    break
                this_loot.append(choice(loot_dict[item_key]))
                points -= 10

        main_menu.textEdit_battlelog.append(f'\nДобыча:')
        for item in this_loot:
            main_menu.textEdit_battlelog.append(f'{item}')

        main_menu.textEdit_battlelog.append("~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        main_menu.textEdit_battlelog.append("Сгенерируйте NPC!")


def lines_inspector(i: int):  # i - widget number
    only_integro_lines_list = [  # поля, где можно вводить только положительные цифры (почти все)
        main_menu.lineEdit_lvl,

        widget[i].lineEdit_lvl,

        widget[i].lineEdit_physique,

        widget[i].lineEdit_mastery,
        widget[i].lineEdit_skill_1,
        widget[i].lineEdit_skill_2,
        widget[i].lineEdit_skill_3,
        widget[i].lineEdit_skill_4,

        widget[i].lineEdit_intelligence,
        widget[i].lineEdit_spell_1,
        widget[i].lineEdit_spell_2,
        widget[i].lineEdit_spell_3,
        widget[i].lineEdit_spell_4,
        widget[i].lineEdit_spell_5,

        widget[i].lineEdit_health,
        widget[i].lineEdit_magic_barrier,
        widget[i].lineEdit_armor,

        widget[i].lineEdit_incoming_damage_penetration_damage,
        widget[i].lineEdit_incoming_damage_magic,
        widget[i].lineEdit_incoming_damage_health,
        widget[i].lineEdit_incoming_damage_armor,

        widget[i].lineEdit_periodic_damage_armor,
        widget[i].lineEdit_periodic_damage_health,
        widget[i].lineEdit_periodic_damage_penetration_damage,
        widget[i].lineEdit_periodic_damage_magic,

        widget[i].lineEdit_incoming_heal_magic,
        widget[i].lineEdit_incoming_heal_health,
        widget[i].lineEdit_incoming_heal_armor,

        widget[i].lineEdit_periodic_heal_armor,
        widget[i].lineEdit_periodic_heal_health,
        widget[i].lineEdit_periodic_heal_magic,

        widget[i].lineEdit_weapon1_armor_damage,
        widget[i].lineEdit_weapon1_health_damage,
        widget[i].lineEdit_weapon1_magic_damage,
        widget[i].lineEdit_weapon1_penetration_damage,

        widget[i].lineEdit_weapon2_armor_damage,
        widget[i].lineEdit_weapon2_health_damage,
        widget[i].lineEdit_weapon2_magic_damage,
        widget[i].lineEdit_weapon2_penetration_damage,
    ]

    not_more_20_list = [  # поля, где можно вводить только положительные цифры (почти все)
        widget[i].lineEdit_physique,

        widget[i].lineEdit_mastery,
        widget[i].lineEdit_skill_1,
        widget[i].lineEdit_skill_2,
        widget[i].lineEdit_skill_3,
        widget[i].lineEdit_skill_4,

        widget[i].lineEdit_intelligence,
        widget[i].lineEdit_spell_1,
        widget[i].lineEdit_spell_2,
        widget[i].lineEdit_spell_3,
        widget[i].lineEdit_spell_4,
        widget[i].lineEdit_spell_5,
    ]

    for line in only_integro_lines_list:
        fixed_line = line.text().replace(' ', '').replace(',', '.')  # исправляем те ошибки, что можем
        if fixed_line.count('.') <= 1 and fixed_line.replace('.', ' ').isdigit():
            new_value = int(fixed_line)
            if new_value > 20 and line in not_more_20_list:
                new_value = 20
            line.setText(str(new_value))
        elif fixed_line == '':
            line.setText(str(fixed_line))
        else:  # чистим поля, если там не числа и не пустота
            line.clear()

    text_lines_list = [  # поля, где можно вводить только тект
        widget[i].lineEdit_name,
        widget[i].lineEdit_weapon1,
        widget[i].lineEdit_weapon2,
    ]

    for line in text_lines_list: # удаляем пробелы
        fixed_line = line.text().replace(' ', '')
        if fixed_line == '':
            line.clear()


def pushbutton_generation(i: int):  # i - widget number
    lines_inspector(i)
    # определение типа 0 - не выбрано, 1...len(NPC_types_dict) - остальные типы
    if widget[i].comboBox_type.currentIndex() == 0:  # 0 индекс - ничего не выбрано
        widget[i].comboBox_type.setCurrentIndex(randint(1, len(NPC_types_dict)))  # устанавливает случайное значение
    this_type = widget[i].comboBox_type.currentText()

    # определение пола: 0 - не выбрано, 1 - Ж, 2 - М, 3 - Н (нет)
    if widget[i].comboBox_gender.currentIndex() == 0:  # если пол не выбран
        if NPC_types_dict[this_type]['has_sex'] == 0:  # если пола нет установаить 3 - Н
            widget[i].comboBox_gender.setCurrentIndex(3)
        else:
            if randint(1, 100) >= NPC_types_dict[this_type]['male_percent']:
                widget[i].comboBox_gender.setCurrentIndex(1)
            else:
                widget[i].comboBox_gender.setCurrentIndex(2)
    gender_for_Person_list = [None, Gender.FEMALE, Gender.MALE,
                              None]  # значение для работы класса Person, для генерации имени
    gender_for_Person = gender_for_Person_list[widget[i].comboBox_gender.currentIndex()]
    this_gender = widget[i].comboBox_gender.currentText()

    # определение класса: 0 - не выбрано, 1 - Trash, 2 - Elite, 3 - Legend
    if widget[i].comboBox_trash_elite_legend.currentIndex() == 0:  # если класс не выбран
        trash_elite_legend_random = randint(1, 100)
        if trash_elite_legend_random <= NPC_types_dict[this_type]['elite_chance']:
            widget[i].comboBox_trash_elite_legend.setCurrentIndex(2)
            class_factor = 2
        elif trash_elite_legend_random <= NPC_types_dict[this_type]['elite_chance'] + \
                NPC_types_dict[this_type]['legend_chance']:
            widget[i].comboBox_trash_elite_legend.setCurrentIndex(3)
            class_factor = 3
        else:
            widget[i].comboBox_trash_elite_legend.setCurrentIndex(1)
            class_factor = 1
    this_class = widget[i].comboBox_trash_elite_legend.currentText()
    class_factor = int(widget[i].comboBox_trash_elite_legend.currentIndex())

    # подбор имени
    person = person_ru  # тут, возможно, будут варианты для других стран
    text = text_ru
    if widget[i].lineEdit_name.text() == '':  # Если в "имя" ничего не введено:
        if NPC_types_dict[this_type]['name_chance'] == 1:  # Если существу вообще положено иметь имя
            this_first_name = person.name(gender=gender_for_Person)
            this_last_name = person.last_name(gender=gender_for_Person)
            this_full_name = f"{this_first_name} {this_last_name}"
            if randint(1, 100) <= NPC_types_dict[this_type]['nick_chance']:  # будет ли кличка?
                this_nick = f"'{text.swear_word().title()}' "
            else:
                this_nick = ''
            if randint(1, 100) <= NPC_types_dict[this_type]['full_name_chance']:  # будет ли полное имя?
                widget[i].lineEdit_name.setText(f"{this_first_name} {this_nick}{this_last_name}")
            else:  # тогда имя или фамилия?
                if randint(1, 100) <= NPC_types_dict[this_type]['first_name_or_last_name']:
                    widget[i].lineEdit_name.setText(f"{this_first_name} {this_nick}")
                else:
                    widget[i].lineEdit_name.setText(f"{this_last_name} {this_nick}")
        else:
            widget[i].lineEdit_name.setText(f"{this_type}")

    # определим уровень
    if widget[i].lineEdit_lvl.text() == '':
        this_lvl = randint(NPC_types_dict[this_type]['min_lvl'], NPC_types_dict[this_type]['max_lvl'])
        widget[i].lineEdit_lvl.setText(str(this_lvl))
    else:
        this_lvl = int(widget[i].lineEdit_lvl.text())

    # определим уклон в силу или магию
    if not widget[i].radioButton_might.isChecked() and not widget[i].radioButton_magic.isChecked():
        if randint(1, 100) <= NPC_types_dict[this_type]['might_or_magic']:
            might_or_magic = 1
            widget[i].radioButton_might.setChecked(True)
        else:
            might_or_magic = 0
            widget[i].radioButton_magic.setChecked(True)
    else:
        might_or_magic = int(widget[i].radioButton_might.isChecked())  # 1 - уклон в оружие, 0 - уклон в магию

    # Установка порогового нижнего и верхнего значений для навыков и спелов
    skill_left = 3 + (class_factor - 1) * 5 + might_or_magic
    if skill_left > 20:
        skill_left = 20
    skill_right = 8 + (class_factor - 1) * 5 + might_or_magic
    if skill_right > 20:
        skill_right = 20
    spell_left = 3 + (class_factor - 1) * 5 + (1 - 1 * might_or_magic)
    if spell_left > 20:
        spell_left = 20
    spell_right = 8 + (class_factor - 1) * 5 + (1 - 1 * might_or_magic)
    if spell_right > 20:
        spell_right = 20

    # Проверка на повторы в выбранных скилах и генерация значений к имеющемуся оружию
    points = this_lvl
    virtual_skills_list = [None,  # Список скиллов, в котором могут быть повторы
                           widget[i].comboBox_skill_1.currentText(),
                           widget[i].comboBox_skill_2.currentText(),
                           widget[i].comboBox_skill_3.currentText(),
                           widget[i].comboBox_skill_4.currentText()]

    for n in range(1, len(virtual_skills_list)):  # сгенерируем скилы к выбранному оружию
        if virtual_skills_list[n] == '' and widget[i].comboBox_weapon_1.currentText() not in ['', 'Занято', 'Щит'] \
                and weapons_dict[widget[i].comboBox_weapon_1.currentText()]['skill'] not in virtual_skills_list:
            virtual_skills_list[n] = weapons_dict[widget[i].comboBox_weapon_1.currentText()]['skill']
        elif virtual_skills_list[n] == '' and widget[i].comboBox_weapon_2.currentText() not in ['', 'Занято',
                                                                                                'Щит'] \
                and weapons_dict[widget[i].comboBox_weapon_2.currentText()]['skill'] not in virtual_skills_list:
            virtual_skills_list[n] = weapons_dict[widget[i].comboBox_weapon_2.currentText()]['skill']

    virtual_skills_points_list = [None,  # Список значений скиллов
                                  widget[i].lineEdit_skill_1.text(),
                                  widget[i].lineEdit_skill_2.text(),
                                  widget[i].lineEdit_skill_3.text(),
                                  widget[i].lineEdit_skill_4.text()]

    for n in range(len(virtual_skills_list) - 1, 0, -1):  # поверка в обратном порядке
        if virtual_skills_list[n] != '':  # если в скилл n что-то вписано, то два варианта:
            # это повтор, удалить значение в '' (если не 0)
            if virtual_skills_list.count(virtual_skills_list[n]) > 1:
                virtual_skills_list[n] = ''
                if virtual_skills_points_list[n] != '':
                    virtual_skills_points_list[n] = ''
            else:  # это не повтор, проверить значение, 0 - не менять, '' - генерировать, 22 - не менять
                if virtual_skills_points_list[n] == '':  # либо ничего
                    virtual_skills_points_list[n] = randint(skill_left, skill_right)
                points -= int(virtual_skills_points_list[n])  # вычитаем points
        # проверка заполненных значений и генерация к ним скилов
        if virtual_skills_points_list[n] != '0' and virtual_skills_points_list[n] != '' \
                and virtual_skills_list[n] == '':
            if NPC_types_dict[this_type]['has_skills']:  # если у НПС вообще есть скилы, то:
                skill_random = randint(1, 100)
                if skill_random <= NPC_types_dict[this_type]['melee_percent']:
                    virtual_skills_list[n] = choice(list(set(skills_list_melee) - set(virtual_skills_list)))
                elif skill_random <= NPC_types_dict[this_type]['ranged_percent'] + \
                        NPC_types_dict[this_type]['melee_percent']:
                    virtual_skills_list[n] = choice(list(set(skills_list_ranged) - set(virtual_skills_list)))
                else:
                    virtual_skills_list[n] = choice(
                        list(set(skills_list_noncombat) - set(virtual_skills_list)))
            else:  # если нет, то нам не важно что рандомить
                virtual_skills_list[n] = choice(list(set(skills_list) - set(virtual_skills_list)))

    # Проверка на повторы в выбранных спеллах и генерация значений к имеющимся
    virtual_spells_list = [None,  # Список индексов спеллов, в котором могут быть повторы
                           widget[i].comboBox_spell_1.currentText(),
                           widget[i].comboBox_spell_2.currentText(),
                           widget[i].comboBox_spell_3.currentText(),
                           widget[i].comboBox_spell_4.currentText(),
                           widget[i].comboBox_spell_5.currentText()]
    virtual_spells_points_list = [None,  # Список значений спелов
                                  widget[i].lineEdit_spell_1.text(),
                                  widget[i].lineEdit_spell_2.text(),
                                  widget[i].lineEdit_spell_3.text(),
                                  widget[i].lineEdit_spell_4.text(),
                                  widget[i].lineEdit_spell_5.text()]

    for n in range(len(virtual_spells_list) - 1, 0, -1):  # поверка в обратном порядке
        if virtual_spells_list[n] != '':  # если в спелл n что-то вписано (индекс не 0) то два варианта:
            if virtual_spells_list.count(virtual_spells_list[n]) > 1:  # это повтор, удалить значение в '' (если не 0)
                virtual_spells_list[n] = ''
                if virtual_spells_points_list[n] != '0':
                    virtual_spells_points_list[n] = ''
            else:  # это не повтор, проверить значение, 0 - не менять, '' - генерировать, 22 - не емнять
                if virtual_spells_points_list[n] == '':  # либо ничего
                    virtual_spells_points_list[n] = randint(spell_left, spell_right)
                points -= int(virtual_spells_points_list[n])  # вычитаем points
        # проверка заполненных значений и генерация к ним спелов
        if virtual_spells_points_list[n] != '0' and virtual_spells_points_list[n] != '' and virtual_spells_list[
            n] == '':
            virtual_spells_list[n] = choice(list(set(spells_list) - set(virtual_spells_list)))

    # Генерация случайных скиллов и спеллов циклом
    if (NPC_types_dict[this_type]['has_skills'] or NPC_types_dict[this_type]['has_spells']) \
            and ('' in virtual_spells_points_list or '' in virtual_skills_points_list) \
            and points > 0:
        while points > 0:
            # (если НПС может иметь скилы И места есть)
            # И (НПС не может иметь спеллы ИЛИ удачный проброс
            # ИЛИ места в спелах уже нет)
            if (NPC_types_dict[this_type]['has_skills'] == 1 and '' in virtual_skills_points_list) and \
                    (NPC_types_dict[this_type]['has_spells'] == 0 or randint(1, 100) <= NPC_types_dict[this_type][
                        'skill_or_spell']
                     or '' not in virtual_spells_points_list):
                free_skill_index = virtual_skills_points_list.index('')
                skill_random = randint(1, 100)
                if skill_random <= NPC_types_dict[this_type]['melee_percent']:
                    virtual_skills_list[free_skill_index] = choice(
                        list(set(skills_list_melee) - set(virtual_skills_list)))
                elif skill_random <= NPC_types_dict[this_type]['ranged_percent'] + \
                        NPC_types_dict[this_type]['melee_percent']:
                    virtual_skills_list[free_skill_index] = choice(
                        list(set(skills_list_ranged) - set(virtual_skills_list)))
                else:
                    virtual_skills_list[free_skill_index] = choice(
                        list(set(skills_list_noncombat) - set(virtual_skills_list)))
                randint_skills_points = randint(skill_left, skill_right)
                virtual_skills_points_list[free_skill_index] = randint_skills_points
                points -= randint_skills_points
            # если НПС может иметь спеллы И свободные места ещё есть
            elif NPC_types_dict[this_type]['has_spells'] == 1 and '' in virtual_spells_points_list:
                free_spell_index = virtual_spells_points_list.index('')
                virtual_spells_list[free_spell_index] = choice(list(set(spells_list) - set(virtual_spells_list)))
                randint_spells_points = randint(spell_left, spell_right)
                virtual_spells_points_list[free_spell_index] = randint_spells_points
                points -= randint_spells_points
            else:
                break

    widget[i].comboBox_skill_1.setCurrentText(virtual_skills_list[1])
    widget[i].comboBox_skill_2.setCurrentText(virtual_skills_list[2])
    widget[i].comboBox_skill_3.setCurrentText(virtual_skills_list[3])
    widget[i].comboBox_skill_4.setCurrentText(virtual_skills_list[4])
    widget[i].lineEdit_skill_1.setText(str(virtual_skills_points_list[1]))
    widget[i].lineEdit_skill_2.setText(str(virtual_skills_points_list[2]))
    widget[i].lineEdit_skill_3.setText(str(virtual_skills_points_list[3]))
    widget[i].lineEdit_skill_4.setText(str(virtual_skills_points_list[4]))

    widget[i].comboBox_spell_1.setCurrentText(virtual_spells_list[1])
    widget[i].comboBox_spell_2.setCurrentText(virtual_spells_list[2])
    widget[i].comboBox_spell_3.setCurrentText(virtual_spells_list[3])
    widget[i].comboBox_spell_4.setCurrentText(virtual_spells_list[4])
    widget[i].comboBox_spell_5.setCurrentText(virtual_spells_list[5])
    widget[i].lineEdit_spell_1.setText(str(virtual_spells_points_list[1]))
    widget[i].lineEdit_spell_2.setText(str(virtual_spells_points_list[2]))
    widget[i].lineEdit_spell_3.setText(str(virtual_spells_points_list[3]))
    widget[i].lineEdit_spell_4.setText(str(virtual_spells_points_list[4]))
    widget[i].lineEdit_spell_5.setText(str(virtual_spells_points_list[5]))

    # Проверка на повторы в выбранных талантах
    virtual_talents_list = [None,  # Выбранный вписок индексов талантов, в котором могут быть ошибки
                            widget[i].comboBox_talent_1.currentText(),
                            widget[i].comboBox_talent_2.currentText()]
    for n in range(len(virtual_talents_list) - 1, 1, -1):  # поверка в обратном порядке
        if virtual_talents_list[n] != '' and virtual_talents_list.count(virtual_talents_list[n]) > 1:
            virtual_talents_list[n] = ''

    # Формирование талантов
    for n in range(1, len(virtual_talents_list)):  # поверка от 1-го
        if virtual_talents_list[n] == '':  # если индекс устанволен на 0 (есть место свободное)
            # если среди навыков выбраны единоборства и ни одно из усилилений единоборства не присутсвует:
            if 'Единоборства' in virtual_skills_list and 'Кулаки - молоты' not in virtual_talents_list and 'Когти - кинжалы' not in virtual_talents_list:
                virtual_talents_list[n] = choice(['Когти - кинжалы', 'Кулаки - молоты'])
            if virtual_talents_list[n] == '' and randint(1, 9) <= class_factor ** 2:
                virtual_talents_list[n] = choice(list(set(talents_list) - set(virtual_talents_list)))

    widget[i].comboBox_talent_1.setCurrentText(virtual_talents_list[1])
    widget[i].comboBox_talent_2.setCurrentText(virtual_talents_list[2])

    # сформируем характеристики
    if len(widget[i].lineEdit_physique.text()) == 0:
        this_physique = (NPC_types_dict[this_type]['base_physique'] + might_or_magic * 2) * class_factor
        if this_physique > 20:
            this_physique = 20
        widget[i].lineEdit_physique.setText(str(this_physique))

    if len(widget[i].lineEdit_intelligence.text()) == 0:
        this_intelligence = (NPC_types_dict[this_type]['base_intelligence'] + (1 - might_or_magic) * 2) * class_factor
        if this_intelligence > 20:
            this_intelligence = 20
        widget[i].lineEdit_intelligence.setText(str(this_intelligence))

    if len(widget[i].lineEdit_mastery.text()) == 0:
        max_skill_points = 0
        for n in virtual_skills_points_list:
            if n and n != '' and int(n) > max_skill_points:
                max_skill_points = int(n)  # мастерство определяется половиной от максимального навыка
        if NPC_types_dict[this_type]['base_mastery'] + might_or_magic + class_factor <= int(max_skill_points / 2):
            this_mastery = int(max_skill_points / 2)
        else:
            this_mastery = NPC_types_dict[this_type]['base_mastery'] + might_or_magic + class_factor
        if this_mastery > 20:
            this_mastery = 20
        widget[i].lineEdit_mastery.setText(str(this_mastery))

    # если оружие 1 не выбрано !!! Происходит бабуйня при преднастроке второй руки!!! FIX IT!!!
    weapon_mod = randint(1, 100)
    if weapon_mod <= NPC_types_dict[this_type]['weapon_percent']:  # если оружие НПС может брать
        if widget[i].comboBox_weapon_1.currentIndex() == 0:
            # поиск максимального боевого навыка:
            max_battle_skill_points = 0
            max_battle_skill = 'Единоборства'  # отвечает за метательное, бой без оружия, бой в каcтетах
            for n in range(1, len(virtual_skills_list)):
                if virtual_skills_list[n] in (skills_dict['Melee'] + skills_dict['Ranged']) and int(
                        virtual_skills_points_list[n]) > max_battle_skill_points:
                    max_battle_skill_points = int(virtual_skills_points_list[n])
                    max_battle_skill = virtual_skills_list[n]
            # поиск оружия, подходящего под скилл
            random_weapons_list = []
            for weapon in weapons_list:
                if weapons_dict[weapon]['skill'] == max_battle_skill:
                    random_weapons_list.append(weapon)
            if len(random_weapons_list) == 0:
                random_weapons_list.append('Без оружия')
            this_weapon_1 = choice(random_weapons_list)
            widget[i].comboBox_weapon_1.setCurrentText(this_weapon_1)
            # подберём оружие для второй руки:
            if not weapons_dict[this_weapon_1]['two-handed'] and widget[i].comboBox_weapon_2.currentIndex() == 0:
                shield_mod = 1 if randint(1, 100) <= NPC_types_dict[this_type]['shield_percent'] \
                                  and weapons_dict[this_weapon_1]['skill'] not in ['Единоборства', '1хПистолеты'] \
                                  and this_weapon_1 != 'Кинжал' else 0
                this_weapon_2 = choice(random_weapons_list + ['Щит'] * shield_mod)
                widget[i].comboBox_weapon_2.setCurrentText(this_weapon_2)
            else:
                this_weapon_2 = 'Занято'
                widget[i].comboBox_weapon_2.setCurrentText(this_weapon_2)
    else:
        this_weapon_1 = 'Без оружия'
        widget[i].comboBox_weapon_1.setCurrentText(this_weapon_1)
        this_weapon_2 = 'Без оружия'
        widget[i].comboBox_weapon_2.setCurrentText(this_weapon_2)

    this_weapon_1 = widget[i].comboBox_weapon_1.currentText()
    this_weapon_2 = widget[i].comboBox_weapon_2.currentText()
    # выставим оружию получившиеся настройки
    if this_weapon_1 != 'Занято' and this_weapon_1 != '':
        widget[i].lineEdit_weapon1.setText(weapons_dict[this_weapon_1]['name'])
        widget[i].lineEdit_weapon1_magic_damage.setText(str(weapons_dict[this_weapon_1]['magic_damage']))
        widget[i].lineEdit_weapon1_armor_damage.setText(str(weapons_dict[this_weapon_1]['armor_damage']))
        widget[i].lineEdit_weapon1_penetration_damage.setText(str(weapons_dict[this_weapon_1]['penetration_damage']))
        widget[i].lineEdit_weapon1_health_damage.setText(str(weapons_dict[this_weapon_1]['health_damage']))
    if this_weapon_2 != 'Занято' and this_weapon_2 != '':
        widget[i].lineEdit_weapon2.setText(weapons_dict[this_weapon_2]['name'])
        widget[i].lineEdit_weapon2_magic_damage.setText(str(weapons_dict[this_weapon_2]['magic_damage']))
        widget[i].lineEdit_weapon2_armor_damage.setText(str(weapons_dict[this_weapon_2]['armor_damage']))
        widget[i].lineEdit_weapon2_penetration_damage.setText(
            str(weapons_dict[this_weapon_2]['penetration_damage']))
        widget[i].lineEdit_weapon2_health_damage.setText(str(weapons_dict[this_weapon_2]['health_damage']))

    # если класс брони (как шкура дракона или рыцарский доспех) не выбрано
    if widget[i].comboBox_plate.currentIndex() == 0:
        if randint(1, 100) <= NPC_types_dict[this_type]['armor_percent']:
            this_plate = choice(
                plate_list[floor((class_factor - 1) * len(plate_list) / 3):ceil(class_factor * len(plate_list) / 3)])
        else:
            this_plate = 'Без лат'
        widget[i].comboBox_plate.setCurrentText(this_plate)
    else:
        this_plate = widget[i].comboBox_plate.currentText()

    # обозначим броню
    if widget[i].lineEdit_armor.text() == '':
        widget[i].lineEdit_armor.setText(str(plate_dict[this_plate]))

    # обозначим здоровье
    if widget[i].lineEdit_health.text() == '':
        widget[i].lineEdit_health.setText(str(widget[i].lineEdit_physique.text()))


def pushbutton_reset(i: int):  # i - widget number
    list_for_reset_lines = [
        widget[i].lineEdit_physique,

        widget[i].lineEdit_mastery,
        widget[i].lineEdit_skill_1,
        widget[i].lineEdit_skill_2,
        widget[i].lineEdit_skill_3,
        widget[i].lineEdit_skill_4,

        widget[i].lineEdit_intelligence,
        widget[i].lineEdit_spell_1,
        widget[i].lineEdit_spell_2,
        widget[i].lineEdit_spell_3,
        widget[i].lineEdit_spell_4,
        widget[i].lineEdit_spell_5,

        widget[i].lineEdit_weapon1,
        widget[i].lineEdit_weapon1_magic_damage,
        widget[i].lineEdit_weapon1_armor_damage,
        widget[i].lineEdit_weapon1_penetration_damage,
        widget[i].lineEdit_weapon1_health_damage,

        widget[i].lineEdit_weapon2,
        widget[i].lineEdit_weapon2_magic_damage,
        widget[i].lineEdit_weapon2_armor_damage,
        widget[i].lineEdit_weapon2_penetration_damage,
        widget[i].lineEdit_weapon2_health_damage,

        widget[i].lineEdit_magic_barrier,
        widget[i].lineEdit_armor,
        widget[i].lineEdit_health,

        widget[i].lineEdit_periodic_damage_magic,
        widget[i].lineEdit_periodic_damage_armor,
        widget[i].lineEdit_periodic_damage_penetration_damage,
        widget[i].lineEdit_periodic_damage_health,

        widget[i].lineEdit_periodic_heal_magic,
        widget[i].lineEdit_periodic_heal_armor,
        widget[i].lineEdit_periodic_heal_health,

        widget[i].lineEdit_incoming_damage_magic,
        widget[i].lineEdit_incoming_damage_armor,
        widget[i].lineEdit_incoming_damage_penetration_damage,
        widget[i].lineEdit_incoming_damage_health,

        widget[i].lineEdit_incoming_heal_magic,
        widget[i].lineEdit_incoming_heal_armor,
        widget[i].lineEdit_incoming_heal_health,
    ]

    for line in list_for_reset_lines:
        line.clear()

    list_for_reset_combo_boxes = [
        widget[i].comboBox_weapon_1,
        widget[i].comboBox_weapon_2,
        widget[i].comboBox_plate,
        widget[i].comboBox_talent_1,
        widget[i].comboBox_talent_2,
        widget[i].comboBox_skill_1,
        widget[i].comboBox_skill_2,
        widget[i].comboBox_skill_3,
        widget[i].comboBox_skill_4,
        widget[i].comboBox_spell_1,
        widget[i].comboBox_spell_2,
        widget[i].comboBox_spell_3,
        widget[i].comboBox_spell_4,
        widget[i].comboBox_spell_5,
    ]

    for combo_box in list_for_reset_combo_boxes:
        combo_box.setCurrentIndex(0)

    list_for_reset_radio_buttons = [
        widget[i].radioButton_might,
        widget[i].radioButton_magic,
        widget[i].radioButton_crit,
        widget[i].radioButton_defense,
    ]

    for radio_button in list_for_reset_radio_buttons:
        radio_button.setAutoExclusive(False)
        radio_button.setChecked(False)


def pushbutton_load(i: int):  # i - widget number
    pass


def pushbutton_save(i: int):  # i - widget number
    pass


def pushbutton_incoming_heal_enter(i: int):  # i - widget number
    lines_inspector(i)
    name = widget[i].lineEdit_name.text()
    if name != '':
        health = int(widget[i].lineEdit_health.text()) \
            if widget[i].lineEdit_health.text() != '' else 0

        if health > 0:  # если NPC вообще жив

            armor = int(widget[i].lineEdit_armor.text()) \
                if widget[i].lineEdit_armor.text() != '' else 0
            magic_barrier = int(widget[i].lineEdit_magic_barrier.text()) \
                if widget[i].lineEdit_magic_barrier.text() != '' else 0

            incoming_heal_health = int(widget[i].lineEdit_incoming_heal_health.text()) \
                if widget[i].lineEdit_incoming_heal_health.text() != '' else 0
            incoming_heal_armor = int(widget[i].lineEdit_incoming_heal_armor.text()) \
                if widget[i].lineEdit_incoming_heal_armor.text() != '' else 0
            incoming_heal_magic = int(widget[i].lineEdit_incoming_heal_magic.text()) \
                if widget[i].lineEdit_incoming_heal_magic.text() != '' else 0

            new_health = health + incoming_heal_health
            new_armor = armor + incoming_heal_armor
            new_magic_barrier = magic_barrier + incoming_heal_magic

            widget[i].lineEdit_health.setText(str(new_health))
            widget[i].lineEdit_armor.setText(str(new_armor))
            widget[i].lineEdit_magic_barrier.setText(str(new_magic_barrier))
        else:
            main_menu.textEdit_battlelog.append(f'{name} мёртв')


def pushbutton_incoming_damage_enter(i: int):  # i - widget number
    lines_inspector(i)
    name = widget[i].lineEdit_name.text()
    if name != '':
        health = int(widget[i].lineEdit_health.text()) \
            if widget[i].lineEdit_health.text() != '' else 0

        if health > 0:  # если NPC вообще жив

            armor = int(widget[i].lineEdit_armor.text()) \
                if widget[i].lineEdit_armor.text() != '' else 0
            magic_barrier = int(widget[i].lineEdit_magic_barrier.text()) \
                if widget[i].lineEdit_magic_barrier.text() != '' else 0

            incoming_damage_health = int(widget[i].lineEdit_incoming_damage_health.text()) \
                if widget[i].lineEdit_incoming_damage_health.text() != '' else 0
            incoming_damage_penetration_damage = int(widget[i].lineEdit_incoming_damage_penetration_damage.text()) \
                if widget[i].lineEdit_incoming_damage_penetration_damage.text() != '' else 0
            incoming_damage_armor = int(widget[i].lineEdit_incoming_damage_armor.text()) \
                if widget[i].lineEdit_incoming_damage_armor.text() != '' else 0
            incoming_damage_magic = int(widget[i].lineEdit_incoming_damage_magic.text()) \
                if widget[i].lineEdit_incoming_damage_magic.text() != '' else 0


            if armor > 0:
                incoming_damage_health = 0

            if magic_barrier == 0 and incoming_damage_magic > 0:
                incoming_damage_penetration_damage += incoming_damage_magic

            new_health = health - incoming_damage_health - incoming_damage_penetration_damage
            if new_health <= 0:
                new_health = 0
                main_menu.textEdit_battlelog.append(f'{name} умирает')
            new_armor = armor - incoming_damage_armor
            if new_armor < 0:
                new_armor = 0
            new_magic_barrier = magic_barrier - incoming_damage_magic
            if new_magic_barrier < 0:
                new_magic_barrier = 0

            widget[i].lineEdit_health.setText(str(new_health))
            widget[i].lineEdit_armor.setText(str(new_armor))
            widget[i].lineEdit_magic_barrier.setText(str(new_magic_barrier))
        else:
            main_menu.textEdit_battlelog.append(f'{name} мёртв')


def pushbutton_attack(i: int):  # i - widget number
    lines_inspector(i)
    virtual_skills_list = [None,  # Список индексов скиллов, в котором могут быть повторы
                           widget[i].comboBox_skill_1.currentText(),
                           widget[i].comboBox_skill_2.currentText(),
                           widget[i].comboBox_skill_3.currentText(),
                           widget[i].comboBox_skill_4.currentText()]

    virtual_skills_points_list = [None,  # Список индексов скиллов, в котором могут быть повторы
                                  widget[i].lineEdit_skill_1.text(),
                                  widget[i].lineEdit_skill_2.text(),
                                  widget[i].lineEdit_skill_3.text(),
                                  widget[i].lineEdit_skill_4.text()]
    virtual_weapon_name_list = [None,  # Список индексов скиллов, в котором могут быть повторы
                                widget[i].comboBox_weapon_1.currentText(),
                                widget[i].comboBox_weapon_2.currentText()]
    attacks = 0
    for hand in range(1, 3):
        if virtual_weapon_name_list[hand] != 'Занято' and virtual_weapon_name_list[hand] != '':
            if attacks == 0:
                main_menu.textEdit_battlelog.append(
                    f"{widget[i].lineEdit_name.text()} атакует!\n~~~~~~~~~~~~~~~~~~~~~~~")
            for strike in range(weapons_dict[virtual_weapon_name_list[hand]]['speed']):
                attacks += 1
                if weapons_dict[virtual_weapon_name_list[hand]]['skill'] in virtual_skills_list:
                    skill = weapons_dict[virtual_weapon_name_list[1]]['skill']
                    skill_index = virtual_skills_list.index(skill)
                    skill_value = int(virtual_skills_points_list[skill_index])
                    D20_roll(i, skill, skill_value)
                else:
                    skill = 'Мастерство'
                    skill_value = int(widget[i].lineEdit_mastery.text())
                    D20_roll(i, skill, skill_value)
    if attacks > 0:
        main_menu.textEdit_battlelog.append("~~~~~~~~~~~~~~~~~~~~~~~")


def D20_roll(i: int, skill: str, skill_value: str):  # i - widget number
    if skill != '' and skill_value != '' and widget[0].lineEdit_name.text() != '':
        skill_value = int(skill_value)
        D20_roll = randint(1, 20)
        if D20_roll == 1:
            result = 'Критическая неудача'
        elif D20_roll == 20:
            result = 'Максимальный результат! Крит!'
        elif D20_roll <= (20 - skill_value * 2):  # красная зона
            result = 'Неудача!'
        elif D20_roll > (20 - (skill_value - 10) * 2):  # зелёная зона
            result = 'Крит!'
        else:  # серая зона
            result = 'Номрально'

        main_menu.textEdit_battlelog.append(f"{widget[i].lineEdit_name.text()} бросает на\n'{skill}' {skill_value}"
                                            f"\nРезультат броска - {D20_roll}\n{result}\n")


def main():
    global widget, WidgetNPС, widgets_counter, main_menu, person_ru, text_ru, round_number
    person_ru = Person('ru')  # объект Person для генерации личных данных NPC
    text_ru = Text('ru')  # объект для генерации некотрых слов
    app = QtWidgets.QApplication(sys.argv)  # Create application - инициализация приложения
    MainWindow = QtWidgets.QMainWindow()  # Create form main menu создание формы окна главного меню
    widgets_counter = 0
    round_number = 0
    widget = []
    WidgetNPС = []
    for i in range(0, 10):  # создаём виджеты NPC от 0 до 9
        widget.append(Ui_NPC_Widget())

        WidgetNPС.append(QtWidgets.QWidget())

        widget[i].setupUi(WidgetNPС[i])

        widget[i].comboBox_type.addItems(NPC_types_list)
        widget[i].comboBox_talent_1.addItems(talents_dict)
        widget[i].comboBox_talent_2.addItems(talents_dict)
        widget[i].comboBox_skill_1.addItems(skills_list)
        widget[i].comboBox_skill_2.addItems(skills_list)
        widget[i].comboBox_skill_3.addItems(skills_list)
        widget[i].comboBox_skill_4.addItems(skills_list)
        widget[i].comboBox_spell_1.addItems(spells_dict)
        widget[i].comboBox_spell_2.addItems(spells_dict)
        widget[i].comboBox_spell_3.addItems(spells_dict)
        widget[i].comboBox_spell_4.addItems(spells_dict)
        widget[i].comboBox_spell_5.addItems(spells_dict)
        widget[i].comboBox_weapon_1.addItems(weapons_list)
        widget[i].comboBox_weapon_2.addItems(weapons_list)
        widget[i].comboBox_plate.addItems(plate_list)
    init_widget_buttons()
    main_menu = Ui_MainWindow()
    main_menu.setupUi(MainWindow)
    MainWindow.show()

    main_menu.pushButton_add_NPC.clicked.connect(pushbutton_add_npc)
    main_menu.pushButton_remove_NPC.clicked.connect(pushbutton_remove_npc)

    main_menu.pushButton_store_talents.clicked.connect(pushbutton_store_talents)
    main_menu.pushButton_store_skills.clicked.connect(pushbutton_store_skills)
    main_menu.pushButton_store_spells.clicked.connect(pushbutton_store_spells)
    main_menu.pushButton_store_weapons.clicked.connect(pushbutton_store_weapons)
    main_menu.pushButton_store_plates.clicked.connect(pushbutton_store_plates)

    main_menu.pushButton_period.clicked.connect(pushbutton_period)

    main_menu.pushButton_loot.clicked.connect(pushbutton_loot)

    main_menu.textEdit_battlelog.append('Программа "Muskrat NPC Generator" иницирована и готова к использованию\n'
                                 'Версия - Pre-Alpha 0.2\n'
                                 'Связь с автором - Григорий Скворцов GregoryValeryS@gmail.com\n'
                                 'GNU General Public License v3.0\n')

    sys.exit(app.exec_())  # Run main loop


if __name__ == '__main__':
    main()
