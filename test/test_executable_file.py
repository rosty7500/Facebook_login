from pages.functions import feature_pages


#Login scenario's

#successfull

def test_login_valid(base_url):
    valid_login = feature_pages(base_url)
    valid_login.accessing_signin_pages_valid()
    print("SUCCESSFULLY SIGNED IN")

#Invalid email

def test_invalid_login(base_url):
    invalid_login = feature_pages(base_url)
    invalid_error = invalid_login.accessing_invalid_login()
    print(invalid_error)
    invalid_message = "Sign up for an account."
    assert invalid_message == invalid_error
    if invalid_message == invalid_error:
        print("Invalid email Address")

#Invalid passoword

def test_invalid_password_login(base_url):
    invalid_login = feature_pages(base_url)
    invalid_error_password = invalid_login.accessing_invalid_password_login()
    print(invalid_error_password)
    invalid_message = "Forgotten password?"
    assert invalid_message == invalid_error_password
    if invalid_message == invalid_error_password:
        print("Invalid password")


#Miltiple logins

def test_multiple_valid_login(base_url):
    multiple_login = feature_pages(base_url)
    multiple_login.accessing_multiple_login()
    print("MULTIPLE LOGIN SUCCESSFULL")
