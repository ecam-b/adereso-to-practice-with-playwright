from pages.auth.login_page import LoginPage
from config.settings import Config
from playwright.sync_api import expect
import pytest

@pytest.mark.skip
def test_user_can_login(set_up_no_auth):
    page = set_up_no_auth
    login_p = LoginPage(page)
    login_p.navigate(f"{Config.URL}/vue/#/login")
    login_p.login(Config.USER, Config.PASSWORD)

    expect(page.get_by_role("link", name="AderesoPostcenter")).to_be_visible(timeout=30000)

def test_check_stats(set_up):
    # El fixture 'set_up' ya nos entrega una página LOGUEADA y en el Inbox
    page = set_up
    page.goto(f"{Config.URL}/#/admin/channels/")
    expect(page.get_by_role("link", name="Horario de trabajo")).to_be_visible(timeout=20000)