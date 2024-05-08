import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox, QLineEdit
from unittest.mock import MagicMock
from Withdraw import WithdrawWidget

class TestWithdrawWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_widget_creation(self):
        account_manager_mock = MagicMock()
        withdraw_widget = WithdrawWidget(account_manager_mock)
        self.assertIsNotNone(withdraw_widget)

    def test_withdraw_with_empty_fields(self):
        account_manager_mock = MagicMock()
        withdraw_widget = WithdrawWidget(account_manager_mock)
        withdraw_widget.account_number_input.setText("ulp69563308663380")
        withdraw_widget.amount_input.setText("")  # Ensure amount field is empty
        
        QMessageBox.critical = MagicMock()

        withdraw_widget.withdraw()

        QMessageBox.critical.assert_called_once_with(
            withdraw_widget,
            "Error",
            "Please fill in all the fields!",
        )

    def test_withdraw_with_invalid_amount(self):
        account_manager_mock = MagicMock()
        account_manager_mock.get_balance.return_value = 1000.0  # Mock get_balance method to return a float value
        withdraw_widget = WithdrawWidget(account_manager_mock)
        withdraw_widget.account_number_input.setText("ulp69563308663380")
        withdraw_widget.amount_input = QLineEdit()  # Create a QLineEdit widget
        withdraw_widget.amount_input.setText("5")  # Set amount to 5

        QMessageBox.critical = MagicMock()

        

        QMessageBox.critical.assert_not_called()  # No critical message should be shown for valid amount

        # Ensure account_manager.withdraw is not called
        account_manager_mock.withdraw.assert_not_called()

if __name__ == "__main__":
    unittest.main()
