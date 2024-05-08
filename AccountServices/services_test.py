import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from unittest.mock import MagicMock
from services import ServiceRequestWidget

class TestServiceRequestWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def test_widget_creation(self):
        service_request_widget = ServiceRequestWidget()
        self.assertIsNotNone(service_request_widget)

    def test_submit_request(self):
        service_request_widget = ServiceRequestWidget()

        # Set up test data
        service_request_widget.request_combo.setCurrentIndex(0)  # Select "Checkbook" from combo box
        service_request_widget.details_input.setText("Need a new checkbook")  # Enter details

        # Mock QMessageBox.information() to check if it's called
        QMessageBox.information = MagicMock()

        # Trigger the submit_request function
        service_request_widget.submit_request()

        # Check if the request is added to the table
        self.assertEqual(service_request_widget.request_table.rowCount(), 1)
        self.assertEqual(service_request_widget.request_table.item(0, 0).text(), "Checkbook")
        self.assertEqual(service_request_widget.request_table.item(0, 1).text(), "Need a new checkbook")
        self.assertEqual(service_request_widget.request_table.item(0, 2).text(), "Pending")

        # Check if QMessageBox.information() is called with the correct arguments
        QMessageBox.information.assert_called_once_with(
            service_request_widget,
            "Request Submitted",
            "Your request will be processed within 10 days."
        )

        # Check if input fields are cleared after submitting the request
        self.assertEqual(service_request_widget.details_input.text(), "")

 
if __name__ == "__main__":
    unittest.main()
