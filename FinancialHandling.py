#FinancialHandling.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QTransform, QIcon
from AccountManagement.AccountHandling import AccountWindow
from connection import AccountManager
from FinancialTransactions.Deposit import DepositWidget
from FinancialTransactions.Transfer import TransferWidget
from FinancialTransactions
class FinancialWidget(QWidget):
    go_back = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Financial Menu")
        self.setGeometry(100, 100, 400, 300)

        self.button_layout = QGridLayout()

        self.deposit_button = QPushButton("Deposit Money", self)
        self.deposit_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 14px; }"
                                      "QPushButton:hover { background-color: #3e8e41; }"
                                      "QPushButton:pressed { background-color: #2e7d32; }")

        self.button_layout.addWidget(self.deposit_button, 0, 0, 1, 2)

        self.transfer_button = QPushButton("Transfer Money", self)
        self.transfer_button.setStyleSheet("QPushButton { background-color: #00bcd4; color: white; font-size: 14px; }"
                                        "QPushButton:hover { background-color: #0097a7; }"
                                        "QPushButton:pressed { background-color: #00838f; }")

        self.button_layout.addWidget(self.transfer_button, 1, 0, 1, 2)

        self.withdraw_button = QPushButton("Withdraw Money", self)
        self.withdraw_button.setStyleSheet("QPushButton { background-color: #009688; color: white; font-size: 14px; }"
                                      "QPushButton:hover { background-color: #00796b; }"
                                      "QPushButton:pressed { background-color: #00695c; }")

        self.button_layout.addWidget(self.withdraw_button, 2, 0, 1, 2)
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setStyleSheet("QPushButton {"
            "   background-color: #f44336;"  # Red background color
            "   color: white;"                # White text color
            "   font-size: 14px;"             # Font size
            "   padding: 10px 20px;"          # Padding (top/bottom, left/right)
            "}"
            "QPushButton:hover {"
            "   background-color: #e53935;"   # Darker red background color on hover
            "}"
            "QPushButton:pressed {"
            "   background-color: #d32f2f;"   # Even darker red background color when pressed
            "}")
        
        self.button_layout.addWidget(self.back_button, 3, 0, 1, 1)
        
        spacer = QLabel("", self)
        self.button_layout.addWidget(spacer, 3, 1, 1, 1)
        
        self.setLayout(self.button_layout)
        
        self.account_manager = AccountManager(server=r"DESKTOP-K8BIO91\SQLEXPRESS", database="BankSystem")
        self.deposit_widget = DepositWidget(self.account_manager)
        self.deposit_widget.go_back.connect(self.show)  # Connect the signal to a slot that shows FinancialWidget
        
        self.transfer_widget = TransferWidget(self.account_manager)
        self.transfer_widget.go_back.connect(self.show)
        
        font = QFont("Arial", 14)
        self.deposit_button.setFont(font)
        self.transfer_button.setFont(font)
        self.withdraw_button.setFont(font)
        self.back_button.setFont(font)
        
        pixmap = QPixmap("back_icon.png")
        transform = QTransform().rotate(-90)
        back_icon = QIcon(pixmap.transformed(transform))
        self.back_button.setIcon(back_icon)
        self.back_button.clicked.connect(self.go_back_to_main_menu)
        self.deposit_button.clicked.connect(self.show_deposit_form)
        self.transfer_button.clicked.connect(self.show_transfer_form)

        def show_deposit_form(self):
        self.deposit_widget.show()
        self.close() 
        
    def show_transfer_form(self):
        self.transfer_widget.show()
        self.close()
        
    def go_back_to_main_menu(self):
        self.go_back.emit()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinancialWidget()
    window.show()
    sys.exit(app.exec_())
