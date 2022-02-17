from selenium.webdriver.common.by import By

from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


class User_DashBoard_Page(Base_Page):
    #Webelements of the page
    PENDING_QUIZ_BUTTON = (By.XPATH, "//span[text()='Pending Quiz']/parent::div")
    COMPLETED_QUIZ_BUTTON = (By.XPATH, "//span[text()='Completed Quiz']/parent::div")

    def __init__(self, driver):
        super().__init__(driver)

    def click_pending_quiz_button(self):
        log = test_Base.getLogger()

        self.click_operation(User_DashBoard_Page.PENDING_QUIZ_BUTTON)
        log.info("Pending quiz button is clicked")

    def click_completed_quiz_button(self):
        log = test_Base.getLogger()

        self.click_operation(User_DashBoard_Page.COMPLETED_QUIZ_BUTTON)
        log.info("Completed quiz button is clicked")