global sus
global NAME
sus = 0
with open('game/questions/questions.txt') as f:
    lines = [line.rstrip() for line in f]
def get_username():
    """ Asks the user for their name and stores it as a variable {name} """
    global NAME
    NAME = input('What is your name? \n')
    if not NAME.isalpha():
        print('Please enter only alphabetical characters')
        get_username()
    return NAME
def read_storyline():
    """ A function to read from the storyline text file and give the user an idea of how the game works"""
    with open('game/story/storyline.txt') as f:
        storyline = f.read()
        f.close()
        print(storyline)

def ask_to_begin():
    """Asks the user if they would like to begin the game"""
    begin = input('Would you like to begin? \n 1 = Yes, 2 = No \n')
    if begin == '1':
        pass
    elif begin == '2':
        print('Okay, maybe next time! Goodbye')
        exit()
    else: 
        print('Invalid entry please select option 1 or 2')
        ask_to_begin()
def read_story_1():
    """A function to read the first part of the story"""
    with open('game/story/story_1.txt') as f:
        story_1 = f.read()
        f.close()
        print(story_1)

def read_question_1():
    """A function to read the first part of the story"""
    print('Detective : '+ (lines[0].format(NAME)))

def ans_question_1():
    """asks the user to answer the first question raises suspiscion level if certain answers are chosen"""
    global sus
    sus = 0
    ans = input('Let the detective in to talk? \n 1 = Yes, 2 = No \n')
    if ans == '1':
        pass
    elif ans == '2':
        sus +=1
        print('Detective: "Well we have a warrant for questioning, so I sugguest you comply"')
        ans1 = input('Do you comply? \n 1 = Yes, 2 = No \n')
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

def read_story_2():
    """A function to read the second part of the story"""
    with open('game/story/story_2.txt') as f:
        story_2 = f.read()
        f.close()
        print(story_2.format(NAME))

def read_question_2():
    """A function to read the second question"""
    print('Detective : '+ (lines[1].format(NAME)))

def ans_question_2():
    """asks the user to answer the second question raises suspiscion level if certain answers are chosen"""
    global sus
    ans = input('How do you answer the detective\'s question? \n 1 = Yes, I\'m aware, 2 = No, I haven\'t been following the news \n')
    if ans == '1':
        pass
    elif ans == '2':
        sus +=1
        print('Detective: "Well it\'s a fact he was last reported to be seen wandering this street by multiple witnesses and warning letters were posted to each house on this street.\"')
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_2()
def read_story_3():
    """A function to read the third part of the story"""
    with open('game/story/story_3.txt') as f:
        story_3 = f.read()
        f.close()
        print(story_3.format(NAME))

def read_question_3():
    """A function to read the third question"""
    print('Detective : '+ (lines[2].format(NAME)))

def ans_question_3():
    """asks the user to answer the third question raises suspiscion level if certain answers are chosen"""
    global sus
    ans = input('How do you answer the detective\'s question? \n 1 = We were good friends, but I cut ties with Vinnie once he started going down the wrong path. \n 2 = Yeah, me and Vinnie are close. \n')
    if ans == '2':
        pass
    elif ans == '1':
        sus +=1
        print('Detective: "' + (NAME) + ' You\'ve been recorded on the visitor logs as a visitor of Vinnie\'s on multiple occasions"')
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_3()

def read_story_4():
    """A function to read the fourth part of the story """
    with open('game/story/story_4.txt') as f:
        story_4 = f.read()
        f.close()
        print(story_4.format(NAME))
def read_question_4():
    """A function to read the fourth question"""
    print('Detective : '+ (lines[3].format(NAME)))
def ans_question_4():
    """asks the user to answer the fourth question raises suspiscion level if certain answers are chosen"""
    global sus
    ans = input('How do you answer the detective\'s question? \n 1 = Like you said - we were good friends. We just talked about old times . \n 2 = We discussed future business opportunities once Vinne was officially released from prison \n')
    if ans == '2':
        pass
    elif ans == '1':
        sus +=1
        print('Detective: "That\'s interesting considering the letter we intercepted from Vinnie addressed to you. He spoke about business opportunities you two had planned for when he \'gets out\'"')
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_4()

def read_story_5():
    """A function to read the fifth part of the story"""
    with open('game/story/story_5.txt') as f:
        story_5 = f.read()
        f.close()
        print(story_5.format(NAME))

def read_question_5():
    """A function to read the fifth question"""
    print('Detective : '+ (lines[4].format(NAME)))

def ans_question_5():
    """asks the user to answer the fifth question raises suspiscion level if certain answers are chosen"""
    global sus
    ans = input('How do you answer the detective\'s question? \n 1 = No, never. He always kept his crime life separate from our friendship. \n 2 = He had mentioned a hiding place to me but I refused to hear of it. I didn\'t want to be involved. \n')
    if ans == '2':
        pass
    elif ans == '1':
        sus +=1
        print('Detective: "Come on, you know we intercepted the letter ' + (NAME) + ', he clearly mentioned wanting to follow up on your discussion about his hiding place')
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_5()
def read_story_6():
    """A function to read the fifth part of the story"""
    with open('game/story/story_6.txt') as f:
        story_6 = f.read()
        f.close()
        print(story_6.format(NAME))
def read_question_6():
    """A function to read the fifth question"""
    print('Detective : '+ (lines[5].format(NAME)))

def ans_question_6():
    """asks the user to answer the fifth question raises suspiscion level if certain answers are chosen"""
    global sus
    ans = input('How do you answer the detective\'s question? \n 1 = He has a girlfriend that lives around this area. He could be with her. \n 2 = I wish I could help, but i really don\'t know \n')
    if ans == '2':
        pass
    elif ans == '1':
        sus +=1
        print('Detective: "We looked into his girlfriend, her home address is registered as 5km from here. Vinnie was spotted on this street, not 5km away."')
    else:
        print('invalid entry, please select option 1 or 2')
        ans_question_6()