import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont



class SeatAssigner(QWidget):
    def __init__(self):
        super().__init__()
        self.namen = ["Bob", "Alice", "Susan", "Charlie"]
        self.sitzplaetze = list(range(1, 5))
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Zufälliger Sitzplatz-Zuweiser')
        self.layout = QVBoxLayout()
        self.welcome_label = QLabel('Willkommen beim Zufälligen Sitzplatz-Zuweiser!', self)
        self.welcome_label.setFont(QFont('Arial', 16))
        self.layout.addWidget(self.welcome_label)
        self.prompt_button = QPushButton('Drücke die Eingabetaste, um die Sitzplätze zufällig zuzuweisen', self)
        self.prompt_button.setFont(QFont('Arial', 14))
        self.prompt_button.clicked.connect(self.zufaellige_zuweisung)
        self.layout.addWidget(self.prompt_button)
        self.result_labels = []
        for _ in range(len(self.namen)):
            label = QLabel('', self)
            label.setFont(QFont('Arial', 14))
            self.result_labels.append(label)
            self.layout.addWidget(label)
        self.setLayout(self.layout)
        self.resize(400, 300)
        self.show()

    def zufaellige_zuweisung(self):
        random.shuffle(self.namen)
        random.shuffle(self.sitzplaetze)
        sitzzuweisungen = list(zip(self.namen, self.sitzplaetze))
        for i, (name, platz) in enumerate(sitzzuweisungen):
            self.result_labels[i].setText(f"{name} sitzt auf Platz {platz}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SeatAssigner()
    sys.exit(app.exec_())
