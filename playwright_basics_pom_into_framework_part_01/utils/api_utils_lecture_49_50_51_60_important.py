from playwright.sync_api import Playwright

# Creating this order step by step in rahul shetty academy page and when we will click the
# create order button before that open the network tab then click. Once it gets created from network
# find the "create-order" from "name" and from "Payload" collect this data in "View source" mode so that
# you get the json format which is a dictionary format in python
order_details_payload = {"orders": [{"country": "Canada", "productOrderedId": "6960ea76c941646b7a8b3dd5"}]}

# When we will click on the "Log In" button before that open the network tab then click.Once you logged in
# # find the "login" from "name" and from "Payload" collect this data in "View source" mode so that
# # you get the json format which is a dictionary format in python
login_payload = {"userEmail": "nazmul2811@diu.edu.bd", "userPassword": "Rh@r12345512"}


class APIValidationFirstClass:
    # one argument is for playwright and another is to intercept the json file "user_details"
    # from where we will collect the user details login and password that are already in dictionary type.
    # Our goal  is make the code readable and no hard code means, no data such as username, password
    # tag names should not be directly placed in the code. If you see the method it takes the username and
    # password as data in request post which we do not want to hard code. We already have this username
    # and password in json file and using the fixture "each_user_credential_fixture" we can collect it.
    # So, we are calling the "each_user_credential_fixture['user_email']" and storing in "email" and
    # also calling "each_user_credential_fixture['user_password']" storing in "password" variable. As we
    # are using the "each_user_credential_fixture" to collect the json data, we are sending this
    # fixture as an argument in this method, converting hard code in readable professional code where
    # data are hidden.

    def token_for_login_details(self, playwright: Playwright, each_user_credential_fixture):
        # to call chrome, firefox we used chromium or firefox after "playwright" but when
        # we want to validate api, we use "request". Then "new_context(), connecting us with the server,
        # and we provide our arguments inside the parameter such as ["base-url" = The url of the main page
        # we do not use new_page() as we are not opening any page here, but we are getting,posting, putting,
        #  or updating in APIs. that's why we use post
        # REMEMBER ------
        # "https://rahulshettyacademy.com//api/ecom/auth/login" in this whole url,
        # the base url is "https://rahulshettyacademy.com" and rest "/api/ecom/auth/login" we call
        # it as "resources"
        # storing in "email" the user email
        email = each_user_credential_fixture['user_email']
        # storing the password in "password" variable
        password = each_user_credential_fixture['user_password']
        login_request_url = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        # Now, we will post our request providing the "resources" url, then data we are parsing
        # "login_payload" variable
        login_response = (
            login_request_url.post(url="/api/ecom/auth/login",
                                   # calling the email and password variable
                                   data={"userEmail": email, "userPassword": password}))
        # If log in is successful, the assertion will pass
        assert login_response.ok
        # Grab the response body in json format once we logged in successfully
        login_response_body = login_response.json()
        # print in console
        print("\nCame from API validation class: -> Log in successful and response: ", login_response_body)
        # As the response is in json format, it's a dictionary, and we are extracting the value
        # of index name "token" from the json response and returning in this function
        return login_response_body["token"]

    def create_order_api_validation_rahul_shetty(self, playwright: Playwright, each_user_credential_fixture):
        # calling the above function inside this function using 'self'. as the above function has an
        # argument which type is "Playwright", we are giving the instance variable "playwright" which
        # is declared in this function argument (self, playwright <- this one : Playwright). And
        # as the "token_for_login_details" method takes 2 arguments to provide the email and password
        # we need to give also the 2nd argument "each_user_credential_fixture". To call a method
        # we must make sure we also provide the arguments.
        token = self.token_for_login_details(playwright, each_user_credential_fixture)
        # to call chrome, firefox we used chromium or firefox after "playwright" but when
        # we want to validate api, we use "request". Then "new_context(), connect us with the server,
        # and we provide our arguments inside the parameter such as ["base-url" = The url of the main page
        # REMEMBER ------
        # "https://rahulshettyacademy.com/api/ecom/order/create-order" in this whole url,
        # the base url is "https://rahulshettyacademy.com" and rest "/api/ecom/order/create-order" we call
        # it as "resources"
        api_request_connection = (
            playwright.request.new_context(base_url="https://rahulshettyacademy.com"))
        # Now the "api_request_connection" variable is posting something and for that post we need
        # to give arguments. So, the "url" is the resources that are partially attached with actual
        # link. Now, "data" is "order_details_payload" variable where we stored our payload I mean
        # from which country I am ordering and which product. We can get this my creating order in the
        # rahul shetty website and check in network tab once we create the order where you will see
        # something like "create-order". Click on "Payload" and click on "View resource". Copy the json
        # file and store it in "order_details_payload" and put this in "data" argument in the below
        # post connection. Now, "headers" in this function is dictionary type and this header we will
        # pass the "authorisation" key, "content-type [ This will give the response in json format ]".
        # This content type can be found in "create -order" network "Headers".

        # Now, the "token" we need to generate it by calling the log in function or "file. content-type"
        # comes from the Headers in network file of that create-order api call
        response_create_order = api_request_connection.post(url="/api/ecom/order/create-order",
                                                            data=order_details_payload,
                                                            headers={"authorization": token,
                                                                     "content-type": "application/json"}, )
        # printing the details of that order in json format in console which have "orders",
        # "productOrderId", "message"
        print("\nAPI validation Class: -> Order Placed thorough API: ", response_create_order.json())
        # If you notice in console after calling the test function "test_e2e_web_api_check" in file
        # "test_lecture_58_59_60_data_calling_from_json_file_e2e_important.py" you will see the response is in json
        # which is in dictionary format. Inside the dictionary "values" are in list format
        # --- [] -> list , {} - dictionary, () -> tuple
        # in the list there only one value for each key, and these values are present in index 0,
        # which I am collecting only for "order" key
        order_id = response_create_order.json()["orders"][0]
        # Printing the API order number
        print("\nAPI validation class:-> Order ID from API:", order_id)
        # at the end of everything we are returning this "order_id". So, when ever this function will be
        # called, it will always return the order id, which we can use to click, visible and so on
        # playwright codes in the UI
        return order_id
