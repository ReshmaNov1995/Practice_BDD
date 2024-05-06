import time

from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@Given("lims1 {LIMSlink} test")
def link(context,LIMSlink):
    global driver
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    time.sleep(3)
    print("The passed link is",LIMSlink)
    driver.get(LIMSlink)
    time.sleep(4)


@When("enter1 the {LIMSuser} name")
def un(context,LIMSuser):
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys(LIMSuser)
    print("user name entered successfully211221")



@When("enter1 the {LIMSpassword}")
def pswd(context,LIMSpassword):
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys(LIMSpassword)
    time.sleep(3)
    print("password entered successfully212121")


@Then("click1 on the login button")
def loginbutton(context):
    driver.find_element_by_xpath("//*[text()='Login']").click()