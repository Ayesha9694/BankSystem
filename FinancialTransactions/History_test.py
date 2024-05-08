import unittest
from unittest.mock import MagicMock  # Import MagicMock for mocking
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from History import TransactionHistoryWidget

class TestTransactionHistoryWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_widget_creation(self):
        account_manager_mock = MagicMock()  # Mocking the account manager object
        transaction_history_widget = TransactionHistoryWidget(account_manager_mock)
        self.assertIsNotNone(transaction_history_widget)

    def test_set_account_number(self):
        account_manager_mock = MagicMock()  # Mocking the account manager object
        transaction_history_widget = TransactionHistoryWidget(account_manager_mock)
        account_number = "ulp69563308663380"
        transaction_history_widget.set_account_number(account_number)
        # Add assertions here to check if the history is loaded with the provided account number

    def test_load_history(self):
        account_manager_mock = MagicMock()  # Mocking the account manager object
        transaction_history_widget = TransactionHistoryWidget(account_manager_mock)
        account_number = "ulp69563308663380"
        transaction_history_widget.load_history(account_number)
        # Add assertions here to check if the history is loaded correctly
        
if __name__ == "__main__":
    unittest.main()
