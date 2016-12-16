import pytest
from selenium import webdriver
from time import gmtime, strftime, sleep


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    #создание новенького
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/")
    driver.find_element_by_css_selector("#box-account-login tr:nth-child(5) a").click()
    driver.find_element_by_name("firstname").send_keys("qwerty")
    driver.find_element_by_name("lastname").send_keys("qwerty")
    driver.find_element_by_name("address1").send_keys("qwerty")
    driver.find_element_by_name("postcode").send_keys("191191")
    driver.find_element_by_name("city").send_keys("qwerty")
    the_best_email = strftime("varakin%H%M%S@mail.ru", gmtime())
    driver.find_element_by_name("email").send_keys(the_best_email)
    driver.find_element_by_name("phone").send_keys("+79999999999")
    driver.find_element_by_name("password").send_keys("qwerty")
    driver.find_element_by_name("confirmed_password").send_keys("qwerty")
    driver.find_element_by_name("create_account").click()

    #логаут из новосозданного
    driver.find_element_by_css_selector("#box-account li:nth-child(4) a").click()

    #повторный вход в новосозданный
    driver.find_element_by_name("email").send_keys(the_best_email)
    driver.find_element_by_name("password").send_keys("qwerty")
    driver.find_element_by_name("login").click()

    #логаут еще раз
    driver.find_element_by_css_selector("#box-account li:nth-child(4) a").click()





