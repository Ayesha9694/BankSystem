#AccountHandling.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from AccountManagement.accountinfo import GetAccountInfoWidget
from AccountManagement.UpdateAccount import  UpdateAccountWidget
from AccountManagement.DeleteAccount import DeleteAccountWidget
from connection import AccountManager
class AccountWindow(QWidget):
    go_back = pyqtSignal()
    create_account_info_signal = pyqtSignal()
    update_account_signal = pyqtSignal()
    delete_account_signal = pyqtSignal()
    edit_account_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Account Management System")
        self.setGeometry(100, 100, 400, 300)

        self.button_layout = QVBoxLayout()

        self.create_account_info_button = QPushButton(" Account Information", self)
        self.create_account_info_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px;")
        self.create_account_info_button.clicked.connect(self.create_account_info_signal.emit)
        
        self.update_account_button = QPushButton("Update Account", self)
        self.update_account_button.setStyleSheet("background-color: #00bcd4; color: white; font-size: 14px;")
        self.update_account_button.clicked.connect(self.update_account_signal.emit)
        
        self.delete_account_button = QPushButton("Delete Account", self)
        self.delete_account_button.setStyleSheet("background-color: #f44336; color: white; font-size: 14px;")
        self.delete_account_button.clicked.connect(self.delete_account_signal.emit)
        
        # self.edit_account_button = QPushButton("Edit Account", self)
        # self.edit_account_button.setStyleSheet("background-color: #9c27b0; color: white; font-size: 14px;")
        # self.edit_account_button.clicked.connect(self.edit_account_signal.emit)
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setStyleSheet("background-color: #f44336; color: white; font-size: 14px; width: 80px;")
        self.back_button.clicked.connect(self.go_back_to_main_menu)
        
        self.button_layout.addWidget(self.create_account_info_button)
        self.button_layout.addWidget(self.update_account_button)
        self.button_layout.addWidget(self.delete_account_button)
        # self.button_layout.addWidget(self.edit_account_button)
        self.button_layout.addWidget(self.back_button)

        self.setLayout(self.button_layout)
        server = r"DESKTOP-K8BIO91\SQLEXPRESS"
        database = "BankSystem"
        account_manager = AccountManager(server, database)
        self.create_account = GetAccountInfoWidget(account_manager)
        self.create_account_info_button.clicked.connect(self.create_account.show)
        
        self.update_form = UpdateAccountWidget(account_manager)
        self.update_account_button.clicked.connect(self.update_form.show)
        
        self.delete_form = DeleteAccountWidget(account_manager)
        self.delete_account_button.clicked.connect(self.delete_form.show)
    
    
        
    def go_back_to_main_menu(self):
        self.go_back.emit()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())



