from behave import *
from selenium import webdriver
from config.config_file import config
from locators.loginpage import loginPage
import time

@given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@given('open login page')
def step_impl(context):
    url = config.homePage
    context.driver.get(url)

@then('verify login page form')
def step_impl(context):
    status = context.driver.find_element_by_class_name("login-container").is_displayed()
    assert status is True

@then('close browser')
def step_impl(context):
    context.driver.close()
    time.sleep(1)


@when('insert username and password')
def step_impl(context):
    username = config.userName
    password = config.passWord
    usernameLocator = loginPage.userName_textbox_id
    passLocator = loginPage.passWord_textbox_id
    context.driver.find_element_by_id(usernameLocator).send_keys(username)
    context.driver.find_element_by_id(passLocator).send_keys(password)


@when('click the login button')
def step_impl(context):
    loginButton = loginPage.login_button_id
    context.driver.find_element_by_id(loginButton).click()
    time.sleep(3)


@then('User successfully login to the homepage')
def step_impl(context):
    homeLogo = loginPage.home_logo
    status = context.driver.find_element_by_css_selector(homeLogo).is_displayed()
    status is True

@when('insert invalid username and password')
def step_impl(context):
    username = config.userName
    password = "1234"
    usernameLocator = loginPage.userName_textbox_id
    passLocator = loginPage.passWord_textbox_id
    context.driver.find_element_by_id(usernameLocator).send_keys(username)
    context.driver.find_element_by_id(passLocator).send_keys(password)


@then('User unsuccessfully login to the homepage')
def step_impl(context):
    invalid_login_message = loginPage.login_error_message
    msg = context.driver.find_element_by_class_name(invalid_login_message).is_displayed()
    msg is True


