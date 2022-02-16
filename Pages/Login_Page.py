from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


class Login_Page(Base_Page):
    LOGIN_POPUP = (By.XPATH, "// a[ @ href = '/account/login?ret=/']")
    EMAIL_ADDRESS = (By.XPATH, "// input[ @ class ='_2IX_2- VJZDxU']")
    PASSWORD = (By.XPATH, "// input[@ class ='_2IX_2- _3mctLh VJZDxU']")
    LOGIN_BUTTON = (By.XPATH, "// button[@ class ='_2KpZ6l _2HKlqd _3AWRsL']")
    EMAIL_CLASSNAME = "_2IX_2- VJZDxU"
    PASSWORD_CLASSNAME = "_2IX_2- _3mctLh VJZDxU"
    GET_USER_NAME = (By.XPATH,
                     "//*[text()='More']/ancestor::div[@class='go_DOp']//preceding-sibling::div[@class='go_DOp']//div[@class='exehdJ']")

    def __init__(self, driver):
        super().__init__(driver)

    def base_login_to_application(self):
        log = test_Base.getLogger()
        dict_d = {}
        log.info("Getting Test Data")
        dict_d = Test_Data.getTestData(self, "test_Login")
        log.info("Entering the url")
        self.enter_url_operation(dict_d["url"], Login_Page.LOGIN_POPUP)
        log.info("Entering the Username")
        self.send_keys_operation(Login_Page.EMAIL_ADDRESS, dict_d["username"])
        #self.send_keys_operation(Login_Page.EMAIL_ADDRESS, "ttt")
        log.info("Entering the Password")
        self.send_keys_operation(Login_Page.PASSWORD, dict_d["password"])
        log.info("Clicking login button")
        self.click_operation(Login_Page.LOGIN_BUTTON)
        user = self.get_text_from_locator(Login_Page.GET_USER_NAME)
        log.info("Validating if the user is successfully logged in")
        assert user == dict_d["logged_in_user"]
        log.info("user is successfully logged in the account")
