#https://realpython.com/python-pyqt-layout/

import sys

from PyQt5.QtWidgets import *

class Start_dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('KillPass-One password to rule them all')
        self.dlgLayout = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.qLineEdit = QLineEdit()
        self.formLayout.addRow('Your Master Key:', self.qLineEdit)
        self.dlgLayout.addLayout(self.formLayout)
        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.btns.accepted.connect(self.get_master_key)
        self.btns.rejected.connect(self.show_application_dialog)
        self.dlgLayout.addWidget(self.btns)
        self.setLayout(self.dlgLayout)

    def get_master_key(self):
        i, j = self.formLayout.getWidgetPosition(self.qLineEdit)
        #print(i, j)
        widget_item = self.formLayout.itemAt(i, j)
        widget = widget_item.widget()
        text = widget.text()
        print(f'Master key is {text}')


    def show_application_dialog(self):
        # clear previous layout
        self.clearLayout(self.formLayout)
        
        # Decrypt the encrypted files using the master key. Caution the master key should always be in the memory.
        
        #show the new layout. Preferably should have a split view like nordPass.




    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()   
        self.btns.setVisible(False)
        start_dialog.resize(800, 500) # Do not hard code it. Make it full screen thats all...





start_dialog = None
if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_dialog = Start_dialog()
    start_dialog.show()
    sys.exit(app.exec_())
    