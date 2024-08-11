import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from TranslationFromOneNumberSystemToAnotherWindow import Ui_MainWindow


class QuestionCostTour(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_convert.clicked.connect(self.num_system_transform)

    def num_system_transform(self):
        self.number = int(self.lbl_number.text())
        self.system_first = int(self.sb_system_first.value())
        self.system_second = int(self.sb_system_second.value())

        self.number_in_system = ''
        self.numbers_and_letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        flag = True

        for i in self.numbers_and_letters[self.system_first:]:
            if i in str(self.number):
                flag = False
                break

        if not flag:
            self.lbl_end_number.setText("Неверные данные")
        else:
            self.number_in_10_system = int(str(self.number), int(self.system_first))
            while self.number_in_10_system > 0:
                if self.system_second == 10:
                    self.number_in_system += str(self.number_in_10_system % 10)
                    self.number_in_10_system //= 10
                elif self.system_second > 10:
                    self.number_in_system += self.numbers_and_letters[self.number_in_10_system % self.system_second]
                    self.number_in_10_system //= self.system_second
                else:
                    self.number_in_system += str(self.number_in_10_system % self.system_second)
                    self.number_in_10_system //= self.system_second

            self.number_in_system = self.number_in_system[::-1]
            self.lbl_end_number.setText(self.number_in_system)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qct = QuestionCostTour()
    qct.show()
    sys.exit(app.exec())
