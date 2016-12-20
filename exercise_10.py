import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/")
    first_product = driver.find_element_by_css_selector("#box-campaigns .name").get_attribute("textContent")
    first_price = driver.find_element_by_css_selector("#box-campaigns .campaign-price").get_attribute("textContent")
    first_color_old_price = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("color")
    first_style_old_price = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("text-decoration")
    first_color_new_price = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("color")
    first_style_new_price = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("font-weight")
    driver.find_element_by_css_selector("#box-campaigns .image").click()

    second_product = driver.find_element_by_css_selector("#box-product .title").get_attribute("textContent")
    second_price = driver.find_element_by_css_selector("#box-product .campaign-price").get_attribute("textContent")
    second_color_old_price = driver.find_element_by_css_selector("#box-product .regular-price").value_of_css_property("color")
    second_style_old_price = driver.find_element_by_css_selector("#box-product .regular-price").value_of_css_property("text-decoration")
    second_color_new_price = driver.find_element_by_css_selector("#box-product .campaign-price").value_of_css_property("color")
    second_style_new_price = driver.find_element_by_css_selector("#box-product .campaign-price").value_of_css_property("font-weight")

    assert first_product == second_product
    assert first_price == second_price
    assert first_color_old_price == second_color_old_price
    assert first_style_old_price == second_style_old_price
    assert first_color_new_price == second_color_new_price
    assert first_style_new_price == second_style_new_price

    sleep(3)