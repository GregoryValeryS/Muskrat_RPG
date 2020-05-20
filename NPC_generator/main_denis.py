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
    global click_counter_add_NPC
    if click_counter_add_NPC < 9:
        click_counter_add_NPC += 1
    if click_counter_add_NPC == 1:
        WidgetNPС_1.show()
    elif click_counter_add_NPC == 2:
        WidgetNPС_2.show()
    elif click_counter_add_NPC == 3:
        WidgetNPС_3.show()
    elif click_counter_add_NPC == 4:
        WidgetNPС_4.show()
    elif click_counter_add_NPC == 5:
        WidgetNPС_5.show()
    elif click_counter_add_NPC == 6:
        WidgetNPС_6.show()
    elif click_counter_add_NPC == 7:
        WidgetNPС_7.show()
    elif click_counter_add_NPC == 8:
        WidgetNPС_8.show()
    elif click_counter_add_NPC == 9:
        WidgetNPС_9.show()


def pb_remove_npc():
    global click_counter_add_NPC
    click_counter_add_NPC -= 1
    WidgetNPС_1.close()


def bptest():
    widget_1.lineEdit_name.setText('test')

def bptest2():
    widget_2.lineEdit_name.setText('test')


def test():
    text = Text('ru')
    print(text.swear_word())
    print(text.answer())
    print(text.level())
    print(text.word())

    person = Person('ru')  # сы создали объект person, класса Person()

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
    app = QtWidgets.QApplication(sys.argv)  # init application
    MainWindow = QtWidgets.QMainWindow()  # Create form main menu создание формы окна главного меню
    # Create NPC widgets создание формы виджетов NPC
    global click_counter_add_NPC, widget_1, widget_2, widget_3, widget_4, widget_5, widget_6, widget_7, widget_8, widget_9, WidgetNPС_1, WidgetNPС_2, WidgetNPС_3, WidgetNPС_4, WidgetNPС_5, WidgetNPС_6, WidgetNPС_7, WidgetNPС_8, WidgetNPС_9
    click_counter_add_NPC = 0
    widget_1 = Ui_NPC_Widget()
    WidgetNPС_1 = QtWidgets.QWidget()
    widget_1.setupUi(WidgetNPС_1)
    widget_2 = Ui_NPC_Widget()
    WidgetNPС_2 = QtWidgets.QWidget()
    widget_2.setupUi(WidgetNPС_2)
    widget_3 = Ui_NPC_Widget()
    WidgetNPС_3 = QtWidgets.QWidget()
    widget_3.setupUi(WidgetNPС_3)
    widget_4 = Ui_NPC_Widget()
    WidgetNPС_4 = QtWidgets.QWidget()
    widget_4.setupUi(WidgetNPС_4)
    widget_5 = Ui_NPC_Widget()
    WidgetNPС_5 = QtWidgets.QWidget()
    widget_5.setupUi(WidgetNPС_5)
    widget_6 = Ui_NPC_Widget()
    WidgetNPС_6 = QtWidgets.QWidget()
    widget_6.setupUi(WidgetNPС_6)
    widget_7 = Ui_NPC_Widget()
    WidgetNPС_7 = QtWidgets.QWidget()
    widget_7.setupUi(WidgetNPС_7)
    widget_8 = Ui_NPC_Widget()
    WidgetNPС_8 = QtWidgets.QWidget()
    widget_8.setupUi(WidgetNPС_8)
    widget_9 = Ui_NPC_Widget()
    WidgetNPС_9 = QtWidgets.QWidget()
    widget_9.setupUi(WidgetNPС_9)
    # init main menu UI - инициализация формы главного меню:
    main_menu = Ui_MainWindow()
    main_menu.setupUi(MainWindow)
    MainWindow.show()
    # описание действия кнопок главного меню:
    widget_1.pushButton_generation.clicked.connect(bptest)
    widget_2.pushButton_generation.clicked.connect(bptest2)
    main_menu.pushButton_add_NPC.clicked.connect(pb_add_npc)
    main_menu.pushButton_remove_NPC.clicked.connect(pb_remove_npc)
    # Run main loop:
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
