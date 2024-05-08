# # main.py
# import sys
# from PyQt5.QtWidgets import QApplication
# from gui import AccountManagementApp
# from connection import AccountManager

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = AccountManagementApp()

#     # Replace these values with your SQL Server database credentials
#     server = r"DESKTOP-K8BIO91\SQLEXPRESS"  # Use raw string literal
#     database = "BankSystem"


#     account_manager = AccountManager(server, database)
#     window.show()
#     sys.exit(app.exec_())

import sys

from PyQt5.QtWidgets import QApplication

from gui import AccountManagementApp
from connection import AccountManager

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Initialize the connection to the database
    server = r"DESKTOP-K8BIO91\SQLEXPRESS"  # User name 
    database = "BankSystem"              # database name

    account_manager = AccountManager(server, database)

    bank_system = account_manager

    window = AccountManagementApp(bank_system)

    window.show()

    sys.exit(app.exec())
