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
