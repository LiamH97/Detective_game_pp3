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

get_username()
from detective_game import NAME
print("Hello " + (NAME) +"!")
time.sleep(1)
read_storyline()
time.sleep(8)
ask_to_begin()
read_story_1()
time.sleep(3)
read_question_1()
time.sleep(3)
ans_question_1()
# print('sus = ' + str(sus)) # will be removed for final deployment, user should not see their suspiscion levels until the end
read_story_2()
time.sleep(5)
read_question_2()
time.sleep(3)
ans_question_2()
# print('sus = ' + str(sus)) #remove for deployment
read_story_3()
time.sleep(5)
read_question_3()
time.sleep(3)
ans_question_3()
# print('sus = ' + str(sus))
time.sleep(3)
read_story_4()
time.sleep(5)
read_question_4()
time.sleep(3)
ans_question_4()
read_story_5()
time.sleep(5)
read_question_5()
time.sleep(3)
ans_question_5()
# print('sus = ' + str(sus))
read_story_6()
time.sleep(5)
read_question_6()
time.sleep(3)
ans_question_6()
print('sus = ' + str(sus))




from detective_game import *



status = 'unkown'
"""Status is used to determine whether suspiscion was raised enough for you to be arrested or free, 
the if statement below takes the sus level and assignes status the correct value based on your sus level"""
if sus >= 3:
    print('You have been brought in for further quesitioning. You raised the suspiscions of the detective')
    status = 'arrested'
else:
    print('The detective left without his suspiscion being raised enough to bring you in. Congrats' + (NAME)+ '!')
    status = 'free'
end_dict = {
	"first_name": (NAME),
	"status": (status),
	"sus_level": (sus)
}
print (status)

print (end_dict)