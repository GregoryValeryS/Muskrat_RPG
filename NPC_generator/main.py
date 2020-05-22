from mimesis import Person
from mimesis.enums import Gender
from mimesis import Text
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main_menu import Ui_MainWindow
from ui_NPC_widget import Ui_NPC_Widget


def init_app_and_create_forms():
    pass


def pb_add_npc():
    global counter_NPC
    if counter_NPC <= 9:
        WidgetNPС[counter_NPC].show()
        counter_NPC += 1


def pb_remove_npc():
    global counter_NPC
    if counter_NPC >= 1:
        counter_NPC -= 1
        WidgetNPС[counter_NPC].close()


def bptest(widget_number=1):
    print(widget_number)
    widget[widget_number].lineEdit_name.setText('test')


def test():
    text = Text('ru')
    print(text.swear_word())
    print(text.answer())
    print(text.level())
    print(text.word())

    person = Person('ru')  # мы создали объект person, класса Person()

    man = person.full_name(gender=Gender.FEMALE)
    woman = person.full_name(gender=Gender.MALE)
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
    global widget, WidgetNPС, counter_NPC
    app = QtWidgets.QApplication(sys.argv)  # init application
    MainWindow = QtWidgets.QMainWindow()  # Create form main menu создание формы окна главного меню
    counter_NPC = 0
    widget = []
    WidgetNPС = []
    for i in range(0, 10):
        print(i)
        widget.append(Ui_NPC_Widget())
        WidgetNPС.append(QtWidgets.QWidget())
        widget[i].setupUi(WidgetNPС[i])
        widget[i].pushButton_info.clicked.connect(bptest)
        widget[i].pushButton_generation.clicked.connect(bptest)
        widget[i].pushButton_reset.clicked.connect(bptest)
        widget[i].pushButton_load.clicked.connect(bptest)
        widget[i].pushButton_save.clicked.connect(bptest)
        widget[i].pushButton_incoming_damage_enter.clicked.connect(bptest)
        widget[i].pushButton_attack.clicked.connect(bptest)
        widget[i].pushButton_d20_physique.clicked.connect(bptest)
        widget[i].pushButton_d20_mastery.clicked.connect(bptest)
        widget[i].pushButton_d20_skill_1.clicked.connect(bptest)
        widget[i].pushButton_d20_skill_2.clicked.connect(bptest)
        widget[i].pushButton_d20_skill_3.clicked.connect(bptest)
        widget[i].pushButton_d20_skill_4.clicked.connect(bptest)
        widget[i].pushButton_d20_intelligence.clicked.connect(bptest)
        widget[i].pushButton_d20_spell_1.clicked.connect(bptest)
        widget[i].pushButton_d20_spell_2.clicked.connect(bptest)
        widget[i].pushButton_d20_spell_3.clicked.connect(bptest)
        widget[i].pushButton_d20_spell_4.clicked.connect(bptest)
        widget[i].pushButton_d20_spell_5.clicked.connect(bptest)
    main_menu = Ui_MainWindow()
    main_menu.setupUi(MainWindow)
    MainWindow.show()
    main_menu.pushButton_add_NPC.clicked.connect(pb_add_npc)
    main_menu.pushButton_remove_NPC.clicked.connect(pb_remove_npc)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
