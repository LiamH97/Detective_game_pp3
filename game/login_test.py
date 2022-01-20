from sheet import *

def login():
    """function to check user and password for verification. Comparing with google sheet data"""
    user_id = input('Please enter your username \n')
    user_pw = input('Please enter your password \n')
    logins = get_login()
    if not [i for i in logins if i['Username'] == user_id]:
        print('\nUsername does not exist')
        print('\nPlease try again.')
        login()
    else:
        correct_uid = [i for i in logins if i['Username'] == user_id][0]
    if user_pw == correct_uid['Password']:
        print('\nLogin complete')
    else:
        print('\nPassword did not match for the username enetered.')
        print('\nPlease try again.')
        login()

