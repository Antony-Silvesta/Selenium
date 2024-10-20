from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_google_search():
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['goog:chromeOptions'] = {'w3c': False}

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )
    driver.get("http://www.google.com")
    assert "Google" in driver.title
    driver.quit()
