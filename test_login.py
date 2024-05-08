import pytest
from PyQt5.QtTest import QTest

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from Login_form import AdvancedLoginForm

@pytest.fixture
def app(qtbot):
    test_app = QApplication([])
    login_form = AdvancedLoginForm()
    qtbot.addWidget(login_form)
    login_form.show()
    yield test_app
    login_form.close()

def test_login_form_create_account_button(qtbot, app):
    assert app.activeWindow().objectName() == 'Login'
    qtbot.mouseClick(app.activeWindow().create_button, Qt.LeftButton)
    assert app.activeWindow().create_account_widget.isVisible()

def test_login_form_clear_fields(qtbot, app):
    assert app.activeWindow().objectName() == 'Login'
    app.activeWindow().Name_input.setText("John")
    app.activeWindow().Email_input.setText("john@example.com")
    app.activeWindow().Password_input.setText("password")
    qtbot.mouseClick(app.activeWindow().login_button, Qt.LeftButton)
    app.processEvents()
    assert app.activeWindow().Name_input.text() == ''
    assert app.activeWindow().Email_input.text() == ''
    assert app.activeWindow().Password_input.text() == ''
