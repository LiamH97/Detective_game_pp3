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
global sus
sus = 0

def get_username():
    """ Asks the user for their name and stores it as a variable {name} """
    print("What is your name?")
    global NAME
    NAME = input()
    if not NAME.isalpha():
        print('Please enter only alphabetical characters')
        get_username()
    return NAME
print("Hello " + get_username() +"!")

def read_storyline():
    """ A function to read from the storyline text file and give the user an idea of how the game works"""
    with open('story/storyline.txt') as f:
        storyline = f.read()
        f.close()
        print(storyline)
read_storyline()

def ask_to_begin():
    """Asks the user if they would like to begin the game"""
    print('Would you like to begin? \n 1 = Yes, 2 = No')
    begin = input()
    if begin == '1':
        pass
    elif begin == '2':
        print('Okay, maybe next time! Goodbye')
        exit()
    else: 
        print('Invalid entry')
        ask_to_begin()
ask_to_begin()

def read_story_1():
    """A function to read the first part of the story as the game has begun"""
    with open('story/story_1.txt') as f:
        story_1 = f.read()
        f.close()
        print(story_1)
read_story_1()
def read_question_1():
    """A function to read the first part of the story as the game has begun"""
    with open('questions/question_1.txt') as f:
        story_1 = f.read()
        f.close()
        print('Detective : '+ (story_1.format(NAME)))
read_question_1()
def ans_question_1():
    """asks the user to answer the first question raises suspiscion level if certain answers are chosen"""
    global sus
    sus = 0
    print('Let the detective in to talk? \n 1 = Yes, 2 = No')
    ans = input()
    if ans == '1':
        pass
    elif ans == '2':
        sus +=1
        print('Well we have a warrant for questioning, so I sugguest you comply')
        print('Do you comply? \n 1 = Yes, 2 = No')
        ans1 = input()
        if ans1 == '2':
            sus +=5
            print('You were arrested and brought in for further questioning')
            exit()
        elif ans1 =='1':
            pass
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_1()

ans_question_1()
print('sus = ' + str(sus)) # will be removed for final deployment, user should not see their suspiscion levels until the end
