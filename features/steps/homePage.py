from behave import *
from selenium import webdriver
from locators.homepage import homePage
import time

@when('I click Home')
def step_impl(context):
    homeLogo = homePage.home_logo
    context.driver.find_element_by_css_selector(homeLogo).click()
    time.sleep(1)

@then('I successfully go to the Home page')
def step_impl(context):
    homeLogo = homePage.home_logo
    status = context.driver.find_element_by_css_selector(homeLogo).is_displayed()
    status is True

@when('I click Explore')
def step_impl(context):
    explore = homePage.menu_explore
    context.driver.find_element_by_css_selector(explore).click()
    time.sleep(1)

@then('I successfully go to the Explore page')
def step_impl(context):
    explore = homePage.explore_page
    status = context.driver.find_element_by_id(explore).is_displayed()
    status is True


@when('I click Notifications')
def step_impl(context):
    notification = homePage.menu_notification
    context.driver.find_element_by_id(notification).click()
    time.sleep(1)

@then('I successfully go to the Notification content')
def step_impl(context):
    notification_content = homePage.notification_content
    status = context.driver.find_element_by_id(notification_content).is_displayed()
    status is True

@when('I click Messages')
def step_impl(context):
    messages = homePage.menu_messages
    context.driver.find_element_by_xpath(messages).click()
    time.sleep(1)

@then('I successfully go to the Messages App')
def step_impl(context):
    messages_app = homePage.message_app
    status = context.driver.find_element_by_id(messages_app).is_displayed()
    status is True

@when('I click Account')
def step_impl(context):
    account = homePage.userMenu_xpath
    context.driver.find_element_by_xpath(account).click()
    time.sleep(1)

@then('I successfully go to the User Menu')
def step_impl(context):
    user_menu = homePage.logOutLink_css_selector
    status = context.driver.find_element_by_css_selector(user_menu).is_displayed()
    status is True