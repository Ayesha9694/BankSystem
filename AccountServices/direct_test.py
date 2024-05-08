import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QDateTime
from unittest.mock import MagicMock
from DirectDebits import RecurringPaymentsWidget

class TestRecurringPaymentsWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_widget_creation(self):
        account_manager_mock = MagicMock()
        recurring_payments_widget = RecurringPaymentsWidget(account_manager_mock)
        self.assertIsNotNone(recurring_payments_widget)

    def test_update_ui(self):
        account_manager_mock = MagicMock()
        recurring_payments_widget = RecurringPaymentsWidget(account_manager_mock)

        # Test when the type is "Direct Debit"
        recurring_payments_widget.type_combo.setCurrentIndex(1)  # Select "Direct Debit"
        recurring_payments_widget.update_ui()
        self.assertTrue(recurring_payments_widget.direct_debit_widget.isVisible())
        self.assertFalse(recurring_payments_widget.details_input.isVisible())
        self.assertFalse(recurring_payments_widget.amount_input.isVisible())

        # Test when the type is "Recurring Payment"
        recurring_payments_widget.type_combo.setCurrentIndex(0)  # Select "Recurring Payment"
        recurring_payments_widget.update_ui()
        self.assertFalse(recurring_payments_widget.direct_debit_widget.isVisible())
        self.assertTrue(recurring_payments_widget.details_input.isVisible())
        self.assertTrue(recurring_payments_widget.amount_input.isVisible())

    def test_fetch_account_number(self):
        account_manager_mock = MagicMock()
        recurring_payments_widget = RecurringPaymentsWidget(account_manager_mock)

        # Test when the fetch operation is successful
        recurring_payments_widget.fetch_account_number = MagicMock(return_value="ulp69563308663380")
        account_number = recurring_payments_widget.fetch_account_number()
        self.assertEqual(account_number, "ulp69563308663380")

        # Test when the fetch operation fails
        recurring_payments_widget.fetch_account_number = MagicMock(side_effect=Exception("Database connection error"))
        account_number = recurring_payments_widget.fetch_account_number()
        self.assertIsNone(account_number)

if __name__ == "__main__":
    unittest.main()
