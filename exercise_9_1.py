import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def check_alph(collection):
    texts = [text for text in collection]

    return texts == sorted(texts)


def test_example(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    rows = driver.find_elements_by_css_selector(".dataTable .row")
    countries = [row.find_element_by_css_selector('td:nth-child(5) a') for row in rows]
    names = [country.text for country in countries]
    urls = [country.get_property('href') for country in countries]
    zones_numbers = [row.find_element_by_css_selector('td:nth-child(6)').text for row in rows]

    for i, row in enumerate(rows):
        if int(zones_numbers[i]) != 0:
            driver.get(urls[i])
            cities = driver.find_elements_by_css_selector("#table-zones tr:not(:last-child) td:nth-child(3)")

            if not check_alph([city.text for city in cities]):
                return False

            driver.back()

    return check_alph(names)


