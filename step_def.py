import time

from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@Given("lims link")
def link(context):
    global driver
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(4)


@When("enter the user name")
def un(context):
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
    print("user name entered successfully")



@When("enter the password")
def pswd(context):
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
    time.sleep(3)
    print("password entered successfully")


@Then("click on the login button")
def loginbutton(context):
    driver.find_element_by_xpath("//*[text()='Login']").click()