import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver(request):
    dc = DesiredCapabilities.CHROME
    dc['loggingPrefs'] = {'browser': 'ALL'}
    wd = webdriver.Chrome(desired_capabilities=dc)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("#box-apps-menu-wrapper li:nth-child(2)").click()
    driver.find_element_by_css_selector(".dataTable tr:nth-child(3) a").click()
    rows = driver.find_elements_by_css_selector(".dataTable .row")
    ducks = []

    for i, row in enumerate(rows):
        if i < 3:
            continue

        ducks.append(row.find_element_by_css_selector("a").get_property('href'))

    for duck in ducks:
        driver.get(duck)
        print(driver.get_log("browser"))
        driver.back()
