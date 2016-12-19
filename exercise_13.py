import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/")
    wait = WebDriverWait(driver, 3)

    quantity = int(driver.find_element_by_css_selector("#cart > a.content > span.quantity").text)
    driver.find_element_by_css_selector("#box-most-popular a[title='Red Duck']").click()
    driver.find_element_by_name("add_cart_product").click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"), str(quantity+1)))
    driver.get("http://localhost/litecart/")

    quantity = int(driver.find_element_by_css_selector("#cart > a.content > span.quantity").text)
    driver.find_element_by_css_selector("#box-most-popular a[title='Blue Duck']").click()
    driver.find_element_by_name("add_cart_product").click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"), str(quantity+1)))
    driver.get("http://localhost/litecart/")

    quantity = int(driver.find_element_by_css_selector("#cart > a.content > span.quantity").text)
    driver.find_element_by_css_selector("#box-most-popular a[title='Green Duck']").click()
    driver.find_element_by_name("add_cart_product").click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"), str(quantity+1)))
    driver.get("http://localhost/litecart/")

    driver.get("http://localhost/litecart/en/checkout")
    blocks = driver.find_elements_by_css_selector("#box-checkout-cart .item > form > div")

    for i in range(len(blocks)):
        block = driver.find_element_by_css_selector("#box-checkout-cart .item > form > div")
        item_name = block.find_element_by_tag_name("strong").text
        cells = driver.find_elements_by_css_selector("#order_confirmation-wrapper td.item")

        for cell in cells:
            if cell.text == item_name:
                block.find_element_by_name("remove_cart_item").click()
                wait.until(EC.staleness_of(cell))
                break
        else:
            raise Exception()



