import unittest
from PyQt5.QtWidgets import QApplication
from report import ReportIssueWidget

class TestReportIssueWidget(unittest.TestCase):
    def test_widget_creation(self):
        app = QApplication([])
        report_issue_widget = ReportIssueWidget()

        # Check if the widget is created without errors
        self.assertIsNotNone(report_issue_widget)

if __name__ == "__main__":
    unittest.main()
