import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton
from Login_form import AdvancedLoginForm  # Adjust the import path as per your project structure

class TestAdvancedLoginForm(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_init_ui(self):
        form = AdvancedLoginForm()
        self.assertIsInstance(form, AdvancedLoginForm)
        self.assertEqual(form.windowTitle(), "Login")
        self.assertIsNotNone(form.layout)

        # Test whether widgets are correctly initialized
        self.assertIsInstance(form.Name_input, QLineEdit)
        self.assertIsInstance(form.Email_input, QLineEdit)
        self.assertIsInstance(form.Password_input, QLineEdit)
        self.assertIsInstance(form.login_button, QPushButton)
        self.assertIsInstance(form.create_button, QPushButton)

    def test_handle_login_click(self):
        form = AdvancedLoginForm()

        # Patching the show method to prevent GUI from showing
        with patch.object(form, 'show'):
            form.Name_input.setText("ali")
            form.Email_input.setText("ali@gmail.com")
            form.Password_input.setText("ali1")

            form.handle_login_click()

            # Test if the QMessageBox is shown for successful login
            self.assertTrue(form.isHidden())

            # Test if appropriate warning message is shown for missing fields
            form.Name_input.clear()
            form.handle_login_click()
            self.assertFalse(form.isHidden())  # Form should still be visible

            form.Name_input.setText("ali")
            form.Email_input.clear()
            form.handle_login_click()
            self.assertFalse(form.isHidden())  # Form should still be visible

            form.Email_input.setText("ali@gmail.com")
            form.Password_input.clear()
            form.handle_login_click()
            self.assertFalse(form.isHidden())  # Form should still be visible

if __name__ == "__main__":
    unittest.main()
