import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main_menu import Ui_MainWindow
from ui_NPC_widget import Ui_NPC_Widget
from mimesis import Person
from mimesis.enums import Gender
from mimesis import Text
from random import randint, choice
from store import NPC_types_dict, weapons_types, spells_dict, talents_dict, skills_dict, skills_list, skills_types_list

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
        pushbutton_d20_physique(0)


    def pushbutton_d20_physique_1():
        pushbutton_d20_physique(1)


    def pushbutton_d20_physique_2():
        pushbutton_d20_physique(2)


    def pushbutton_d20_physique_3():
        pushbutton_d20_physique(3)


    def pushbutton_d20_physique_4():
        pushbutton_d20_physique(4)


    def pushbutton_d20_physique_5():
        pushbutton_d20_physique(5)


    def pushbutton_d20_physique_6():
        pushbutton_d20_physique(6)


    def pushbutton_d20_physique_7():
        pushbutton_d20_physique(7)


    def pushbutton_d20_physique_8():
        pushbutton_d20_physique(8)


    def pushbutton_d20_physique_9():
        pushbutton_d20_physique(9)


    def pushbutton_d20_mastery_0():
        pushbutton_d20_mastery(0)


    def pushbutton_d20_mastery_1():
        pushbutton_d20_mastery(1)


    def pushbutton_d20_mastery_2():
        pushbutton_d20_mastery(2)


    def pushbutton_d20_mastery_3():
        pushbutton_d20_mastery(3)


    def pushbutton_d20_mastery_4():
        pushbutton_d20_mastery(4)


    def pushbutton_d20_mastery_5():
        pushbutton_d20_mastery(5)


    def pushbutton_d20_mastery_6():
        pushbutton_d20_mastery(6)


    def pushbutton_d20_mastery_7():
        pushbutton_d20_mastery(7)


    def pushbutton_d20_mastery_8():
        pushbutton_d20_mastery(8)


    def pushbutton_d20_mastery_9():
        pushbutton_d20_mastery(9)


    def pushbutton_d20_skill_1_0():
        pushbutton_d20_skill_1(0)


    def pushbutton_d20_skill_1_1():
        pushbutton_d20_skill_1(1)


    def pushbutton_d20_skill_1_2():
        pushbutton_d20_skill_1(2)


    def pushbutton_d20_skill_1_3():
        pushbutton_d20_skill_1(3)


    def pushbutton_d20_skill_1_4():
        pushbutton_d20_skill_1(4)


    def pushbutton_d20_skill_1_5():
        pushbutton_d20_skill_1(5)


    def pushbutton_d20_skill_1_6():
        pushbutton_d20_skill_1(6)


    def pushbutton_d20_skill_1_7():
        pushbutton_d20_skill_1(7)


    def pushbutton_d20_skill_1_8():
        pushbutton_d20_skill_1(8)


    def pushbutton_d20_skill_1_9():
        pushbutton_d20_skill_1(9)


    def pushbutton_d20_skill_2_0():
        pushbutton_d20_skill_2(0)


    def pushbutton_d20_skill_2_1():
        pushbutton_d20_skill_2(1)


    def pushbutton_d20_skill_2_2():
        pushbutton_d20_skill_2(2)


    def pushbutton_d20_skill_2_3():
        pushbutton_d20_skill_2(3)


    def pushbutton_d20_skill_2_4():
        pushbutton_d20_skill_2(4)


    def pushbutton_d20_skill_2_5():
        pushbutton_d20_skill_2(5)


    def pushbutton_d20_skill_2_6():
        pushbutton_d20_skill_2(6)


    def pushbutton_d20_skill_2_7():
        pushbutton_d20_skill_2(7)


    def pushbutton_d20_skill_2_8():
        pushbutton_d20_skill_2(8)


    def pushbutton_d20_skill_2_9():
        pushbutton_d20_skill_2(9)


    def pushbutton_d20_skill_3_0():
        pushbutton_d20_skill_3(0)


    def pushbutton_d20_skill_3_1():
        pushbutton_d20_skill_3(1)


    def pushbutton_d20_skill_3_2():
        pushbutton_d20_skill_3(2)


    def pushbutton_d20_skill_3_3():
        pushbutton_d20_skill_3(3)


    def pushbutton_d20_skill_3_4():
        pushbutton_d20_skill_3(4)


    def pushbutton_d20_skill_3_5():
        pushbutton_d20_skill_3(5)


    def pushbutton_d20_skill_3_6():
        pushbutton_d20_skill_3(6)


    def pushbutton_d20_skill_3_7():
        pushbutton_d20_skill_3(7)


    def pushbutton_d20_skill_3_8():
        pushbutton_d20_skill_3(8)


    def pushbutton_d20_skill_3_9():
        pushbutton_d20_skill_3(9)


    def pushbutton_d20_skill_4_0():
        pushbutton_d20_skill_4(0)


    def pushbutton_d20_skill_4_1():
        pushbutton_d20_skill_4(1)


    def pushbutton_d20_skill_4_2():
        pushbutton_d20_skill_4(2)


    def pushbutton_d20_skill_4_3():
        pushbutton_d20_skill_4(3)


    def pushbutton_d20_skill_4_4():
        pushbutton_d20_skill_4(4)


    def pushbutton_d20_skill_4_5():
        pushbutton_d20_skill_4(5)


    def pushbutton_d20_skill_4_6():
        pushbutton_d20_skill_4(6)


    def pushbutton_d20_skill_4_7():
        pushbutton_d20_skill_4(7)


    def pushbutton_d20_skill_4_8():
        pushbutton_d20_skill_4(8)


    def pushbutton_d20_skill_4_9():
        pushbutton_d20_skill_4(9)


    def pushbutton_d20_intelligence_0():
        pushbutton_d20_intelligence(0)


    def pushbutton_d20_intelligence_1():
        pushbutton_d20_intelligence(1)


    def pushbutton_d20_intelligence_2():
        pushbutton_d20_intelligence(2)


    def pushbutton_d20_intelligence_3():
        pushbutton_d20_intelligence(3)


    def pushbutton_d20_intelligence_4():
        pushbutton_d20_intelligence(4)


    def pushbutton_d20_intelligence_5():
        pushbutton_d20_intelligence(5)


    def pushbutton_d20_intelligence_6():
        pushbutton_d20_intelligence(6)


    def pushbutton_d20_intelligence_7():
        pushbutton_d20_intelligence(7)


    def pushbutton_d20_intelligence_8():
        pushbutton_d20_intelligence(8)


    def pushbutton_d20_intelligence_9():
        pushbutton_d20_intelligence(9)


    def pushbutton_d20_spell_1_0():
        pushbutton_d20_spell_1(0)


    def pushbutton_d20_spell_1_1():
        pushbutton_d20_spell_1(1)


    def pushbutton_d20_spell_1_2():
        pushbutton_d20_spell_1(2)


    def pushbutton_d20_spell_1_3():
        pushbutton_d20_spell_1(3)


    def pushbutton_d20_spell_1_4():
        pushbutton_d20_spell_1(4)


    def pushbutton_d20_spell_1_5():
        pushbutton_d20_spell_1(5)


    def pushbutton_d20_spell_1_6():
        pushbutton_d20_spell_1(6)


    def pushbutton_d20_spell_1_7():
        pushbutton_d20_spell_1(7)


    def pushbutton_d20_spell_1_8():
        pushbutton_d20_spell_1(8)


    def pushbutton_d20_spell_1_9():
        pushbutton_d20_spell_1(9)


    def pushbutton_d20_spell_2_0():
        pushbutton_d20_spell_2(0)


    def pushbutton_d20_spell_2_1():
        pushbutton_d20_spell_2(1)


    def pushbutton_d20_spell_2_2():
        pushbutton_d20_spell_2(2)


    def pushbutton_d20_spell_2_3():
        pushbutton_d20_spell_2(3)


    def pushbutton_d20_spell_2_4():
        pushbutton_d20_spell_2(4)


    def pushbutton_d20_spell_2_5():
        pushbutton_d20_spell_2(5)


    def pushbutton_d20_spell_2_6():
        pushbutton_d20_spell_2(6)


    def pushbutton_d20_spell_2_7():
        pushbutton_d20_spell_2(7)


    def pushbutton_d20_spell_2_8():
        pushbutton_d20_spell_2(8)


    def pushbutton_d20_spell_2_9():
        pushbutton_d20_spell_2(9)


    def pushbutton_d20_spell_3_0():
        pushbutton_d20_spell_3(0)


    def pushbutton_d20_spell_3_1():
        pushbutton_d20_spell_3(1)


    def pushbutton_d20_spell_3_2():
        pushbutton_d20_spell_3(2)


    def pushbutton_d20_spell_3_3():
        pushbutton_d20_spell_3(3)


    def pushbutton_d20_spell_3_4():
        pushbutton_d20_spell_3(4)


    def pushbutton_d20_spell_3_5():
        pushbutton_d20_spell_3(5)


    def pushbutton_d20_spell_3_6():
        pushbutton_d20_spell_3(6)


    def pushbutton_d20_spell_3_7():
        pushbutton_d20_spell_3(7)


    def pushbutton_d20_spell_3_8():
        pushbutton_d20_spell_3(8)


    def pushbutton_d20_spell_3_9():
        pushbutton_d20_spell_3(9)


    def pushbutton_d20_spell_4_0():
        pushbutton_d20_spell_4(0)


    def pushbutton_d20_spell_4_1():
        pushbutton_d20_spell_4(1)


    def pushbutton_d20_spell_4_2():
        pushbutton_d20_spell_4(2)


    def pushbutton_d20_spell_4_3():
        pushbutton_d20_spell_4(3)


    def pushbutton_d20_spell_4_4():
        pushbutton_d20_spell_4(4)


    def pushbutton_d20_spell_4_5():
        pushbutton_d20_spell_4(5)


    def pushbutton_d20_spell_4_6():
        pushbutton_d20_spell_4(6)


    def pushbutton_d20_spell_4_7():
        pushbutton_d20_spell_4(7)


    def pushbutton_d20_spell_4_8():
        pushbutton_d20_spell_4(8)


    def pushbutton_d20_spell_4_9():
        pushbutton_d20_spell_4(9)


    def pushbutton_d20_spell_5_0():
        pushbutton_d20_spell_5(0)


    def pushbutton_d20_spell_5_1():
        pushbutton_d20_spell_5(1)


    def pushbutton_d20_spell_5_2():
        pushbutton_d20_spell_5(2)


    def pushbutton_d20_spell_5_3():
        pushbutton_d20_spell_5(3)


    def pushbutton_d20_spell_5_4():
        pushbutton_d20_spell_5(4)


    def pushbutton_d20_spell_5_5():
        pushbutton_d20_spell_5(5)


    def pushbutton_d20_spell_5_6():
        pushbutton_d20_spell_5(6)


    def pushbutton_d20_spell_5_7():
        pushbutton_d20_spell_5(7)


    def pushbutton_d20_spell_5_8():
        pushbutton_d20_spell_5(8)


    def pushbutton_d20_spell_5_9():
        pushbutton_d20_spell_5(9)


    def init_widget_buttons():
        """функция инцииализации всех кнопок виджета"""
        widget[0].pushButton_info.clicked.connect(pushbutton_info_0)
        widget[0].pushButton_generation.clicked.connect(pushbutton_generation_0)
        widget[0].pushButton_reset.clicked.connect(pushbutton_reset_0)
        widget[0].pushButton_load.clicked.connect(pushbutton_load_0)
        widget[0].pushButton_save.clicked.connect(pushbutton_save_0)
        widget[0].pushButton_incoming_damage_enter.clicked.connect(pushbutton_incoming_damage_enter_0)
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


