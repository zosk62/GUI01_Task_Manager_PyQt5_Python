from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import sys

import sqlite3

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main2.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.removeButton.clicked.connect(self.removeSelectedTask)  
        
    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        self.updateTaskList(dateSelected)
        
    def addNewTask(self):
        db = sqlite3.connect("tasks.db")
        cursor = db.cursor()
        newTask = str(self.taskLineEdit.text())
        date = self.calendarWidget.selectedDate().toPyDate()
        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date, )
        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.taskLineEdit.clear()
        
    def updateTaskList(self, date):
        self.listWidget.clear()
        db = sqlite3.connect("tasks.db")
        cursor = db.cursor()
        query = "SELECT task, completed FROM tasks where date=?"
        row = (date, )
        results = cursor.execute(query, row).fetchall()
        for result in results:
            task = str(result[0])
            completed = result[1]

            # Check if the task is not empty before adding it to the list
            if task:
                item = QListWidgetItem(task)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)          
                item.setCheckState(Qt.Checked if completed == "Yes" else Qt.Unchecked)
                self.listWidget.addItem(item)



    def saveChanges(self):
        db = sqlite3.connect("tasks.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()
        
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            task = item.text()
            
            if item.checkState() == Qt.Checked:
                query = "UPDATE tasks set completed ='Yes' where task =? AND date =?" 
            else: 
                query = "UPDATE tasks set completed ='No' where task =? AND date =?" 
            row = (task, date, )
            cursor.execute(query, row)
        db.commit()
        
        messageBox = QMessageBox()
        messageBox.setText("Changes saved")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def removeSelectedTask(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            task = selected_item.text()
            db = sqlite3.connect("tasks.db")
            cursor = db.cursor()
            query = "DELETE FROM tasks WHERE task = ? AND date = ?"
            row = (task, self.calendarWidget.selectedDate().toPyDate())
            cursor.execute(query, row)
            db.commit()
            db.close()
            self.updateTaskList(self.calendarWidget.selectedDate().toPyDate())
        else:
            self.show_warning("Select a task to remove.")

    def show_warning(self, message):
        messageBox = QMessageBox()
        messageBox.setText(message)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
