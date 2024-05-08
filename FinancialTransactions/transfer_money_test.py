import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from unittest.mock import MagicMock
from Transfer import TransferWidget

class TestTransferWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_widget_creation(self):
        account_manager_mock = MagicMock()  # Create a mock account manager
        transfer_widget = TransferWidget(account_manager_mock)  # Provide the mock account manager as argument
        self.assertIsNotNone(transfer_widget)

    def test_transfer_with_empty_fields(self):
        account_manager_mock = MagicMock()  # Create a mock account manager
        transfer_widget = TransferWidget(account_manager_mock)  # Provide the mock account manager as argument

        # Mocking QMessageBox.critical to check if it is called with the expected message
        QMessageBox.critical = MagicMock()

        # Making the transfer with empty fields
        transfer_widget.transfer()

        # Assert that QMessageBox.critical was called with the expected message
        QMessageBox.critical.assert_called_with(
            transfer_widget,
            "Error",
            "Please fill in all the fields!",
        )

    def test_transfer_with_invalid_amount(self):
        account_manager_mock = MagicMock()  # Create a mock account manager
        transfer_widget = TransferWidget(account_manager_mock)  # Provide the mock account manager as argument

        # Mocking QMessageBox.critical to check if it is called with the expected message
        QMessageBox.critical = MagicMock()

        # Entering an invalid amount
        transfer_widget.from_account_input.setText("ulp56728972075787")
        transfer_widget.to_account_input.setText("ulp56728972075787")
        transfer_widget.amount_input.setText("invalid")

        # Making the transfer
        transfer_widget.transfer()

        # Assert that QMessageBox.critical was called with the expected message
        QMessageBox.critical.assert_called_with(
            transfer_widget,
            "Error",
            "Invalid amount! Please enter a valid amount of money.",
        )

    # Add more test methods for other scenarios...

if __name__ == "__main__":
    unittest.main()
