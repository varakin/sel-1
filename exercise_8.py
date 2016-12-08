import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/")

    ducks = driver.find_elements_by_css_selector(".product.column.shadow.hover-light")

    for duck in ducks:
        stickers = duck.find_elements_by_class_name('sticker')

        if len(stickers) != 1:
            return False

    return True
