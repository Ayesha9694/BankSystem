import unittest
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QRect
from Homepage import HomePage

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.home_page = HomePage()

    def tearDown(self):
        self.home_page.deleteLater()
        self.app.quit()

    def test_home_page_init(self):
        self.assertEqual(self.home_page.windowTitle(), "Home Page")
        self.assertEqual(self.home_page.geometry(), QRect(100, 100, 400, 300))
        self.assertIsInstance(self.home_page.login_button, QPushButton)
        self.assertEqual(self.home_page.login_button.text(), "Login")
        self.assertEqual(self.home_page.login_button.styleSheet(), "background-color: #4CAF50; color: white")
        self.assertEqual(len(self.home_page.layout()), 2)  # Check if two widgets are added to the layout

    def test_show_login_form(self):
        self.home_page.show_login_form()
        self.assertTrue(self.home_page.login_form.isVisible())

if __name__ == '__main__':
    unittest.main()
