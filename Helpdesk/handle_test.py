import unittest
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from unittest.mock import MagicMock
from Helpdesk.handle import HelpHandleMain

class TestHelpHandleMain(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_widget_creation(self):
        help_handle_main = HelpHandleMain()
        self.assertIsNotNone(help_handle_main)

    def test_open_helpdesk(self):
        help_handle_main = HelpHandleMain()
        help_handle_main.open_helpdesk()
        # Add an assertion to check if the helpdesk widget is created and shown
        self.assertTrue(help_handle_main.helpdesk_widget.isVisible())

    def test_open_report_issue(self):
        help_handle_main = HelpHandleMain()
        help_handle_main.open_report_issue()
        # Add an assertion to check if the report issue widget is created and shown
        self.assertTrue(help_handle_main.report_issue_widget.isVisible())

    def test_go_back_button(self):
        help_handle_main = HelpHandleMain()
        help_handle_main.go_back.emit()
        # Add an assertion to check if the go_back signal is emitted
        self.assertTrue(help_handle_main.isVisible())

if __name__ == "__main__":
    unittest.main()
