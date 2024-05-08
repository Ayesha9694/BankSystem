# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
# from Helpdesk.help import HelpdeskWidget
# from Helpdesk.report import ReportIssueWidget
# from PyQt5.QtCore import pyqtSignal
# from Helpdesk.report import ReportIssueWidget

# class HelpHandleMain(QWidget):
#     go_back = pyqtSignal()
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Help Handle Main")
#         self.setGeometry(100, 100, 400, 300)

#         self.helpdesk_button = QPushButton("Helpdesk")
#         self.report_issue_button = QPushButton("Report Issue")

#         self.helpdesk_button.clicked.connect(self.open_helpdesk)
#         self.report_issue_button.clicked.connect(self.open_report_issue)
#         self.report_issue_button.clicked.connect(self.show_transfer_form)
#         self.back_button = QPushButton("BACK")
#         self.back_button.clicked.connect(self.go_back_button)
        
#         layout = QVBoxLayout()
#         layout.addWidget(self.helpdesk_button)
#         layout.addWidget(self.report_issue_button)
#         layout.addWidget(self.back_button)
#         self.setLayout(layout)
        
#         self.setStyleSheet("""
#             QPushButton {
#                 background-color: #5c3d88;
#                 color: white;
#                 padding: 8px 16px;
#                 border: none;
#                 border-radius: 4px;
#                 font-weight: bold;
#                 font-size: 14px;
#             }

#             QPushButton:hover {
#                 background-color: #4a2f6d;
#             }

#             QPushButton:pressed {
#                 background-color: #35204a;
#             }
#         """)

#     def open_helpdesk(self):
#         self.helpdesk_widget = HelpdeskWidget()
#         self.helpdesk_widget.show()

#     def open_report_issue(self):
#         self.report_issue_widget = ReportIssueWidget()
#         self.report_issue_widget.show()
    
#     def go_back_button(self):
#         self.go_back.emit()
#         self.close()
#     def show_transfer_form(self):
#         try:
#             # Connect to the database
#             connection = pyodbc.connect(
#                 driver="{SQL Server}",
#                 server=r"DESKTOP-K8BIO91\SQLEXPRESS",
#                 database="BankSystem",
#                 trusted_connection="yes",
#             )

#             # Create a cursor to execute SQL queries
#             cursor = connection.cursor()

#             # Execute a query to retrieve the last logged-in account number from login_log table
#             cursor.execute("SELECT TOP 1  Name,account_number FROM login_log ORDER BY login_time DESC")
#             row = cursor.fetchone()

#             # Check if a row was returned
#             if row:
#                 from_account = row[1]
#                 Name = row[2]
#                 print("Successfully retrieved from_account:", from_account,Name)  # Debug print statement

#                 # Show the transfer form with the retrieved account number
#                 self.transfer_widget = report_issue_widget(self.account_manager,Name ,from_account)  # Pass both arguments
#                 print("From Account in homepage.py:", from_account) 
#                 self.transfer_widget.go_back.connect(self.show)  # Connect the signal to a slot that shows FinancialWidget
#                 self.transfer_widget.show()
#             else:
#                 QMessageBox.warning(self, "Warning", "No login history found.")
            
#             # Close the cursor and connection
#             cursor.close()
#             connection.close()
#         except pyodbc.Error as e:
#             QMessageBox.warning(self, "Error", f"Error retrieving login history: {e}")

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     main_interface = HelpHandleMain()
#     main_interface.show()
#     sys.exit(app.exec_())
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from Helpdesk.help import HelpdeskWidget
from Helpdesk.report import ReportIssueWidget
from PyQt5.QtCore import pyqtSignal

import pyodbc

class HelpHandleMain(QWidget):
    go_back = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help Handle Main")
        self.setGeometry(100, 100, 400, 300)

        self.helpdesk_button = QPushButton("Helpdesk")
        self.report_issue_button = QPushButton("Report Issue")

        self.helpdesk_button.clicked.connect(self.open_helpdesk)
        self.report_issue_button.clicked.connect(self.open_report_issue)
        self.back_button = QPushButton("BACK")
        self.back_button.clicked.connect(self.go_back_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.helpdesk_button)
        layout.addWidget(self.report_issue_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #5c3d88;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                font-weight: bold;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #4a2f6d;
            }

            QPushButton:pressed {
                background-color: #35204a;
            }
        """)

    def open_helpdesk(self):
        self.helpdesk_widget = HelpdeskWidget()
        self.helpdesk_widget.show()

    def open_report_issue(self):
        self.get_user_info()
        self.report_issue_widget = ReportIssueWidget(self.user_name, self.account_number)
        self.report_issue_widget.show()
    
    def go_back_button(self):
        self.go_back.emit()
        self.close()

    def get_user_info(self):
        try:
            # Connect to the database
            connection = pyodbc.connect(
                driver="{SQL Server}",
                server=r"DESKTOP-K8BIO91\SQLEXPRESS",
                database="BankSystem",
                trusted_connection="yes",
            )

            # Create a cursor to execute SQL queries
            cursor = connection.cursor()

            # Execute a query to retrieve the user name and account number from the login_log table
            cursor.execute("SELECT TOP 1 Name,account_number FROM login_log ORDER BY login_time DESC")
            row = cursor.fetchone()

            # Check if a row was returned
            if row:
                self.user_name, self.account_number = row
            else:
                QMessageBox.warning(self, "No Login History", "No login history found.")
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
        except pyodbc.Error as e:
            QMessageBox.warning(self, "Database Error", f"Error retrieving user information: {e}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_interface = HelpHandleMain()
    main_interface.show()
    sys.exit(app.exec_())
