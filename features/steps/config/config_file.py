from configparser import ConfigParser
file = "C:/Users/shuai.wang/PycharmProjects/project1_bdd/features/steps/config/config.ini"

class config():
    config = ConfigParser()
    config.read(file)
    userName = config["account"]["user"]
    passWord = config["account"]["pass"]
    homePage = config["homepage"]["url"]
    athelet1 = config["athelet"]["athelet1"]
    athelet2 = config["athelet"]["athelet2"]


