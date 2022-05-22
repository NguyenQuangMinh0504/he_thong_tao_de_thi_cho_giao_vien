import sys
import PyQt5
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QCompleter, QLineEdit

app = QApplication(sys.argv)

model = QStringListModel()
model.setStringList(['some', 'words', 'in', 'my', 'dictionary'])

completer = QCompleter()
completer.setModel(model)

lineedit = QLineEdit()
lineedit.setCompleter(completer)
lineedit.show()

sys.exit(app.exec_())