import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_css_selector("#box-apps-menu li:nth-child(2) a").click()
    driver.find_element_by_css_selector("#content a.button:nth-child(2)").click()

    #закладка General
    driver.find_element_by_css_selector("#tab-general input").click()
    driver.find_element_by_css_selector("#tab-general tr:nth-child(2) input").send_keys("qwerty")
    driver.find_element_by_name("code").send_keys("qwerty")
    driver.find_element_by_css_selector("#tab-general tr:nth-child(4) tr:nth-child(2) input").click()
    driver.find_element_by_css_selector("#tab-general tr:nth-child(7) tr:nth-child(3) input").click()
    quantity = driver.find_element_by_css_selector("#tab-general tr:nth-child(8) input")
    quantity.clear()
    quantity.send_keys("123")
    Quantity_Unit = Select(driver.find_element_by_name("quantity_unit_id"))
    Quantity_Unit.select_by_value('1')
    Delivery_Status = Select(driver.find_element_by_name("delivery_status_id"))
    Delivery_Status.select_by_value('1')
    Sold_Out_Status = Select(driver.find_element_by_name("sold_out_status_id"))
    Sold_Out_Status.select_by_value('2')
    driver.find_element_by_name("new_images[]").send_keys("c:\\xmapp\\passwords.txt")
    driver.find_element_by_name("date_valid_from").send_keys(Keys.HOME+"23.11.2016")
    driver.find_element_by_name("date_valid_to").send_keys(Keys.HOME + "23.11.2016")
    driver.find_element_by_class_name("trumbowyg-editor")

    sleep(10)

    #закладка Information
    driver.find_element_by_css_selector("#content li:nth-child(2) a").click()
    Manufacturer = Select(driver.find_element_by_name("manufacturer_id"))
    Manufacturer.select_by_value('1')
    driver.find_element_by_name("keywords").send_keys("qwerty")
    driver.find_element_by_name("short_description[en]").send_keys("qwerty")
    driver.find_element_by_class_name("trumbowyg-editor").send_keys("qwertyqwerty")
    driver.find_element_by_name("head_title[en]").send_keys("qwerty")
    driver.find_element_by_name("meta_description[en]").send_keys("qwerty")

    #закладка Prices
    driver.find_element_by_css_selector("#content li:nth-child(4) a").click()
    quantity = driver.find_element_by_name("purchase_price")
    quantity.clear()
    quantity.send_keys("123")
    purchase_price = Select(driver.find_element_by_name("purchase_price_currency_code"))
    purchase_price.select_by_value('USD')
    driver.find_element_by_name("prices[USD]").send_keys("123")
    driver.find_element_by_name("prices[EUR]").send_keys("123")




