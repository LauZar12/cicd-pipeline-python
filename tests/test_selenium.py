import pytest
import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.app import app


# Fixture to run Flask in a background thread
@pytest.fixture(scope="module")
def test_app():
    """Run the Flask app in a separate thread for testing."""

    def run():
        app.run(port=5000, debug=False, use_reloader=False)

    thread = Thread(target=run)
    thread.daemon = True
    thread.start()
    time.sleep(1)
    yield app


@pytest.fixture(scope="module")
def browser():
    """Set up headless Chrome for Selenium."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.quit()


def test_homepage_loads(test_app, browser):
    """Check if homepage loads correctly."""
    browser.get("http://localhost:5000")
    assert "Just a calculator, man." in browser.title


def test_addition(test_app, browser):
    """Test addition functionality."""
    browser.get("http://localhost:5000")
    time.sleep(0.5)  #
