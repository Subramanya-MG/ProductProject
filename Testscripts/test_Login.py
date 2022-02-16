
from Pages.Login_Page import Login_Page
from Utilities.test_Base import test_Base


class Test_Loginn(test_Base):

    def login_functionality(self):

        self.login = Login_Page(self.driver)
        self.login.base_login_to_application()

    def test_login_functionality(self):
        log = test_Base.getLogger()
        log.info("Into Grocery Section")
        self.login = Login_Page(self.driver)
        self.login.base_login_to_application()
        self.grocery = Grocery_Page(self.driver)





