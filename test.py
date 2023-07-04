from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QPoint


class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        class DraggableLabel(QLabel):
            def __init__(self, text, parent):
                super().__init__(text, parent)
                self.setMouseTracking(True)
                self.dragging = False
                self.offset = QPoint()

            def mousePressEvent(self, event):
                if event.button() == Qt.MouseButton.LeftButton:
                    self.dragging = True
                    self.offset = event.pos()

            def mouseMoveEvent(self, event):
                if self.dragging and event.buttons() == Qt.MouseButton.LeftButton:
                    new_pos = self.mapToParent(event.pos() - self.offset)
                    self.move(new_pos)

            def mouseReleaseEvent(self, event):
                if event.button() == Qt.MouseButton.LeftButton:
                    self.dragging = False

        self.label1 = DraggableLabel("Перетаскиваемый элемент 1", self)
        self.label1.setGeometry(10, 10, 200, 30)
        self.label1.setStyleSheet("background-color: yellow;")

        self.label2 = DraggableLabel("Перетаскиваемый элемент 2", self)
        self.label2.setGeometry(10, 50, 200, 30)
        self.label2.setStyleSheet("background-color: lightblue;")


app = QApplication([])
window = ExampleApp()
window.show()
app.exec()
