from behave import *
from selenium import webdriver
from config.config_file import config
from locators.homepage import homePage
import time

@when('I query with Ronaldo Mulitalo')
def step_impl(context):
    athelet_query = config.athelet1
    query_xpath = homePage.query_xpath
    context.driver.find_element_by_xpath(query_xpath).send_keys(athelet_query)
    time.sleep(2)


@then('I successfully go to the Ronaldo Mulitalo page')
def step_impl(context):
    athelet_click = config.athelet1
    query_select1 = homePage.query_select_1
    query_select2 = homePage.query_select_2
    context.driver.find_element_by_xpath(query_select1+athelet_click+query_select2).click()
    time.sleep(2)
    query_validate1 = homePage.query_validate1
    query_validate2 = homePage.query_validate2
    status = context.driver.find_element_by_xpath(query_validate1 + athelet_click + query_validate2).is_displayed()
    status is True


@when('I query with Milan Hammond')
def step_impl(context):
    athelet_query = config.athelet2
    query_xpath = homePage.query_xpath
    context.driver.find_element_by_xpath(query_xpath).send_keys(athelet_query)
    time.sleep(2)


@then('I successfully go to the Milan Hammond page')
def step_impl(context):
    athelet_click = config.athelet2
    query_select1 = homePage.query_select_1
    query_select2 = homePage.query_select_2
    context.driver.find_element_by_xpath(query_select1 + athelet_click + query_select2).click()
    time.sleep(2)
    query_validate1 = homePage.query_validate1
    query_validate2 = homePage.query_validate2
    status = context.driver.find_element_by_xpath(query_validate1 + athelet_click + query_validate2).is_displayed()
    status is True

@when(u'I query with *')
def step_impl(context):
    query_xpath = homePage.query_xpath
    context.driver.find_element_by_xpath(query_xpath).send_keys("*")
    time.sleep(2)


@then(u'I unsuccessfully go to the * page')
def step_impl(context):
    query_negative = homePage.query_nega_validation
    status = context.driver.find_element_by_xpath(query_negative).is_displayed()
    status is True


@when(u'I query with !')
def step_impl(context):
    query_xpath = homePage.query_xpath
    context.driver.find_element_by_xpath(query_xpath).send_keys("!")
    time.sleep(2)


@then(u'I unsuccessfully go to the ! page')
def step_impl(context):
    query_negative = homePage.query_nega_validation
    status = context.driver.find_element_by_xpath(query_negative).is_displayed()
    status is True

