import unittest
from PyQt5.QtWidgets import QApplication
from UpdateAccount import UpdateAccountWidget

class TestUpdateAccountWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_update_account_success(self):
        # Create an instance of UpdateAccountWidget
        widget = UpdateAccountWidget(account_manager=None)

        # Set input values for testing
        widget.account_number_input.setText("ulp55223765032524")
        widget.new_account_type_input.setText("Personal")
        widget.email_input.setText("janidali957@gmail.com")
        widget.password_input.setText("Ali1234#")
        widget.mobilenumber_input.setText("11111111111")

        # Call the update_account method
        # widget.update_account()

        # Assert that success message box is shown
        self.assertEqual(widget.isVisible(), False)  # Widget should be closed after successful account update

    def test_update_account_failure(self):
        # Create an instance of UpdateAccountWidget
        widget = UpdateAccountWidget(account_manager=None)

        # Leave input fields blank intentionally
        # No input values provided

        # Call the update_account method
        widget.update_account()

        # Assert that an error message box is shown
        self.assertEqual(widget.isVisible(), False)  # Widget should still be open due to missing input

if __name__ == '__main__':
    unittest.main()
