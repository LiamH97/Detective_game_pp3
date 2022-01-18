import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('detective_game')

def get_username():
    """ Asks the user for their name and stores it as a variable {name} """
    print("What is your name?")
    name = input()
    if not name.isalpha():
        print('Please enter only alphabetical characters')
        get_username()
    return name
print("Hello " + get_username() +"!")

def read_storyline():
    """ A function to read from the storyline text file and give the user an idea of how the game works"""
    f = open('storyline.txt', 'r')
    storyline = f.read()
    f.close()
    print(storyline)
read_storyline()

def start_game():
    """Temporary function for starting the game to test it is called correctly"""
    print('start game function called')
def ask_to_begin():
    """Asks the user if they would like to begin the game"""
    print('Would you like to begin? \n 1 = Yes, 2 = No')
    begin = input()
    if begin == '1':
        start_game()
    elif begin == '2':
        print('Okay, maybe next time! Goodbye')
        exit()
    else: 
        print('Invalid entry')
        ask_to_begin()
ask_to_begin()
