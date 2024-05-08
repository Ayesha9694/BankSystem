import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from unittest.mock import MagicMock
from Deposit import DepositWidget

class TestDepositWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_widget_creation(self):
        deposit_widget = DepositWidget()
        self.assertIsNotNone(deposit_widget)

    def test_make_deposit_with_empty_fields(self):
        deposit_widget = DepositWidget()
        
        # Mocking QMessageBox.critical to check if it is called with the expected message
        QMessageBox.critical = MagicMock()

        # Making the deposit with empty fields
        deposit_widget.make_deposit()

        # Assert that QMessageBox.critical was called with the expected message
        QMessageBox.critical.assert_called_with(
            deposit_widget,
            "Error",
            "Please fill in all the fields!",
        )

    def test_make_deposit_with_invalid_amount(self):
        deposit_widget = DepositWidget()
        
        # Mocking QMessageBox.critical to check if it is called with the expected message
        QMessageBox.critical = MagicMock()

        # Setting account manager mock
        deposit_widget.account_manager = MagicMock()

        # Entering an invalid amount
        deposit_widget.account_number_input.setText("ulp69563308663380")
        deposit_widget.amount_input.setText("invalid")

        # Making the deposit
        deposit_widget.make_deposit()

        # Assert that QMessageBox.critical was called with the expected message
        QMessageBox.critical.assert_called_with(
            deposit_widget,
            "Error",
            "pleace enter a valid amount!",
        )

    # Add more test methods for other scenarios...

if __name__ == "__main__":
    unittest.main()