def pushbutton_info(i: int):  # i - widget number
    main_menu.textEdit_battlelog.append('info')
    pass


def pushbutton_generation(i: int):  # i - widget number

    # определение типа 0 - не выбрано, 1...len(NPC_types_dict) - остальные типы
    if widget[i].comboBox_type.currentIndex() == 0:  # 0 индекс - ничего не выбрано
        widget[i].comboBox_type.setCurrentIndex(randint(1, len(NPC_types_dict)))  # устанавливает случайное значение
    this_type = widget[i].comboBox_type.currentText()

    # определение пола: 0 - не выбрано, 1 - Ж, 2 - М, 3 - Н (нет)
    if widget[i].comboBox_gender.currentIndex() == 0:  # если пол не выбран
        if NPC_types_dict[this_type]['has_sex'] == 0:  # если пола нет установаить 3 - Н
            widget[i].comboBox_gender.setCurrentIndex(3)
            gender_for_Person = None  # значение для работы класса Person, для генерации имени
        else:
            if randint(1, 100) >= NPC_types_dict[this_type]['male_percent']:
                widget[i].comboBox_gender.setCurrentIndex(1)
                gender_for_Person = Gender.FEMALE  # значение для работы класса Person, для генерации имени
            else:
                widget[i].comboBox_gender.setCurrentIndex(2)
                gender_for_Person = Gender.MALE  # значение для работы класса Person, для генерации имени
    this_gender = widget[i].comboBox_gender.currentText()

    # определение класса: 0 - не выбрано, 1 - Trash, 2 - Elite, 3 - Legend
    if widget[i].comboBox_trash_elite_legend.currentIndex() == 0:  # если класс не выбран
        trash_elite_legend_random = randint(1, 100)
        if trash_elite_legend_random <= NPC_types_dict[this_type]['elite_chance']:
            widget[i].comboBox_trash_elite_legend.setCurrentIndex(2)
            class_factor = 2
        elif trash_elite_legend_random <= NPC_types_dict[this_type]['elite_chance'] + NPC_types_dict[this_type]['legend_chance']:
            widget[i].comboBox_trash_elite_legend.setCurrentIndex(3)
            class_factor = 3
        else:
            widget[i].comboBox_trash_elite_legend.setCurrentIndex(1)
            class_factor = 1
    this_class = widget[i].comboBox_trash_elite_legend.currentText()

    # подбор имени
    person = person_ru  # тут, возможно, будут варианты для других стран
    text = text_ru
    if len(widget[i].lineEdit_name.text()) == 0:  # Если в "имя" ничего не введено:
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
                    widget[i].lineEdit_name.setText(f"{this_first_name} {this_nick}{this_last_name}")
                else:
                    widget[i].lineEdit_name.setText(f"{this_last_name} {this_nick}")
        else:
            widget[i].lineEdit_name.setText(f"{this_class} {this_type}")

    # определим уровень
    if len(widget[i].lineEdit_lvl.text()) == 0:
        widget[i].lineEdit_lvl.setText(str(randint(NPC_types_dict[this_type]['min_lvl'],NPC_types_dict[this_type]['max_lvl'])))



