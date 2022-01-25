from detective_game import *
from sheet import *
login()
get_username()
from detective_game import NAME
print ("Hello " + (NAME) + "!")
time.sleep(1)
read_storyline()
time.sleep(8)
ask_to_begin()
read_story_1()
time.sleep(3)
read_question_1()
time.sleep(3)
ans_question_1()
read_story_2()
time.sleep(5)
read_question_2()
time.sleep(3)
ans_question_2()
read_story_3()
time.sleep(5)
read_question_3()
time.sleep(3)
ans_question_3()
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
read_story_6()
time.sleep(5)
read_question_6()
time.sleep(3)
ans_question_6()
read_story_7()
time.sleep(5)
read_question_7()
time.sleep(3)
ans_question_7()


status = 'unkown'
"""Status is used to determine whether suspiscion was raised enough
for you to be arrested or free,
the if statement below takes the sus level
 and assignes status the correct value based on your sus level"""


from sheet import *


def update_sheet():
    row = [(NAME), (status), (sus)]
    index = 2
    RESULTS.insert_row(row, index)
from detective_game import sus
if sus >= 3:
    print('You have been brought in for further quesitioning. You raised the suspiscions of the detective')
    status = 'arrested'
    update_sheet()
    begin = input('Would you like to try again? \n 1 = Yes, 2 = No \n')
    if begin == '1':
        pass
    elif begin == '2':
        print('Okay, maybe next time! Goodbye')
        exit()
    else:
        print('Invalid entry please select option 1 or 2')
        ask_to_begin()
else:
    print('The detective left without his suspiscion being raised enough to bring you in. Congrats ' + (NAME) + '!')
    status = 'free'
    update_sheet()
