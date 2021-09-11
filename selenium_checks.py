#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


target_url = "${{ secrets.EXT_IP }}/install"
#target_url = "http://34.88.214.184/install"

print("########## Running the Selenium Script ##########")

@pytest.fixture(scope="session")
def get_driver():
    global driver
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield
    driver.close()

@pytest.mark.usefixtures("get_driver")
def test_data():
    driver.get(target_url)
    element = driver.find_element_by_tag_name("h3")
    print("########## Checking for AdminEmail field on the page ##########")
    assert element.text == "Store information"

#@pytest.mark.usefixtures("get_driver")
#def test_body():
#    element = driver.find_element_by_xpath('//*[@id="mainMenu"]/form/a[1]')
#    print("########## Checking for Login Button ##########")
#    assert element.text == "Log in"

