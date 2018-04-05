from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class App:

    def __init__(self):
        self.app = QApplication(["gomoku"])
        self.w = QWidget()
        self.w.setGeometry(800, 800, 250, 150)  # x, y, w, h
        self.w.setWindowTitle("Gomoku")

        label = QLabel("Hello", self.w)
        label.setToolTip("This is a <b>QLabel</b> widget with Tooltip")
        label.resize(label.sizeHint())
        label.move(80, 50)

        self.w.show()
        input()

if __name__ == "__main__":

    app = App()