def pushbutton_reset(i: int):  # i - widget number
    pass


def pushbutton_load(i: int):  # i - widget number
    pass


def pushbutton_save(i: int):  # i - widget number
    pass


def pushbutton_incoming_damage_enter(i: int):  # i - widget number
    pass


def pushbutton_attack(i: int):  # i - widget number
    pass


def pushbutton_d20_physique(i: int):  # i - widget number
    pass


def pushbutton_d20_mastery(i: int):  # i - widget number
    pass


def pushbutton_d20_skill_1(i: int):  # i - widget number
    pass


def pushbutton_d20_skill_2(i: int):  # i - widget number
    pass


def pushbutton_d20_skill_3(i: int):  # i - widget number
    pass


def pushbutton_d20_skill_4(i: int):  # i - widget number
    pass


def pushbutton_d20_intelligence(i: int):  # i - widget number
    pass


def pushbutton_d20_spell_1(i: int):  # i - widget number
    pass


def pushbutton_d20_spell_2(i: int):  # i - widget number
    pass


def pushbutton_d20_spell_3(widget_number: int):  # i - widget number
    pass


def pushbutton_d20_spell_4(i: int):  # i - widget number
    pass


def pushbutton_d20_spell_5(i: int):  # i - widget number
    pass


def main():
    global widget, WidgetNPС, widgets_counter, main_menu, person_ru, text_ru
    person_ru = Person('ru') # объект Person для генерации личных данных NPC
    text_ru = Text('ru') # объект для генерации некотрых слов
    app = QtWidgets.QApplication(sys.argv)  # init application
    MainWindow = QtWidgets.QMainWindow()  # Create form main menu создание формы окна главного меню
    widgets_counter = 0
    widget = []
    WidgetNPС = []
    for i in range(0, 10):  # создаём виджеты NPC от 0 до 9
        widget.append(Ui_NPC_Widget())
        WidgetNPС.append(QtWidgets.QWidget())
        widget[i].setupUi(WidgetNPС[i])
        widget[i].comboBox_type.addItems(NPC_types_dict)
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
    init_widget_buttons()
    main_menu = Ui_MainWindow()
    main_menu.setupUi(MainWindow)
    MainWindow.show()
    main_menu.pushButton_add_NPC.clicked.connect(pushbutton_add_npc)
    main_menu.pushButton_remove_NPC.clicked.connect(pushbutton_remove_npc)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
