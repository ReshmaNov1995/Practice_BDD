import time

from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@Given("my bank balance")
def link(context):
    context.kk=65000       #so we can access this variable globally
    print("My account balance is",context.kk)


@When("deducted amount")
def un(context):
    emi=10000
    print("The deducted amount is",context.kk-emi)



