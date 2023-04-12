import random
import time

story1 = """
---------------------------------------------------------------------------------------------------------------
        BOING BOING
       "Whats up? too scared traveller? Mwhahahaha, do you want to play?"
        
        Pick Your next action:
        ***********************************
        1) Nod your Head.
        3) Try pushing the Jack back in the box.
        4) Try and run.
        ***********************************
"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        You sucessfully push the Jack back in the box, but as you walk away he pops right back up.
        
        "BOO!"
        
        He grins.
        
        "You cant get rid of me that easily traveller. Mwhahaha, are you ready to play now?"
        
        Pick Your next action:
        ***********************************
        1) Nod your Head.
        3) Try pushing the Jack back in the box.
        4) Try and run.
        ***********************************
        
"""
story3 = """
---------------------------------------------------------------------------------------------------------------
        You run towards the door and find its locked, Jack in the box laughs at your silliness.
        
        "Mwhahahahahaha, nowhere to run, nowhere to hide. Are you ready to play?"
        
                Pick Your next action:
        ***********************************
        1) Nod your Head.
        2) Shake your head.
        3) Try pushing the Jack back in the box.
        ***********************************
"""
wronganswer = """
---------------------------------------------------------------------------------------------------------------
        "NO NO NO THATS THE WRONG ANSWER MWHAHAHAHAAH, Guess again traveller"
"""
correctanswer = """
---------------------------------------------------------------------------------------------------------------
        "Hmmm, maybe that was too easy, but fair is fair."
        
        The Jack in the Box bounces back inside in its box. The air falls silent.
        
        Suddenly, the box unfolds, with the Jack nowhere to be seen it reveals key, this time in the shape a 
        sqaure. You place it in your pocket.
        
                                         .___,             |-|
                                        /    |\____________| | 
                                        |()  | ____________  |
                                        \    |/            | |
                                         `---'             |_|
                                         
        You turn and leave the room.        
"""
puzzleinstructions = """
---------------------------------------------------------------------------------------------------------------
        "Okay, you have 3 minutes to solve the anagram, each guess that is wrong you will lose a life, if you run 
        out of time, you will DIEEEEEEEEE mwhahahahahahaha"

        The Jack in the box jumps up and down in excitment. 

        "Are you ready?"
"""
door1 = "You suxessfully open the door to your left revealing another room."
# List of anagrams to choose from
anagrams = ["triangle", "reptile", "galaxy", "tavern", "treason"]

# Select a random anagram from the list
anagram = random.choice(anagrams)
scrambled_word = ''.join(random.sample(anagram, len(anagram)))
         
class puzzleRoom3:
    def __init__(self):
        self.description = """
        *********************************** PUZZLE ROOM THREE ***********************************
        The room is bigger than you thought it would be, though the ceiling was low and slanted, 
        like an attic. In the center is a giant box and as you edge closer out pops a Jack in the
        box swaying after it sprung you hear the door slam behind you. 
        
                                                 0_
                                                   \`.     ___
                                                    \ \   / __>0
                                                /\  /  |/' / 
                                               /  \/   `  ,`'--.
                                              / /(___________)_ |
                                             |/ //.-.   .-.\ \ |
                                             0 // :@ ___ @: \ \/
                                               ( o ^(___)^ o ) 0
                                                \ \_______/ /
                                            /\   '._______.'--.
                                            \ /|  |<_____>    |
                                             \ \__|<_____>____/|__
                                              \____<_____>_______/
                                                  |<_____>    |
                                                  |<_____>    |
                                                  :<_____>____:
                                                 / <_____>   /|
                                                /  <_____>  / |
                                                /___________/  |
                                                |           | _|__
                                                |           | ---||_
                                                |   |L\/|/  |  | [__]
                                                |  \|||\|\  |  /
                                                |           | /
                                                |___________|/
                                                
        * BOING BOING *
        
        "HALLOW, Traveller, my name is Jackery Symbone, i am here to issue you another challenge, if
        you pass you can have a prize. ROLL UP ROLL UP here is your challange. I have a series of 
        letters that make up a jumbled word, you have to ,wooooooooooooooooo, get the anagram, 
        sound like fun?"
        
        * BOING BOING *
        *****************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Nod your Head.
        2) Shake your head.
        3) Try pushing the Jack back in the box.
        4) Try and run.
        ***********************************
        """
        
        self.story = ""

    def perform_action(self, game, action):
        if action == '1':
            print (puzzleinstructions)
            ready = input("<Press ENTER when youre ready>")
            print ("╔════════════════════════════════════════════════════════════════════════╗ ")
            print ("                           ", scrambled_word.upper())
            print ("╚════════════════════════════════════════════════════════════════════════╝")
            
                # Get user's guess
            guess = input("Enter your guess: ").lower()
                
            # Check if guess is correct
            if guess == anagram:
                game.keys['squareKey'] = 'Y'
                print(correctanswer)
                game.puzzlecomplete['Puzzle3'] = 'Y'
                return 'Upstairs Hall'
                
            else:
                print(wronganswer)
                game.lives -= 1
                print ("Lives left:", game.lives)
                if game.lives == 0:
                    return 'End Game Death'
                               
        elif action == '2':
            self.story = story1
            return 'story'
        elif action == '3':
            self.story = story2
            return 'story'
        elif action == '4':
            self.story = story3
            return 'story'
        elif action == "stats":
            return 'stats'
        else:
            return None
        