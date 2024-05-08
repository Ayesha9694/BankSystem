import unittest
from PyQt5.QtWidgets import QApplication
from accountinfo import GetAccountInfoWidget

class TestGetAccountInfoWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

 

if __name__ == '__main__':
    unittest.main()
