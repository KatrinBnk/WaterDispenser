import sys
import os
from PyQt6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QPixmap
from PyQt6.QtCore import Qt, QPoint, QRect

import design


class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.volume_selected = False
        self.paid = False
        self.selected_volume = -1
        self.filling = False
        self.fill_timer = None
        self.fill_bottle = False

        self.ui = design.Ui_MainWindow()
        self.ui.setupUi(self)

        #начальный интрефейс
        self.reset_program()

        # первый этап: выбор объема
        self.ui.water1.clicked.connect(lambda: self.selection_volume(1))
        self.ui.water5.clicked.connect(lambda: self.selection_volume(5))
        self.ui.water19.clicked.connect(lambda: self.selection_volume(19))

        # второй этап: оплата
        self.ui.true_card.clicked.connect((lambda: self.reset_text(2)))
        self.ui.false_card.clicked.connect((lambda: self.reset_text(3)))

        # третий этап: поместить тару
        self.ui.put_bottle.clicked.connect(lambda: self.reset_text(4))

        # четвртый этап: наполение тары
        self.ui.pushButton.clicked.connect(lambda: self.reset_text(6))

        # пятый этап: забрать тару
        self.ui.pick_up_bottle.clicked.connect(lambda: self.Pick_UP_bottle())

        # движение объектов



    def selection_volume(self, volume):
        self.volume_selected = True
        self.selected_volume = volume
        self.ui.welcome_text.setText(f'Выбран объем {volume} л')
        self.timer(volume)

    def timer(self, i):
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: self.reset_text(i))
        timer.start(5000)

    def reset_text(self, i):
        if i == 0:
            self.reset_program()

        elif self.volume_selected:
            if i in (1, 5, 19):
                self.ui.welcome_text.setText('Ожидание оплаты')
            elif i == 2:
                self.apply_correct_card()
            elif i == 3:
                self.apply_incorrect_card()
            elif i == 4:
                self.bottle()
            elif i == 6:
                self.filling_bottle()
        else:
            self.ui.welcome_text.setText('Объем не выбран')
            self.timer(0)

    def apply_correct_card(self):
        if self.paid:
            self.ui.welcome_text.setText('Поместите тару в автомат')
        else:
            card_balance = self.read_card_balance  # Read the card's balance from a text file

            if card_balance >= self.selected_volume and self.selected_volume != -1:
                #self.ui.card.move(224, 434)
                self.paid = True
                self.update_card_balance(card_balance,
                                         self.selected_volume)  # Deduct the selected volume from the card's balance
                self.ui.welcome_text.setText('Поместите тару в автомат')
            else:
                self.ui.welcome_text.setText('ОШИБКА: Недостаточно средств на карте')
                self.timer(0)

    def update_card_balance(self, current_balance, selected_volume):
        pass

    @property
    def read_card_balance(self):
        return 100

    def apply_incorrect_card(self):
        if self.paid:
            self.ui.welcome_text.setText('Оплата уже выполнена.\n Неправильная карта не влияет на процесс.')
        else:
            self.ui.welcome_text.setText(
                'Карта не найдена')
            self.timer(0)

    def bottle(self):
        if self.paid and self.volume_selected:
            self.ui.welcome_text.setText('Ожидание пуска')
            self.ui.bottle.move(80, 240)
            self.ui.bottle.raise_()
        else:
            self.ui.welcome_text.setText('вы лох')

    def filling_bottle(self):
        if self.filling:
            self.stop_filling()
        else:
            self.start_filling()

    def start_filling(self):
        if self.paid and self.volume_selected:
            self.ui.welcome_text.setText('Наполнение')
            self.filling = True

            if self.fill_timer is not None:
                self.fill_timer.stop()

            interval = 5000 * self.selected_volume
            self.fill_timer = QTimer(self)
            self.fill_timer.setSingleShot(True)
            self.fill_timer.timeout.connect(self.stop_filling)
            self.fill_timer.start(interval)
        else:
            self.ui.welcome_text.setText('Вы лох')

    def stop_filling(self):
        self.filling = False
        if self.fill_timer is not None:
            self.fill_timer.stop()
        self.ui.welcome_text.setText('Заберите тару')
        self.fill_bottle = True

    def Pick_UP_bottle(self):
        if self.fill_bottle:
            self.ui.bottle.move(445, 290)
            self.reset_program()
        else:
            pass

    def reset_program(self):

        # сброс параметров
        self.volume_selected = False
        self.paid = False
        self.selected_volume = -1
        self.filling = False
        if self.fill_timer is not None:
            self.fill_timer.stop()
        self.fill_timer = None
        self.fill_bottle = False

        # сброс кнопок
        self.ui.water1.setChecked(False)
        self.ui.water5.setChecked(False)
        self.ui.water19.setChecked(False)
        self.ui.true_card.setChecked(False)
        self.ui.false_card.setChecked(False)
        self.ui.put_bottle.setChecked(False)
        self.ui.pushButton.setChecked(False)
        self.ui.pick_up_bottle.setChecked(False)

        # сброс приглашения
        self.ui.welcome_text.setText('Ожидание выбора объема')


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec())


if __name__ != '__main__':
    pass
else:
    main()
