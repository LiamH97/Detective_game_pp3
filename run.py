import gspread
from google.oauth2.service_account import Credentials
import time

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

time.sleep(1)
def read_storyline():
    """ A function to read from the storyline text file and give the user an idea of how the game works"""
    with open('story/storyline.txt') as f:
        storyline = f.read()
        f.close()
        print(storyline)
read_storyline()

time.sleep(5)

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
time.sleep(3)
def read_question_1():
    """A function to read the first part of the story as the game has begun"""
    with open('questions/questions.txt') as f:
        question_1 = f.readlines()
        f.close()
        print('Detective : '+ (question_1[0].format(NAME)))
read_question_1()
time.sleep(2)
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
        print('Detective: "Well we have a warrant for questioning, so I sugguest you comply"')
        print('Do you comply? \n 1 = Yes, 2 = No')
        ans1 = input()
        if ans1 == '2':
            sus +=5
            print('You were arrested and brought in for further questioning')
            #Add entry to sheet for arrested
            exit()
        elif ans1 =='1':
            pass
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_1()

ans_question_1()

print('sus = ' + str(sus)) # will be removed for final deployment, user should not see their suspiscion levels until the end

def read_story_2():
    """A function to read the second part of the story as the game has begun"""
    with open('story/story_2.txt') as f:
        story_2 = f.read()
        f.close()
        print(story_2.format(NAME))
read_story_2()
time.sleep(3)
def read_question_2():
    """A function to read the second question"""
    with open('questions/questions.txt') as f:
        question_2 = f.readlines()
        f.close()
        print('Detective : '+ (question_2[1].format(NAME)))
read_question_2()
time.sleep(2)
def ans_question_2():
    """asks the user to answer the second question raises suspiscion level if certain answers are chosen"""
    global sus
    print('How do you answer the detective\'s question? \n 1 = Yes, I\'m aware, 2 = No, I haven\'t been following the news')
    ans = input()
    if ans == '1':
        pass
    elif ans == '2':
        sus +=1
        print('Detective: "Well it\'s a fact he was last reported to be seen wandering this street by multiple witnesses and warning letters were posted to each house on this street.\"')
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_2()

ans_question_2()
time.sleep(3)
print('sus = ' + str(sus)) #remove for deployment

def read_story_3():
    """A function to read the third part of the story as the game has begun"""
    with open('story/story_3.txt') as f:
        story_3 = f.read()
        f.close()
        print(story_3.format(NAME))
read_story_3()
time.sleep(3)
def read_question_3():
    """A function to read the third question"""
    with open('questions/questions.txt') as f:
        question_3 = f.readlines()
        f.close()
        print('Detective : '+ (question_3[2].format(NAME)))
read_question_3()
time.sleep(2)
def ans_question_3():
    """asks the user to answer the third question raises suspiscion level if certain answers are chosen"""
    global sus
    print('How do you answer the detective\'s question? \n 1 = We were good friends, but I cut ties with Vinnie once he started going down the wrong path. \n 2 = Yeah, me and Vinnie are close.')
    ans = input()
    if ans == '2':
        pass
    elif ans == '1':
        sus +=1
        print('Detective: ' + (NAME) + ' You\'ve been recorded on the visitor logs as a visitor of Vinnie\'s on multiple occasions')
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_3()

ans_question_3()
def read_story_4():
    """A function to read the third part of the story as the game has begun"""
    with open('story/story_4.txt') as f:
        story_4 = f.read()
        f.close()
        print(story_4.format(NAME))
read_story_4()
time.sleep(3)