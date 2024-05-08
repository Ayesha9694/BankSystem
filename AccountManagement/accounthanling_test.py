import unittest
from PyQt5.QtWidgets import QApplication
from AccountHandling import AccountWindow
class TestAccountWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_create_account_button_click(self):
        # Create an instance of AccountWindow
        window = AccountWindow()

        # Emit the create_account_info_signal by clicking the create account button
        window.create_account_info_button.click()

        # Assert that the create_account widget is shown
        self.assertEqual(window.create_account.isVisible(), True)

    def test_update_account_button_click(self):
        # Create an instance of AccountWindow
        window = AccountWindow()

        # Emit the update_account_signal by clicking the update account button
        window.update_account_button.click()

        # Assert that the update_form widget is shown
        self.assertEqual(window.update_form.isVisible(), True)

    def test_delete_account_button_click(self):
        # Create an instance of AccountWindow
        # window = AccountWindow()

        # Emit the delete_account_signal by clicking the delete account button
        window.delete_account_button.click()

        # Assert that the delete_form widget is shown
        self.assertEqual(window.delete_form.isVisible(), True)

if __name__ == '__main__':
    unittest.main()
