
door1 = """
---------------------------------------------------------------------------------------------------------------
        You leave back down the stairs.
"""
door2 = """
---------------------------------------------------------------------------------------------------------------
        You leave back down the stairs.
"""
lockedoorstory = """
---------------------------------------------------------------------------------------------------------------
        The door is locked. You need a key to open it.

        Pick Your next action:
        ***********************************
        1) Open Door Number 1.
        2) Open Door Number 2.
        3) Open Door Number 3.
        4) Go back down the stairs to the mess hall.
        ***********************************
"""
wrongcodestory = """
---------------------------------------------------------------------------------------------------------------
        The code you entered must be wrong, the padlock didnt budge.

        Pick Your next action:
        ***********************************
        1) Open Door Number 1.
        2) Open Door Number 2.
        3) Open Door Number 3.
        4) Go back down the stairs to the mess hall.
        ***********************************
"""
puzzlecomplete = """
---------------------------------------------------------------------------------------------------------------
        You try the door but it doesnt budge. You have already completed this challenge.
        
        Pick Your next action:
        ***********************************
        1) Open Door Number 1.
        2) Open Door Number 2.
        3) Open Door Number 3.
        4) Go back down the stairs to the mess hall.
        ***********************************
    
"""
class upstairsHall:
    def __init__(self):
        self.description = """
        *********************************** UPSTAIRS HALL ***********************************
        You can now see three doors. Each door is a different colour and the doors are opposite
        the bansiter which overlooks the tavern mess hall. The doors are numbered as follows:
        
       - Door Number '1' is the BLUE door - It has no key hole and a simple brass door handle.
       - Door Number '2' is the GREEN door - It has a key hole in the shape of a square.
       - Door Number '3' is the YELLOW door - It has no keyhole but,theres a latch locked with a coded padlock,
       with a 3 digit number set at '000'.
       
       **************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Open Door Number 1.
        2) Open Door Number 2.
        3) Open Door Number 3.
        4) Go back down the stairs to the mess hall.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            if game.puzzlecomplete['Puzzle1'] == 'Y':
                print (puzzlecomplete)
                return 'story'
            else:
                print (door1)
                return 'Puzzle Room One'
        elif action == '2':
            if game.puzzlecomplete['Puzzle2'] == 'Y':
                print (puzzlecomplete)
                return 'story'
            elif game.keys['squareKey'] == 'Y':
                print (door2)
                return 'Puzzle Room Two'
            else:
                self.story = lockedoorstory
                return 'story'
        elif action == '3':
            if game.puzzlecomplete['Puzzle3'] == 'Y':
                print (puzzlecomplete)
                return 'story'
            else:
                code = input("Enter the code: ")
                if code == '843':
                    return 'Puzzle Room Three'
                else:
                    print (wrongcodestory)
                    return 'story'
        elif action == '4':
            print (door1)
            return 'Tavern Hall'
        elif action == "stats":
            return 'stats'
        else:
            return None
        