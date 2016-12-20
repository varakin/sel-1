import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_css_selector("#box-apps-menu li:nth-child(3)").click()
    driver.find_element_by_css_selector(".dataTable .row td:nth-child(5) a").click()

    buttons = driver.find_elements_by_css_selector("tr .fa.fa-external-link")
    current_window_handle = driver.current_window_handle
    wait = WebDriverWait(driver, 5)

    for button in buttons:
        window_handles = driver.window_handles
        button.click()

        wait.until(EC.new_window_is_opened(window_handles))

        for window_handle in driver.window_handles:
            if window_handle != current_window_handle:
                driver.switch_to_window(window_handle)
                driver.close()
                driver.switch_to_window(current_window_handle)
                break
        else:
            return False
