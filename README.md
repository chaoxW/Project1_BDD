<!--
  * browser: architecture
  * version: 1.2.0
  * updated: 2020-02-17T02:39:34Z
  * contact: Shuai Wang (shuai.wang.kaos@gmail.com)
-->

# Project1 BDD for GUI automation test

Use Selenium and BDD to make the automation test

Contents:

* [Why use BDD](#why-use-bdd)
* [The architecture information](#the-architecture-information)
* [Configure the enviroment](#configure-the-enviroment)
* [How to run the tests](#how-to-run-the-tests)


## Why use BDD

* High visibility. By using a language understood by all, everyone gets strong visibility into the project’s progression.

* Scenarios focus on the expected behaviors of the product. 

* BDD is designed to speed up the development process

* EBDD is an evolution of TDD. 


## The architecture information

The project has four folders to manage the project:

  * **..\features**
    *  the features folder contains all the feature files
    *  run `behave -f allure_behave.formatter:AllureFormatter -o reports/ features` from command line to launch all the tests

  * **..\features\steps\config**
    * **..\features\steps\Config\config.ini** this file manage all the data for the tests for example users,url and athletes for the query test, it is easy for the maintanence afterwards
    * **..\features\steps\Config\config_file.py** this file is used for parsing the data from ..\Config\config.ini which can import for step definitions

  * **..\Report**
    * This folder receives the reports when tests complete  

  * **..\features\steps**
    * This folder contains all the step definitions for the scenarios

## Configure the enviroment:

  * Install behave
    * use `pip install behave`
    * the version is behave 1.2.6

  * Install selenium
    * use `pip install selenium`
    * the version is selenium 3.141.0

  * Install configparser
    * use `pip install configparser`
    * the version is configparser 5.0.1

  * download webdriver for Chrome (FF, IE)
    * add the drivers to the PATH C:\Users\*****\AppData\Local\Programs\Python\Python39\Scripts

## How to run the tests:
  * you can run from command line with `behave -f allure_behave.formatter:AllureFormatter -o reports/ features` from the path ..\features
  * the report should be generated in the **..\Report** folder

