import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def find_selected_option(select):
    idx = select.get_property("selectedIndex")
    option = select.find_element_by_css_selector("option:nth-child(%s)" % (idx+1))
    return option.text


def test_example(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    rows = driver.find_elements_by_css_selector(".dataTable .row")
    countries = [row.find_element_by_css_selector('td:nth-child(3) a') for row in rows]
    urls = [country.get_property('href') for country in countries]

    for i, row in enumerate(rows):
        driver.get(urls[i])
        zones = driver.find_elements_by_css_selector("#table-zones td:nth-child(3) select")
        zone_names = list(map(find_selected_option, zones))

        assert zone_names == sorted(zone_names)

        driver.back()



