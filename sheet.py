import gspread
from google.oauth2.service_account import Credentials
import time
from detective_game import *

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('detective_game')
RESULTS = SHEET.worksheet('Status')
USER_LOGINS = SHEET.worksheet('login_info')


def get_login():
    """Puts the values from the login_info sheet in to a nested list"""
    login_data = USER_LOGINS.get_all_records()
    return login_data


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

def update_sheet():
    row = [(NAME),(status),(sus)]
    index = 2
    RESULTS.insert_row(row, index)