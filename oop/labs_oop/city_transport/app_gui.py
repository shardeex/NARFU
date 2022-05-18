import sys
from typing import cast

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt

Ui_MainWindow, QtBaseClass = uic.loadUiType('oop/labs_oop/city_transport/app.ui')

class RouteModel(QtCore.QAbstractListModel):
    def __init__(self, *args, routes=[], **kwargs):
        super(RouteModel, self).__init__(*args, **kwargs)
        self.routes = routes

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            text = self.routes[index.row()]
            return text

        '''
        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return QtGui.QColor('green')'''

    def rowCount(self, index):
        return len(self.routes)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = RouteModel()
        self.routeListView.setModel(self.model)

        self.routeAddButton.pressed.connect(self.add_route)
        self.routeDeleteButton.pressed.connect(self.delete_route)

    def add_route(self):
        start = cast(QtCore.QTime, self.routeStartTimeEdit.time())
        end = cast(QtCore.QTime, self.routeEndTimeEdit.time())

        hours = end.hour() - start.hour()
        minutes = end.minute() - start.minute()
        if minutes < 0:
            hours -= 1
            minutes += 60
        if hours < 0:
            hours += 24

        vehicle = self.routeVehicleBox.currentText()
        driver = self.routeDriverBox.currentText()

        self.model.routes.append(f"{hours:02d}:{minutes:02d} | {vehicle} ({driver})")
        self.model.layoutChanged.emit()
    
    def delete_route(self):
        indexes = self.routeListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.routes[index.row()]
            self.model.layoutChanged.emit()
            self.routeListView.clearSelection()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
