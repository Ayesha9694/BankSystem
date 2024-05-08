import unittest
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from unittest.mock import MagicMock
from   ViewDetailed import AccountServicesHistory

class TestAccountServicesHistory(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_load_history(self):
        # Mock the account_manager object
        account_manager_mock = MagicMock()
        history_data = [
            (1, "123456789", "Deposit", 100.0, "2024-05-09 12:30:00"),
            (2, "123456789", "Withdrawal", 50.0, "2024-05-10 10:45:00"),
        ]
        account_manager_mock.cursor.fetchall.return_value = history_data

        # Create an instance of AccountServicesHistory
        account_services_history = AccountServicesHistory(account_manager_mock)

        # Set the account number and load history
        account_services_history.set_account_number("123456789")

        # Check if the history table is populated correctly
        self.assertEqual(account_services_history.history_table.rowCount(), len(history_data))
        for row_idx, row_data in enumerate(history_data):
            for col_idx, value in enumerate(row_data):
                item = account_services_history.history_table.item(row_idx, col_idx)
                self.assertIsNotNone(item)
                self.assertEqual(item.text(), str(value))

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
