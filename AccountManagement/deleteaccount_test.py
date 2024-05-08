import unittest
from PyQt5.QtWidgets import QApplication
from DeleteAccount import DeleteAccountWidget

class TestDeleteAccountWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_delete_account_success(self):
        # Create an instance of DeleteAccountWidget
        widget = DeleteAccountWidget(account_manager=None)

        # Set input value for testing
        widget.account_number_input.setText("ulp84240071036334")

   

        # Assert that success message box is shown
        self.assertEqual(widget.isVisible(), False)  # Widget should be closed after successful account deletion

    def test_delete_account_failure(self):
        # Create an instance of DeleteAccountWidget
        widget = DeleteAccountWidget(account_manager=None)

        # Leave input field blank intentionally
        # No account number provided

        # Call the delete_account method
        widget.delete_account()

        # Assert that an error message box is shown
        self.assertEqual(widget.isVisible(), False)  # Widget should still be open due to missing input

if __name__ == '__main__':
    unittest.main()
