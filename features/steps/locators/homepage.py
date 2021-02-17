class homePage():
    # home page objects to click
    # menu home link
    home_logo = "a[data-qa-id='webnav-globalnav-home']"
    # menu explore
    menu_explore = "a[data-qa-id='webnav-globalnav-explore']"
    # menu notification
    menu_notification = "notifications-link"
    # menu messages
    menu_messages = "//body/div[@id='ssr-webnav']/div[1]/div[1]/nav[1]/div[4]/a[1]"
    # account
    userMenu_xpath = "//span[contains(text(),'Shuai W')]"
    logOutLink_css_selector = "a[data-qa-id='webnav-usermenu-logout']"
    #query
    query_xpath = "//body/div[@id='koMain']/div[@id='home-content']/main[@id='main']/div[@id='feed_w']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    #query select
    query_select_1 = "//h4[contains(text(),'"
    query_select_2 ="')]"

    # validation step use
    #explore page
    explore_page = "explore"
    #notification container
    notification_content = "notifications-content"
    #messages
    message_app = "MessagingApp"
    # query validation
    query_validate1 = "//h2[contains(text(),'"
    query_validate2 = "')]"
    # query negative validation
    query_nega_validation = "//span[contains(text(),'No Results Found')]"

