import unittest
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from Transfer import FinancialWidget
class TestFinancialWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_init_ui(self):
        widget = FinancialWidget()

        # Check if the window title is set correctly
        self.assertEqual(widget.windowTitle(), "Financial Menue")

        # Check if the buttons are initialized correctly
        self.assertIsInstance(widget.deposit_button, QPushButton)
        self.assertIsInstance(widget.transfer_button, QPushButton)
        self.assertIsInstance(widget.withdraw_button, QPushButton)
        self.assertIsInstance(widget.history_button, QPushButton)

        # Check if the labels are initialized correctly
        self.assertIsInstance(widget.history_label, QLabel)

        # Check if the table is initialized correctly
        self.assertIsInstance(widget.history_table, QTableWidget)
        self.assertEqual(widget.history_table.columnCount(), 5)
        self.assertEqual(widget.history_table.horizontalHeaderItem(0).text(), "Transaction ID")
        self.assertEqual(widget.history_table.horizontalHeaderItem(1).text(), "Account Number")
        self.assertEqual(widget.history_table.horizontalHeaderItem(2).text(), "Transaction Type")
        self.assertEqual(widget.history_table.horizontalHeaderItem(3).text(), "Amount")
        self.assertEqual(widget.history_table.horizontalHeaderItem(4).text(), "Date")

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
