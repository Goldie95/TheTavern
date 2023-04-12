import random
story1 = """
---------------------------------------------------------------------------------------------------------------
        "Hehehe, good. Now all you have to do to pass this puzzle is answer a simple riddle.
        Lets get to it!"

        "Remember its only one word answers, traveller!"

"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        "Hehehehehehe, try again. I wont take no for an answer."

        Pick Your next action:
                ***********************************
                1) Say Yes
                3) Try and open the door you came from.
                4) Say nothing
                ***********************************

"""
story3 = """
---------------------------------------------------------------------------------------------------------------
        "No No No traveller, you must stay until you say YES! hehehehe"

        Pick Your next action:
                ***********************************
                1) Say Yes
                2) Say No
                4) Say nothing
                ***********************************

"""
story4 = """
---------------------------------------------------------------------------------------------------------------
        "Im waiting!........"

        Pick Your next action:
                ***********************************
                1) Say Yes
                2) Say No
                3) Try and open the door you came from.
                ***********************************

"""
answerCorrect = """
---------------------------------------------------------------------------------------------------------------
        "Hehehe, well done! You beat my riddle! Here is your prize!"

        The Dolls head did a full rotation and the back of the dolls head opened to reveal a key. The key is in the 
        shape of a 8 pointed star. You place it in your pocket. 
        
                                         .___,             |-|
                                        /    |\____________| | 
                                        |()  | ____________  |
                                        \    |/            | |
                                         `---'             |_|

        You turn around and leave the puzzle room.

"""
questions = [
        ("What has a head and a tail, but no body?", "coin"),       
        ("What gets wet while drying?", "towel"),    
        ("What is always in front of you but can't be seen?", "future"),    
        ("What has one eye but cannot see?", "needle"),    
        ("What starts with an E, ends with an E, but only contains one letter?", "envelope"),    
        ("What goes up but never comes down?", "Age"),    
        ("What has a neck but no head, arms, or legs?", "bottle"),    
        ("What is full of holes but still holds water?", "sponge"),    
        ("What has a thumb and four fingers, but is not alive?", "glove")
        ]
wronganswerstory = """
---------------------------------------------------------------------------------------------------------------
        "Oh no, thats the wrong answer, try again!."
"""
random_pair = random.choice(questions)

# Extract the question and answer strings from the tuple
question = random_pair[0]
answer = random_pair[1].lower()

class puzzleRoom1:
    def __init__(self):
        self.description = """
        *********************************** PUZZLE ROOM ONE ***********************************
        The room is empty apart from a small doll, sat upon a chair, the door slams behind you
        and the doll spring to life. Its manacing eye start to twitch and its jaw moves as if 
        its having a stretch. It then spoke in a girly high pitched sqeak:
        
                                           ,,,,,,,,,,,,,,,
                                        ,(((((((((())))))))),
                                      ,((((((((((()))))))))))),
                                     ,(((((((((\\\|///))))))))),
                                    ,((((((((((///|\\\)))))))))),
                                    ((((((((//////^\\\\\\))))))))
                                    ((((((' .-""-   -""-. '))))))
                                    (((((  `\.-.     .-./`  )))))
                                    ((((( -=(0) )   (0) )=- )))))
                                    '((((   /'-'     '-'\   ))))'
                                     ((((\   _,   A  ,_    /))))
                                     '((((\    \     /    /))))'
                                      '((('.     `-o-'   .')))'
                                             '-.,___,.-'
        
        "Hello traveller, i am lucy. My papa has asked me to perform this task, to get you home
        safely, if you pass" a squeaky giggle echoed around the baron windowless room. "Now are
        you ready for your first challange?"
        ***************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Say Yes
        2) Say No
        3) Try and open the door you came from.
        4) Say nothing
        ***********************************
        """
        
        self.story = ""

    def perform_action(self, game, action):
        if action == '1':
            print(story1)
            riddlepass = False
            while riddlepass == False:
                print(question)
                useranswer = input("Answer: ")
                if useranswer.lower() == answer:
                    game.keys['starKey'] = 'Y'
                    game.puzzlecomplete['Puzzle1'] = 'Y'
                    riddlepass = True
                    print(answerCorrect)
                    return 'Upstairs Hall'
                else:
                    print (wronganswerstory)
                    game.lives -= 1
                    print ("Lives left:", game.lives)
                    if game.lives == 0:
                        return 'End Game Death'
        elif action == '2':
            self.story = story2
            return 'story'
        elif action == '3':
            self.story = story3
            return 'story'
        elif action == '4':
            self.story = story4
            return 'story'
        elif action == "stats":
            return 'stats'
        else:
            return None
        