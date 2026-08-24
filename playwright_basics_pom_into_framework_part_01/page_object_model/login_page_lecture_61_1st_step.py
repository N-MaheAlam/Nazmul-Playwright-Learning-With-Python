from playwright_basics_pom_into_framework_part_01.page_object_model.dashboard_page_lecture_61_62__2nd_step import \
    Dashboard


class LoginPage:
    def __init__(self, page):
        # "self.page is local instance variable that is accessible by the all the functions that are
        # present in this class and "page" is the argument that we are getting as an argument
        # in constructor when we create an object of this class
        self.page = page

    def navigate_to_login_page(self):
        # self is used to call the instance and local variable of this "LoginPage" class from constructor

        self.page.goto("https://rahulshettyacademy.com/client")

    # when we use this method, it provides login and password details and clicks on log in button
    # which land us in dashboard page. that means once we log in and as it takes to our dashboard page
    # so why don't we create an object of Dashboard and return once the login is done. Then we can
    # make a variable of dashboard type when this method is called and can perform our methods that
    # are present in Dashboard class right? As this method is returning Dashboard type something
    def provide_username_password_and_click_log_in(self, username, password):
        self.page.get_by_placeholder("email@example.com").fill(username)
        self.page.locator("#userPassword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = Dashboard(self.page)
        return dashboard_page
