import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_xpath("//li[@id='app-']/a/span[2]").click() #Appearence
    driver.find_element_by_id("doc-template").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-logotype").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[2]").click() #Catalogqw
    driver.find_element_by_id("doc-catalog").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-product_groups").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-option_groups").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-manufacturers").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-suppliers").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-delivery_statuses").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-sold_out_statuses").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-quantity_units").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-csv").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[3]").click() #Countries

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[4]").click()    #Currencies

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[5]").click()    #Customers
    driver.find_element_by_id("doc-customers").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-csv").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-newsletter").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[6]").click()    #Geo Zones

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[7]").click()    #Languages
    driver.find_element_by_id("doc-languages").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-storage_encoding").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[8]").click()    #Modules
    driver.find_element_by_id("doc-jobs").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-customer").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-shipping").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-payment").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-order_total").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-order_success").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-order_action").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[9]").click()    #Orders
    driver.find_element_by_id("doc-orders").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-order_statuses").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[10]").click()    #Pages

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[11]").click()    #Reports
    driver.find_element_by_id("doc-monthly_sales").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-most_sold_products").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-most_shopping_customers").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[12]").click()    #Settings
    driver.find_element_by_id("doc-store_info").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-defaults").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-general").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-listings").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-images").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-checkout").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-advanced").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-security").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[13]").click()    #Slides

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[14]").click()    #Tax
    driver.find_element_by_id("doc-tax_classes").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-tax_rates").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[15]").click()    #Translations
    driver.find_element_by_id("doc-search").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-scan").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_id("doc-csv").click()
    driver.find_element_by_tag_name("h1")

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[16]").click()    #Users

    driver.find_element_by_xpath("(//li[@id='app-']/a/span[2])[17]").click()    #vQmods
    driver.find_element_by_id("doc-vqmods").click()
    driver.find_element_by_tag_name("h1")
